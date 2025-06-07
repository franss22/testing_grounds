from gen_scripts.lib import EntityTrigger, Snippet, Trigger, generate_and_upload_scripts


snippets: list[Snippet] = [
    {"comment": "This is a comment for snippet 1\nWith newlines!", "query": "SELECT * FROM table;"},
    {
        "comment": "This is a comment for snippet 2, with new changes\nWow, even more cahnges",
        "query": "SELECT * FROM table WHERE id = 1;",
    },
    {"comment": None, "query": "UPDATE table SET id = 1;"},
]

author: str = "Auto Script Generator"
author_mail: str = "auto@coderhub.cl"

entity_trigger: list[EntityTrigger] = [
    ("gen_calzo", Trigger.ON_CREATE, snippets),
    ("gen_calzo", Trigger.ON_DELETE, snippets),
]


def main():

    generate_and_upload_scripts(entity_trigger, author, author_mail)


if __name__ == "__main__":
    main()
