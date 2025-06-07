from gen_scripts.lib import EntityTrigger, generate_script, Snippet, Trigger

entity: str = "gen_calzo"
trigger = Trigger.ON_CREATE


snippets: list[Snippet] = [
    {"comment": "This is a comment for snippet 1\nWith newlines!", "query": "SELECT * FROM table;"},
    {"comment": "This is a comment for snippet 2, with new changes", "query": "SELECT * FROM table WHERE id = 1;"},
]

author: str = "Auto Script Generator"
author_mail: str = "auto@coderhub.cl"

entity_trigger : list[EntityTrigger] = [
    (entity, trigger, snippets),
]

def main():
    from pr_maker import generate_and_upload_scripts
    generate_and_upload_scripts(entity_trigger, author, author_mail)


if __name__ == "__main__":
    main()
