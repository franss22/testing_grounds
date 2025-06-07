from chlib import chutil
from chlib.DatabaseConnection import DatabaseConnection
from sqlalchemy import text
from sqlalchemy.sql.elements import TextClause
from enum import Enum
from typing import Tuple, TypedDict


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
    comment: str = snippet.get("comment", "").strip()
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
