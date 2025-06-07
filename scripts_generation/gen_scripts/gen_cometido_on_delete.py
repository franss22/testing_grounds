"""Auto-generated script for gen_cometido with trigger on_delete."""

from lib import QueryRunner

runner = QueryRunner()

"""
This is a comment for snippet 1
With newlines!
"""
runner.add_query("""SELECT * FROM table;""")

"""
This is a comment for snippet 2, with new changes
Wow, even more cahnges
"""
runner.add_query("""SELECT * FROM table WHERE id = 1;""")

"""
No comment provided.
"""
runner.add_query("""UPDATE table SET id = 1;""")


if __name__ == "__main__":
    runner.run_all_queries()
