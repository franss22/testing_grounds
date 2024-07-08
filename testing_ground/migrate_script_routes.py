"""Migra las rutas de scripts que fueron pasadas a modulos pip."""

from chlib.DatabaseConnection import DatabaseConnection as DB
from chlib.chutil import loadConfigFile

new_routes: list[tuple[str, str]] = [
    ("io_capture.py", "-m sheets_bi_lib.io_capture"),
    ("MapObservatoryManager.py", "-m sheets_bi_lib.MapObservatoryManager"),
    ("ObservatoryManager.py", "-m sheets_bi_lib.ObservatoryManager"),
    ("SheetsCube.py", "-m sheets_bi_lib.SheetsCube"),
    ("SheetsCubeStaging.py", "-m sheets_bi_lib.SheetsCubeStaging"),
    ("SheetsTransformations.py", "-m sheets_bi_lib.SheetsTransformations"),
    ("automatic_cubes_other.py", "-m sheets_bi_scripts.automatic_cubes_other"),
    ("automatic_cubes.py", "-m sheets_bi_scripts.automatic_cubes"),
    ("execute_cube.py", "-m sheets_bi_scripts.execute_cube"),
    ("manual_execution_staging.py", "-m sheets_bi_scripts.manual_execution_staging"),
    ("manual_execution.py", "-m sheets_bi_scripts.manual_execution"),
    ("bpmsfunctions.py", "-m bpmshub_lib.bpmsfunctions"),
    ("callbacks.py", "-m bpmshub_lib.callbacks"),
    ("load_process_file.py", "-m bpmshub_lib.load_process_file"),
    ("process_instance.py", "-m bpmshub_lib.process_instance"),
    ("update_process.py", "-m bpmshub_lib.update_process"),
    ("complete_process_instance.py", "-m bpmshub_scripts.complete_process_instance"),
    ("load_process.py", "-m bpmshub_scripts.load_process"),
    ("new_process_instance.py", "-m bpmshub_scripts.new_process_instance"),
    ("update_process_file.py", "-m bpmshub_scripts.update_process_file"),
    ("DocumentGenerator.py", "-m gestor_documental_lib.DocumentGenerator"),
    ("SheetApiConnection.py", "-m gestor_documental_lib.SheetApiConnection"),
    ("create_document_from_template.py", "-m gestor_documental_scripts.create_document_from_template"),
    ("EntityManager.py", "-m template_lib.EntityManager"),
    ("template_entity.py", "-m template_lib.template_entity"),
    ("TemplateEntityType.py", "-m template_lib.TemplateEntityType"),
    ("clone_template_entity.py", "-m template_scripts.clone_template_entity"),
    ("create_template_entity.py", "-m template_scripts.create_template_entity"),
    ("form_clone.py", "-m template_scripts.form_clone"),
    ("update_entity_template_by_entity_type.py", "-m template_scripts.update_entity_template_by_entity_type"),
    ("update_template.py", "-m template_scripts.update_template"),
]


def migrate_script_routes(conf: dict[str, str | None] | None = None) -> None:
    """Migra las rutas de scripts que fueron pasadas a modulos pip."""
    conf = loadConfigFile() if conf is None else conf
    db = DB.fromConf(conf)
    conn = db.get_conn()
    for old_route, new_route in new_routes:
        print(f"- Migrando ruta de {old_route} a {new_route}")
        query = f"UPDATE script SET name = '{new_route}' WHERE name LIKE '%{old_route}'"
        conn.execute(query)

    print("Rutas de scripts migradas.")


if __name__ == "__main__":
    migrate_script_routes()
