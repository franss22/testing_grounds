"""Auto-generated script for gen_calzo with trigger on_create."""

from lib import QueryRunner

runner = QueryRunner()

"""
This is a comment for snippet 1
With newlines!
"""
runner.add_query("""SELECT * FROM table;""")

"""
This is a comment for snippet 2, with new changes
"""
runner.add_query("""SELECT * FROM table WHERE id = 1;""")


if __name__ == "__main__":
    runner.run_all_queries()
