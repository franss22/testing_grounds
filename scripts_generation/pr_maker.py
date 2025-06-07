import subprocess
import time

from gen_scripts.lib import EntityTrigger, Snippet


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
    cmd = f"gh pr create --title '{pr_title}' --body '{pr_body}' --base master"
    run_cmd(cmd)
    print("Pull request created.")
    print("returning to main branch...")
    run_cmd("git checkout master")
    print("Switched back to main branch.")
    print("Done.")


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
