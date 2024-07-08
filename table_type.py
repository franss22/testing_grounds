from typing import Any, Literal
from chlib.DatabaseConnection import DatabaseConnection
import argparse
from pathlib import Path

base_entity = set(
    [
        "id",
        "name",
        "color",
        "text_color",
        "area_id",
        "owner_id",
        "valid",
    ]
)


def type_hint(type_sql: str, nullable: Literal["YES"] | Literal["NO"], default: str) -> str:
    type_hint: str
    if type_sql == "char(36)":
        type_hint = "ID"
    elif type_sql.startswith("varchar"):
        type_hint = "str"
    elif type_sql.startswith("date"):
        type_hint = "datetime"
    elif "int" in type_sql:
        type_hint = "int"
    elif type_sql == "float":
        type_hint = "float"
    else:
        raise Exception(f"SQL type not recognized: {type_sql}")

    or_none = " | None" if nullable == "YES" else ""

    return f"{type_hint}{or_none}"


def parse_table_columns(conn: Any, bdd: str, table_name: str, custom_name: str) -> str:
    table_data = conn.execute(
        f"""select COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT
                from INFORMATION_SCHEMA.COLUMNS
                where TABLE_NAME='{table_name}'
                AND TABLE_SCHEMA='{bdd}'"""
    )
    table_data = [column for column in table_data]
    if len(table_data) == 0:
        print(f"Table {table_name} not found")
        return ""
    parsed_columns = []

    is_base_entity = base_entity.issubset(set([col_name for col_name, _, _, _ in table_data]))
    definition = (
        f"class {custom_name.capitalize() or table_name.capitalize()}"
        f'({"BaseEntity" if is_base_entity else "TypedDict"}):\n'
        f'    """Diccionario tipado generado para la tabla {table_name}."""\n\n'
    )

    for col_name, type, nullable, default in table_data:
        if is_base_entity and col_name in base_entity:
            continue
        parsed_columns.append(f"    {col_name}: {type_hint(type, nullable, default)}")

    return definition + "\n".join(parsed_columns) + "\n"


"""
Generate argparse parser for a python command that takes in:
- a list of table names
- database name
- database user and password, with default value "root:"
- database port, with default value "3306"
- filename to write in, with default value "tipos_bdd.py"
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser("Generar un archivo con los tipos de las tablas especificadas.")
    parser.add_argument(
        "--t",
        "--tables",
        type=str,
        required=True,
        nargs="+",
        help=("Tablas a convertir en tipos. " "Puede ser solo el nombre de la tabla, o <nombre-tabla>:<nombre-tipo>"),
    )
    parser.add_argument("--db", type=str, required=True, help="Nombre de la BDD")
    parser.add_argument("--u", "--user", type=str, default="root:", help="Usuario de la BDD: <user>:<pass>")
    parser.add_argument("--p", "--port", type=str, default="3306", help="Port de la BDD")
    parser.add_argument("--f", "--file", type=str, default="tipos_bdd.py", help="Nombre de la BDD")
    parser.add_argument(
        "--r",
        "--replace",
        action="store_const",
        const=True,
        default=False,
        help="Añade al archivo en vez de hacer append",
    )

    args = parser.parse_args()
    db = DatabaseConnection(args.db, args.u, port=args.p)

    type_file = Path(args.f)
    if type_file.is_file() and args.r:
        with open(type_file, "w", encoding="utf-8") as f:
            f.write(("from datetime import datetime\n" "from chlib.base_types import ID, BaseEntity\n"))

    with db.get_conn() as conn:
        with open(type_file, "a", encoding="utf-8") as f:
            for table in args.t:
                if ":" in table:
                    tt = table.split(":")
                    tdict = parse_table_columns(conn, args.db, tt[0], tt[1])
                else:
                    tdict = parse_table_columns(conn, args.db, table, table)
                if tdict != "":
                    f.write("\n\n")
                    f.write(tdict)
