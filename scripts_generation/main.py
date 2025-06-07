from gen_scripts.lib import generate_script, Snippet, Trigger

entity: str = "gen_calzo"
trigger = Trigger.ON_CREATE


snippets: list[Snippet] = [
    {"comment": "This is a comment for snippet 1\nWith newlines!", "query": "SELECT * FROM table;"},
    {"comment": "This is a comment for snippet 2", "query": "SELECT * FROM table WHERE id = 1;"},
]


def main():
    script, path = generate_script(snippets, entity, trigger)
    with open(path, "w") as file:
        file.write(script)


if __name__ == "__main__":
    main()
