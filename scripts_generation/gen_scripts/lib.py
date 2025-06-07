from chlib import chutil
from chlib.DatabaseConnection import DatabaseConnection
from sqlalchemy import text
from sqlalchemy.sql.elements import TextClause
from enum import Enum
from typing import Tuple, TypedDict
import subprocess
import time

BASE_BRANCH = "master"  # Base branch for pull requests


class QueryRunner:
    """Clase para ejecutar consultas que vengan desde un script autogenerado a partir de snippets."""

    db_connection: DatabaseConnection
    input_args: chutil.InputArgs
    queries: list[TextClause]

    def __init__(self) -> None:
        config = chutil.loadConfigFile()
        self.db_connection = DatabaseConnection.fromConf(config)
        self.input_args = chutil.loadInputArgs()
        self.queries = []

    def add_query(self, query: str) -> None:
        """Añade una consulta SQL a la lista de consultas."""
        self.queries.append(text(query))

    def run_all_queries(self) -> None:
        """Ejecuta todas las consultas almacenadas."""
        with self.db_connection.get_connection() as conn:
            with conn.begin():
                for query in self.queries:
                    conn.execute(query, self.input_args)


class Snippet(TypedDict):
    """
    A class to represent a code snippet.
    """

    comment: str | None
    query: str


class Trigger(Enum):
    """
    An enumeration for different types of triggers.
    """

    ON_CREATE = "on_create"
    ON_UPDATE = "on_update"
    ON_DELETE = "on_delete"


EntityTrigger = tuple[str, Trigger, list[Snippet]]


def docstring(snippet: Snippet) -> str:
    """
    Formats a comment as a docstring.
    """
    comment: str = (snippet.get("comment") or "").strip()
    if not comment:
        return '"""\nNo comment provided.\n"""'

    # if the comment contains newlines, format it as a multi-line docstring
    return f'"""\n{comment}\n"""'


def generate_script(snippets: list[Snippet], entity: str, trigger: Trigger) -> Tuple[str, str]:
    """
    Generates a script based on the provided snippets, entity, and trigger.
    """
    script_template = f'''"""Auto-generated script for {entity} with trigger {trigger.value}."""

from lib import QueryRunner

runner = QueryRunner()

{"\n".join([f'{docstring(q)}\nrunner.add_query("""{q["query"]}""")\n' for q in snippets])}

if __name__ == "__main__":
    runner.run_all_queries()
'''
    return script_template, f"./gen_scripts/{entity}_{trigger.value}.py"


def run_cmd(cmd: str) -> subprocess.CompletedProcess[str]:
    """Run a command."""
    try:
        return subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command '{cmd}': {e.stderr}")
        raise e


def changes_exist() -> bool:
    """Check for changes in the repository."""
    cmd = "git diff --exit-code --quiet"
    result = subprocess.run(cmd, shell=True)
    if result.returncode > 1:
        raise RuntimeError(f"Unexpected return code {result.returncode} from command '{cmd}'")
    return result.returncode == 1


def commit_changes(file_list: list[str], author: str, author_mail: str) -> None:
    """Commit changes to the repository."""
    if not file_list:
        print("No files to commit.")
        return

    branch_name = f"feat/auto_script_{time.strftime('%Y%m%d_%H%M%S')}"
    cmd = f"git checkout -b {branch_name}"
    run_cmd(cmd)
    print(f"Created and checked out branch: {branch_name}")

    cmd = f"git add {' '.join(file_list)}"
    run_cmd(cmd)

    commit_msg = "Auto-generated script changes"
    cmd = f"git -c user.name='{author}' -c user.email='{author_mail}' commit -m '{commit_msg}'"
    run_cmd(cmd)
    print(f"Committed changes: {commit_msg}")


def push_and_pr(file_list: list[str], author: str) -> None:
    """Push changes and create a pull request."""
    if not file_list:
        print("No files to push.")
        return

    cmd = "git push --set-upstream origin HEAD"
    run_cmd(cmd)
    print("Pushed changes to remote repository.")

    pr_title = f"Auto-generated script changes by {author}, {time.strftime('%Y-%m-%d %H:%M:%S')}"
    pr_body = "This PR contains auto-generated script changes for:\n\n- " + "\n- ".join(file_list)
    cmd = f"gh pr create --title '{pr_title}' --body '{pr_body}' --base {BASE_BRANCH}"
    pr = run_cmd(cmd)
    print("Pull request created.")
    print("returning to main branch...")
    run_cmd(f"git checkout {BASE_BRANCH}")
    print("Switched back to main branch.")
    print(f"You can review the PR at {pr.stdout}")


def generate_and_upload_scripts(entity_triggers: list[EntityTrigger], author: str, author_mail: str) -> None:
    """Generate scripts and upload them to the repository."""
    from gen_scripts.lib import generate_script  # Import here to avoid circular imports

    file_list = []
    for entity, trigger, snippets in entity_triggers:
        script, path = generate_script(snippets, entity, trigger)
        with open(path, "w") as file:
            file.write(script)
        file_list.append(path)

    if changes_exist():
        commit_changes(file_list, author, author_mail)
        push_and_pr(file_list, author)
    else:
        print("No changes detected. No commit or PR created.")
