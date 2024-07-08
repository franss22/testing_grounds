"""Tipos generados de la base de datos mlc11."""
from typing import Any, TypedDict
from datetime import datetime
from chlib.base_types import ID, BaseEntity


class Area(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `area`."""

    path_id: str
    parent_area_id: ID | None
    created_by: ID | None
    created_at: datetime
    id_ref: int | None


class AreaHierarchy(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `area_hierarchy`."""

    child_id: ID
    created_by: ID | None


class AreaRole(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `area_role`."""

    role_id: ID | None
    created_at: datetime | None
    created_by: ID | None


class AreaRoleView(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `area_role_view`."""

    created_at: datetime | None


class AvailableColumns(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `available_columns`."""

    table_name: str
    column_name: str
    created_by: Any | None  # binary(0)


class AvailableDataSource(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `available_data_source`."""

    order: int | None


class AvailableTables(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `available_tables`."""

    created_by: Any | None  # binary(0)


class BiDimComuna(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `bi_dim_comuna`."""

    value: str | None
    order: int | None
    created_by: ID | None


class BiDimProvincia(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `bi_dim_provincia`."""

    value: str | None
    order: int | None
    created_by: ID | None


class BiDimRegion(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `bi_dim_region`."""

    value: str | None
    iso: str | None
    order: int | None
    created_by: ID | None


class Bucket(TypedDict):
    """Diccionario tipado generado para la tabla `bucket`."""

    id: ID
    name: str | None
    is_public: int | None
    area_id: ID | None
    role_id: ID | None
    owner_id: ID | None
    valid: int


class Calculation(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `calculation`."""

    created_by: ID | None


class Column(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `column`."""

    column_group_id: ID | None
    entity_type_id: ID | None
    column_parent_id: ID | None
    alias: str | None
    col_name: str | None
    format: str | None
    entity_type_fk: str | None
    entity_type_permission_fk: ID | None
    col_name_fk: str | None
    pivot_table: str | None
    entity_type_pivot_fk: ID | None
    default_value: str | None
    col_fk_1_n: str | None
    col_fk_n_1: str | None
    col_fk_filter: str | None
    col_filter_by: str | None
    options: str | None
    order: int
    create_form_order: int | None
    show_in_create_form: int | None
    show_in_edit_form: int | None
    required_in_create_form: int | None
    visible: int
    calculated: int
    created_by: ID | None
    width: int | None
    filter: str | None
    orderby: str | None
    orderby_order: int | None
    front_filter: int | None
    front_filter_default: str | None
    created_at: datetime
    color_dimmed: str | None
    text_color_dimmed: str | None
    is_metric: int | None
    is_dimention: int | None
    row_disaggregation_parent_column_id: ID | None
    description: str | None


class ColumnArea(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `column_area`."""

    role_id: ID | None
    column_id: ID | None
    created_by: ID | None


class ColumnFormat(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `column_format`."""

    created_by: ID | None


class ColumnGenerator(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `column_generator`."""

    entity_type_id: ID | None
    format: str | None
    order: int
    created_at: datetime
    alter_code: str | None
    created_by: ID | None


class ColumnGroup(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `column_group`."""

    show_in_interface: int | None
    order: int | None
    created_by: ID | None


class ColumnRole(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `column_role`."""

    role_id: ID | None
    column_id: ID | None
    created_by: ID | None


class ColumnValidator(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `column_validator`."""

    column_validator_type_id: ID | None
    entity_type_id: ID | None
    restrict_when_invalid: int | None
    block_when_invalid: int | None
    validate_edited_columns_only: int | None
    global_execution: str | None
    filter_row_sql: str | None
    message: str | None
    value1_multiplier: Any | None  # double
    value1_type: str | None
    value1: str | None
    operator: str | None
    value2_multiplier: Any | None  # double
    value2_type: str | None
    value2: str | None
    created_by: ID | None
    created_at: datetime | None


class ColumnValidatorCache(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `column_validator_cache`."""

    created_by: ID | None
    created_at: datetime | None
    entity_type_id: ID
    column_validator_id: ID
    message: str | None
    row_id: ID | None
    global_execution: str | None
    block_when_invalid: int | None


class ColumnValidatorHasColumn(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `column_validator_has_column`."""

    column_validator_id: ID | None
    column_id: ID | None


class ColumnValidatorType(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `column_validator_type`."""

    data_type: str | None
    created_by: ID | None
    created_at: datetime | None


class ColumnWithFormId(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `column_with_form_id`."""

    column_group_id: ID | None
    entity_type_id: ID | None
    alias: str | None
    col_name: str | None
    format: str | None
    entity_type_fk: str | None
    entity_type_permission_fk: ID | None
    col_name_fk: str | None
    pivot_table: str | None
    entity_type_pivot_fk: ID | None
    default_value: str | None
    col_fk_1_n: str | None
    col_fk_n_1: str | None
    col_fk_filter: str | None
    col_filter_by: str | None
    options: str | None
    order: int
    create_form_order: int | None
    show_in_create_form: int | None
    show_in_edit_form: int | None
    required_in_create_form: int | None
    visible: int
    calculated: int
    created_by: ID | None
    width: int | None
    filter: str | None
    orderby: str | None
    orderby_order: int | None
    front_filter: int | None
    front_filter_default: str | None
    created_at: datetime
    is_metric: int | None
    is_dimention: int | None
    form_id: ID | None


class Comment(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `comment`."""

    text: str | None
    email: str | None
    user_name: str | None
    visible: str | None
    section_id: ID | None
    created_by: ID | None


class CommentSource(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `comment_source`."""

    text: str | None
    visible: int | None
    source_id: ID | None
    created_by: ID | None


class Component(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `component`."""

    process_id: ID
    component_type_id: ID
    form_id: ID | None
    lane_id: ID
    is_end_event: int | None
    is_cancel_event: int | None
    is_start_event: int | None
    is_intermediate_event: int | None
    is_exclusive_gateway: int | None
    is_paralel_gateway: int | None
    is_task: int | None
    is_service_task: int | None
    text_annotation: str | None
    ref: str | None
    created_by: ID | None


class ComponentInstance(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `component_instance`."""

    process_instance_id: ID
    component_id: ID
    lane_id: ID
    form_id: ID | None
    is_active: int | None
    completed_at: datetime | None
    created_at: datetime | None
    canceled_at: datetime | None
    completed_by_user_id: ID | None
    asigned_to_user_id: ID | None
    action_id: ID | None
    completed_form_id: ID | None
    created_by_component_instance_id: ID | None
    process_id: ID
    role_id: ID | None
    entity_type_id: ID
    entity_id: ID | None
    created_by: ID | None


class ComponentType(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `component_type`."""

    created_by: ID | None


class Dimension(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `dimension`."""

    name_staging: str | None
    table: str | None
    is_staging: int
    format: str | None
    filter_type: str | None
    created_by: ID | None
    source_db: int
    parent_dimension_id: ID | None
    child_dimension_id: ID | None


class DimensionFormat(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `dimension_format`."""

    created_by: ID | None


class DimensionWithMetric(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `dimension_with_metric`."""

    metric_id: ID | None
    column_name: str | None
    name_staging: str | None
    table: str | None
    is_staging: int
    format: str | None
    filter_type: str | None
    created_by: ID | None
    source_db: int


class Document(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `document`."""

    unique_hash: str | None
    bucket_id: ID | None
    entity_id: ID | None
    created_at: datetime | None
    src: str | None
    old_src: str | None
    is_s3: int | None
    version: int | None
    extension: str | None
    size: int | None
    metadata: str | None
    created_by: ID | None
    src_s3: str | None
    gen_mlc11_observacion: str | None
    gen_mlc11_validado: int | None
    gen_mlc11_es_documentacion: int | None
    is_gcloud: int | None


class EnabledMetric(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `enabled_metric`."""

    metric: ID | None
    ano: int | None
    lower_limit: Any | None  # double
    upper_limit: Any | None  # double
    key_enero: str | None
    key_febrero: str | None
    key_marzo: str | None
    key_abril: str | None
    key_mayo: str | None
    key_junio: str | None
    key_julio: str | None
    key_agosto: str | None
    key_septiembre: str | None
    key_octubre: str | None
    key_noviembre: str | None
    key_diciembre: str | None
    enero: Any | None  # char(50)
    febrero: Any | None  # char(50)
    marzo: Any | None  # char(50)
    abril: Any | None  # char(50)
    mayo: Any | None  # char(50)
    junio: Any | None  # char(50)
    julio: Any | None  # char(50)
    agosto: Any | None  # char(50)
    septiembre: Any | None  # char(50)
    octubre: Any | None  # char(50)
    noviembre: Any | None  # char(50)
    diciembre: Any | None  # char(50)
    created_by: ID | None


class Entity(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `entity`."""

    table_name: str
    created_by: ID | None
    created_at: datetime
    updated_at: datetime | None


class EntityGenerator(TypedDict):
    """Diccionario tipado generado para la tabla `entity_generator`."""

    id: ID
    name: str | None
    entity_type_id: ID | None
    origen_datos: ID | None
    file_id: str | None
    status: int | None
    created_at: datetime
    text_color: str | None
    area_id: ID | None
    owner_id: ID | None
    created_by: ID | None
    valid: int
    replace: ID
    message: str | None


class EntityHasArea(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `entity_has_area`."""

    entity_id: ID | None
    created_by: ID | None


class EntityType(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `entity_type`."""

    table_name: str | None
    entity_name: str | None
    image: str | None
    show_in_interface: int | None
    order: int | None
    limit: int | None
    area_read_all_permission: int | None
    area_update_all_permission: int | None
    iframe_url: str | None
    iframe_width: int | None
    iframe_height: int | None
    group_name: str | None
    on_create: ID | None
    on_update: ID | None
    on_bulk: ID | None
    on_alternative_bulk: ID | None
    created_by: ID | None
    create_form_id: ID | None
    update_form_id: ID | None
    subgroup_name: str | None
    template_id: ID | None
    source_db: int | None
    btn_download: str | None
    btn_import: str | None
    btn_headers: str | None
    btn_refresh: str | None
    btn_create: str | None
    search_bar: int | None
    sql_cache: int | None


class EntityTypeHasComponent(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `entity_type_has_component`."""

    order: int | None
    entity_type_id: ID | None
    sh_component_type_id: ID | None
    config_entity_id: ID | None
    slots_id: ID | None
    custom_styles: str | None
    config_param_1: str | None


class EntityTypeHasFixedColumn(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `entity_type_has_fixed_column`."""

    order: int | None
    entity_type_id: ID | None
    column_id: ID | None


class EntityTypePermission(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `entity_type_permission`."""

    entity_type_id: ID | None
    role_id: ID | None
    created_at: datetime | None
    show_in_interface: int
    read: int
    create: int | None
    update: int | None
    delete: int | None
    created_by: ID | None


class EntityTypeRowDrillDown(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `entity_type_row_drill_down`."""

    json: str | None
    created_by: ID | None
    entity_type_id: ID | None


class FailedJobs(TypedDict):
    """Diccionario tipado generado para la tabla `failed_jobs`."""

    id: int
    connection: str
    queue: str
    payload: str
    exception: str
    failed_at: Any  # timestamp


class Flow(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `flow`."""

    process_id: ID
    from_component_id: ID
    to_component_id: ID
    condition: str | None
    default: int | None
    action_id: ID | None
    created_by: ID | None


class Form(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `form`."""

    entity_type_id: ID | None
    created_at: datetime | None
    on_create: str | None
    on_update: str | None
    type: str
    is_step: int | None
    custom_messages: str | None


class FormAction(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `form_action`."""

    process_id: ID | None
    save_form: int | None
    refresh_form: int | None
    cancel_form: int | None
    close_form: int | None
    cancel_process: int | None
    created_by: ID | None


class FormAlternative(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `form_alternative`."""

    to_string: str | None
    form_field_id: ID | None
    next_form_section: ID | None
    order: int | None


class FormAlternativeHasProducts(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `form_alternative_has_products`."""

    alternative_id: ID | None
    form_field_id: ID | None
    entity_type_id: ID | None
    entity_id: ID | None
    ammount: int
    created_by: ID | None


class FormClone(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `form_clone`."""

    created_by: ID | None
    created_at: datetime | None
    form_id: ID | None
    form: ID | None


class FormCloneElement(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `form_clone_element`."""

    form_id: ID | None
    element_id: ID | None
    created_by: ID | None


class FormField(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `form_field`."""

    form_id: ID | None
    column_id: ID | None
    permission: int | None
    order: int | None
    form_section_id: ID | None
    col_md: int
    col_xl: int
    col_sm: int
    required: int | None
    format: str | None
    link_url: str | None
    link_name: str | None
    description: str | None
    show_by_field_id: ID | None
    show_by_field_value: str | None
    assign_default_value: int | None
    metadata: str | None


class FormHasAction(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `form_has_action`."""

    form_id: ID | None
    action_id: ID | None
    created_by: ID | None


class FormInstance(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `form_instance`."""

    form_id: ID
    entity_id: ID
    interactions: str | None
    interactions_json: str | None
    created_at: datetime | None


class FormProducts(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `form_products`."""

    table_name: str | None
    created_by: ID | None
    created_at: datetime | None
    updated_at: datetime | None
    form_id: ID | None


class FormRow(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `form_row`."""

    order: int | None
    height: int | None
    form_id: ID | None
    identificador: str | None


class FormSection(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `form_section`."""

    order: int | None
    form_id: ID | None
    form_row_id: ID | None
    group_name: str | None
    col_md: int
    col_xl: int
    col_sm: int
    visible_on_load: int
    default_next_form_section: ID | None
    description: str | None
    image_id: ID | None
    show_by_field_id: ID | None
    show_by_field_value: str | None
    identificador: str | None


class GenActualizarTemplate(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_actualizar_template`."""

    created_by: ID | None
    created_at: datetime | None
    sh_template_id: ID | None


class GenAntecedentes(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_antecedentes`."""

    created_by: ID | None
    created_at: datetime | None
    declaracion_jurada_simple_de_inhabilidades_e_: ID | None
    certificado_de_estudios: ID | None
    declaracion_jurada_simple_de_inhabilidades_e__v1: ID | None
    autorizacion_retiro_certificado_antecedentes_: ID | None
    certificado_de_nacimiento: ID | None
    fotocopia_cedula_de_identidad: ID | None
    curriculum_vitae: ID | None
    revision_de_antecedentes_fk: ID | None
    revision_de_certificados_fk: ID | None


class GenAntecedentesrevisionDeAntecedentesFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_antecedentesrevision_de_antecedentes_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenAntecedentesrevisionDeCertificadosFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_antecedentesrevision_de_certificados_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenAsignacion(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_asignacion`."""

    created_by: ID | None
    created_at: datetime | None
    codigo: str | None


class GenAsignacionInterna(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_asignacion_interna`."""

    created_by: ID | None
    created_at: datetime | None
    codigo: str | None
    asignacion: ID | None


class GenAumentarRentaDeCometido(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_aumentar_renta_de_cometido`."""

    created_by: ID | None
    created_at: datetime | None
    fecha_termino: datetime | None
    cometido_especifico: str | None
    valor_hora: int | None
    fecha_cambio: datetime | None
    observaciones: str | None
    valor_periodo: int | None
    cometido_generico: str | None
    horas_semanales: int | None
    fecha_inicio: datetime | None
    id_fk: ID | None
    renta_mensual: int | None
    nivel: int | None
    aumento: int | None


class GenAumentarRentaDeCometidoIdFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_aumentar_renta_de_cometido_id_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenBandejaAprobacionEImputacion(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_bandeja_aprobacion_e_imputacion`."""

    created_by: ID | None
    created_at: datetime | None


class GenCometido(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_cometido`."""

    created_by: ID | None
    created_at: datetime | None
    fecha_inicio: datetime | None
    horas_semanales: float | None
    numero_taller: int | None
    fecha_cambio: datetime | None
    valor_periodo_imp: int | None
    renta_mensual: int | None
    observaciones: str | None
    cometido_especifico: str | None
    vigencia_imp: str | None
    cometido_generico: str | None
    cometido_reemplazado: ID | None
    fecha_termino: datetime | None
    valor_mensual_imp: int | None
    nivel: int | None
    cambio: int | None
    valor_hora: int | None
    valor_periodo: int | None
    estado_cometido: ID | None
    solicitud: ID | None
    gen_solicitud_id: ID | None
    sh_entidad_1n_default_id: ID | None
    cometido_especifico_fk: ID | None
    cometido_generico_fk: ID | None
    nivel_v1: ID | None
    nivel_v2: int | None
    gen_copia_solicitudes_id: ID | None
    valor_periodo_liquido: int | None
    nuevo_termino: datetime | None
    nuevas_horas: int | None
    gen_prueba_solicitudes_nuevas_id: ID | None
    gen_nuevo_inicio: datetime | None
    gen_nuevo_termino: datetime | None
    gen_nuevas_horas: int | None
    gen_nuevo_valor_hora: int | None
    gen_nueva_renta_mensual: float | None
    gen_nuevo_valor_periodo: float | None
    gen_nuevo_valor_periodo_liquido: float | None
    gen_solicitud_id_v1: ID | None
    nuevo_numero_taller: int | None
    gen_observaciones: str | None
    gen_nueva_fecha_de_cambio: datetime | None
    gen_nuevo_numero_de_taller: int | None
    gen_nuevo_nivel: int | None
    gen_valor_cambio: float | None
    gen_nivel_anterior: int | None
    gen_fecha_inicio_anterior: datetime | None
    gen_fecha_termino_anterior: datetime | None
    gen_horas_semanales_anterior: int | None
    gen_numero_talleres_anterior: int | None
    gen_valor_hora_anterior: int | None
    gen_renta_mensual_anterior: float | None
    gen_valor_periodo_anterior: float | None
    gen_valor_periodo_liquido_anterior: float | None
    gen_valor_disminucion: float | None
    gen_solicitud_id_v2: ID | None
    esantiguo: int | None
    unidad_de_origen: ID | None
    fecha_inicio_imputacion: datetime | None
    fecha_inicio_contrato: datetime | None
    eliminar: int | None
    valor_aumento: int | None
    gen_solicitud_id_v3: ID | None
    gen_solicitud_id_v4: ID | None
    gen_solicitud_id_v5: ID | None
    gen_solicitud_id_v6: ID | None


class GenCometidosAnteriores(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_cometidos_anteriores`."""

    created_by: ID | None
    created_at: datetime | None
    fecha_inicio: datetime | None
    horas_semanales: float | None
    numero_taller: int | None
    fecha_cambio: datetime | None
    renta_mensual: int | None
    solicitud: ID | None
    observaciones: str | None
    defecto_n_a_1_fk: ID | None
    cometido_especifico: ID | None
    cometido_generico: ID | None
    cometido_reemplazado: ID | None
    fecha_termino: datetime | None
    nivel: int | None
    valor_disminucion: int | None
    valor_periodo_anterior: int | None
    valor_periodo_liquido_anterior: int | None
    valor_hora_anterior: int | None
    renta_mensual_anterior: int | None
    nivel_anterior: int | None
    numero_talleres_anterior: int | None
    horas_semanales_anterior: int | None
    fecha_termino_anterior: datetime | None
    fecha_inicio_anterior: datetime | None
    eliminar: int | None
    valor_periodo_liquido: int | None
    valor_hora: int | None
    valor_cambio: int | None
    valor_periodo: int | None
    estado_cometido: ID | None
    gen_solicitud_id: ID | None
    sh_entidad_1n_default_id: ID | None


class GenCometidosAnterioresDefectoNA1Fk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_cometidos_anteriores_defecto_n_a_1_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenCometidosEspecificos(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_cometidos_especificos`."""

    created_by: ID | None
    created_at: datetime | None
    nombre_cometido1: str | None
    nombre_cometido2_fk: ID | None
    nivel_fk: ID | None
    activo: int | None


class GenCometidosEspecificosnivelFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_cometidos_especificosnivel_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenCometidosEspecificosnombreCometido2Fk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_cometidos_especificosnombre_cometido2_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenCometidosVigentes(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_cometidos_vigentes`."""

    created_by: ID | None
    created_at: datetime | None
    fecha_inicio: datetime | None
    fecha_termino: datetime | None
    valor_hora: int | None
    cometido_generico: str | None
    valor_periodo: int | None
    observaciones: str | None
    horas_semanales: int | None
    id_v1: int | None
    renta_mensual: int | None
    cometido_especifico: str | None
    nivel: str | None
    nivel_fk: ID | None


class GenCometidosVigentesnivelFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_cometidos_vigentesnivel_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenCometidoCometidoEspecificoFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_cometido_cometido_especifico_fk`."""

    created_by: ID | None
    created_at: datetime | None
    cometido_generico: ID | None


class GenCometidoCometidoGenericoFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_cometido_cometido_generico_fk`."""

    created_by: ID | None
    created_at: datetime | None
    id_cometido_generico: int | None


class GenComunas(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_comunas`."""

    created_by: ID | None
    created_at: datetime | None
    region_fk: ID | None


class GenComunasRegionFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_comunas_region_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenContrato(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_contrato`."""

    created_by: ID | None
    created_at: datetime | None
    documento_contrato_firmado: ID | None
    suma_horas_semanales: float | None
    honorario: ID | None
    fecha_expiracion: datetime | None
    documento_contrato: ID | None
    fecha_emision: datetime | None
    tipo_contrato: ID | None
    solicitudes: ID | None
    estado_contrato: ID | None
    contrato_reemplazado: ID | None
    documento: ID | None
    plantilla_fk: ID | None
    gen_solicitud_id: ID | None


class GenContratoPlantillaFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_contrato_plantilla_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenCopiaSolicitudes(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_copia_solicitudes`."""

    created_by: ID | None
    created_at: datetime | None
    usuario_director_fk: ID | None
    imputar: int | None
    usuario_jefe_de_contrato_fk: ID | None
    honorario: ID | None
    contrato: ID | None
    subprograma: ID | None
    estado_solicitud: str | None
    programa_contrato: ID | None
    documento: ID | None
    plantilla_fk: ID | None
    nombres: ID | None
    fecha_revision_director: datetime | None
    rut: ID | None
    apellido: ID | None
    observacion_jefe_contratos: str | None
    fecha_revision_contratos: datetime | None
    observacion_director: str | None
    observacion_confirmacion: str | None
    usuario: ID | None
    _status: str | None


class GenCopiaSolicitudesPlantillaFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_copia_solicitudes_plantilla_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenCopiaSolicitudesUsuarioDirectorFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_copia_solicitudes_usuario_director_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenCopiaSolicitudesUsuarioJefeDeContrat(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_copia_solicitudes_usuario_jefe_de_contrat`."""

    created_by: ID | None
    created_at: datetime | None


class GenDenunciasGeneradas(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_denuncias_generadas`."""

    created_by: ID | None
    created_at: datetime | None
    ley: str | None
    regente: str | None


class GenDepartamento(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_departamento`."""

    created_by: ID | None
    created_at: datetime | None
    departamento: str | None


class GenDisminuirRentaDeCometido(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_disminuir_renta_de_cometido`."""

    created_by: ID | None
    created_at: datetime | None
    renta_mensual: int | None
    horas_semanales: int | None
    disminucion: int | None
    nivel: int | None
    observaciones: str | None
    cometido_generico: str | None
    valor_hora: int | None
    id_fk: ID | None
    fecha_inicio: datetime | None
    fecha_termino: datetime | None
    cometido_especifico: str | None
    fecha_cambio: datetime | None
    valor_periodo: int | None


class GenDisminuirRentaDeCometidoIdFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_disminuir_renta_de_cometido_id_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenEjecucionManualScripts(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_ejecucion_manual_scripts`."""

    created_by: ID | None
    created_at: datetime | None
    id_entidad: str | None
    tipo_entidad_fk: ID | None
    script_fk: ID | None
    parametros: str | None


class GenEntidadPrueba1(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_entidad_prueba_1`."""

    created_by: ID | None
    created_at: datetime | None


class GenEstados(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_estados`."""

    created_by: ID | None
    created_at: datetime | None
    estado: str | None


class GenEstadoAntecedentes(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_estado_antecedentes`."""

    created_by: ID | None
    created_at: datetime | None


class GenEstadoCivil(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_estado_civil`."""

    created_by: ID | None
    created_at: datetime | None


class GenEstadoCometido(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_estado_cometido`."""

    created_by: ID | None
    created_at: datetime | None


class GenEstadoContrato(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_estado_contrato`."""

    created_by: ID | None
    created_at: datetime | None


class GenEstadoInformeDeSolicitud(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_estado_informe_de_solicitud`."""

    created_by: ID | None
    created_at: datetime | None


class GenEstadoRenuncia(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_estado_renuncia`."""

    created_by: ID | None
    created_at: datetime | None


class GenEstadoSolicitud(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_estado_solicitud`."""

    created_by: ID | None
    created_at: datetime | None


class GenFiscalizacion(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_fiscalizacion`."""

    created_by: ID | None
    created_at: datetime | None
    denuncias_generadas_fk: ID | None
    local: str | None


class GenFiscalizacion2(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_fiscalizacion_2`."""

    created_by: ID | None
    created_at: datetime | None
    local: str | None
    denuncia_generada_2_fk: ID | None


class GenFiscalizacion2DenunciaGenerada2Fk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_fiscalizacion_2_denuncia_generada_2_fk`."""

    created_by: ID | None
    created_at: datetime | None
    gen_fiscalizacion_2_id: ID | None
    ley: str | None


class GenFiscalizacionDenunciasGeneradasFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_fiscalizacion_denuncias_generadas_fk`."""

    created_by: ID | None
    created_at: datetime | None
    gen_fiscalizacion_id: ID | None
    regente: str | None


class GenHonorario(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_honorario`."""

    created_by: ID | None
    created_at: datetime | None
    nivel_educacional: ID | None
    carnet_de_identidad: ID | None
    declaracion_jurada_simple_inhabilidades: ID | None
    rut: str | None
    usuario: ID | None
    certificado_de_nacimiento: ID | None
    profesion: ID | None
    estado_antecedentes: ID | None
    curriculum: ID | None
    certificado_de_estudios: ID | None
    sexo_fk: ID | None
    apellidos: str | None
    estado_certificado_antecedentes: ID | None
    correo: str | None
    autorizacion_antecedentes_srcei: ID | None
    otra_profesion_fk: ID | None
    nacionalidad_fk: ID | None
    direccion: str | None
    fecha_de_nacimiento: datetime | None
    telefono: int | None
    banco: str | None
    numero_de_cuenta: str | None
    correo_v1: str | None
    tipo_de_cuenta: str | None
    codigo_porfa_de_pago: str | None
    codigo_banco: str | None
    apellido_materno: str | None
    apellido_materno_v1: str | None
    comuna: ID | None
    numero: str | None
    calle: str | None
    region: ID | None
    detalle: str | None
    calle_v1: str | None
    detalle_v1: str | None
    numero_v1: str | None
    region_v1: ID | None
    comuna_v1: ID | None
    codigo_forma_pago: str | None
    codigo_forma_pago_v1: str | None
    estado_civil: ID | None
    estado_civil_v1: ID | None
    estado_civil_v2: ID | None
    estado_honorario: str | None


class GenHonorarioNacionalidadFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_honorario_nacionalidad_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenHonorarioOtraProfesionFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_honorario_otra_profesion_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenHonorarioSexoFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_honorario_sexo_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenImputacion(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_imputacion`."""

    created_by: ID | None
    created_at: datetime | None
    valor: float | None
    archivo: ID | None
    fecha_emision: datetime | None
    codigo: str | None
    solicitud: ID | None
    asignacion_interna: ID | None


class GenInformeimputacion(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_informeimputacion`."""

    created_by: ID | None
    created_at: datetime | None
    n_informe: str | None
    _status: str | None
    documento_informe: ID | None
    fecha_de_aprobacion: datetime | None
    documento_aprobacion: ID | None
    fecha_de_aprobacion_v1: datetime | None


class GenInformeSolicitud(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_informe_solicitud`."""

    created_by: ID | None
    created_at: datetime | None
    solicitud: ID | None
    informe_de_solicitud: ID | None
    fecha_solicitud: datetime | None
    usuario_jefe_contrato: ID | None
    estado_informe_solicitud: ID | None
    observacion: str | None
    numero_informe: str | None
    total_solicitud: int | None
    informe_de_solicitud_firmado: ID | None


class GenNiveles(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_niveles`."""

    created_by: ID | None
    created_at: datetime | None


class GenNivelEducacional(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_nivel_educacional`."""

    created_by: ID | None
    created_at: datetime | None


class GenNominaDeHonorarios(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_nomina_de_honorarios`."""

    created_by: ID | None
    created_at: datetime | None
    profesion: str | None
    sexo: str | None
    otra_profesion: str | None
    apellidos: str | None
    nivel_educacional_fk: ID | None
    nombres: str | None
    correo: str | None
    rut: str | None
    rut_v1: str | None
    antecedentes_fk: ID | None
    estado_antecedentes_fk: ID | None
    estado_certificado_de_antecedentes_fk: ID | None
    antecedente_formulario: ID | None


class GenNominaDeHonorariosantecedentesFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_nomina_de_honorariosantecedentes_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenNominaDeHonorariosestadoAntecedentesF(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_nomina_de_honorariosestado_antecedentes_f`."""

    created_by: ID | None
    created_at: datetime | None


class GenNominaDeHonorariosestadoCertificadoDe(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_nomina_de_honorariosestado_certificado_de`."""

    created_by: ID | None
    created_at: datetime | None


class GenNominaDeHonorariosnivelEducacionalFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_nomina_de_honorariosnivel_educacional_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenNominaTarjeta(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_nomina_tarjeta`."""

    created_by: ID | None
    created_at: datetime | None
    caso: str | None


class GenNominaVecinos(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_nomina_vecinos`."""

    created_by: ID | None
    created_at: datetime | None
    local: str | None
    nomina_tarjeta_fk: ID | None


class GenNominaVecinosNominaTarjetaFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_nomina_vecinos_nomina_tarjeta_fk`."""

    created_by: ID | None
    created_at: datetime | None
    gen_nomina_vecinos_id: ID | None


class GenNuevosCometidos(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_nuevos_cometidos`."""

    created_by: ID | None
    created_at: datetime | None
    renta_mensual: int | None
    fecha_termino: datetime | None
    cometido_especifico_fk: ID | None
    valor_hora: int | None
    cometido_generico: str | None
    horas_semanales: int | None
    nivel: str | None
    observaciones: str | None
    valor_periodo: int | None
    fecha_inicio: datetime | None


class GenNuevosCometidosCometidoEspecificoFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_nuevos_cometidos_cometido_especifico_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenPlantillasDeDocumentos(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_plantillas_de_documentos`."""

    created_by: ID | None
    created_at: datetime | None
    cuerpo: str | None
    entidad_fk: ID | None


class GenPlantillasDeDocumentosEntidadFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_plantillas_de_documentos_entidad_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenProfesion(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_profesion`."""

    created_by: ID | None
    created_at: datetime | None


class GenPrograma(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_programa`."""

    created_by: ID | None
    created_at: datetime | None
    programa: str | None


class GenProgramaContrato(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_programa_contrato`."""

    created_by: ID | None
    created_at: datetime | None
    programa_contrato: str | None


class GenPruebaHonorarios(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_prueba_honorarios`."""

    created_by: ID | None
    created_at: datetime | None
    usuario_fk: ID | None
    profesion: ID | None
    profesion_fk: ID | None
    curriculum: ID | None
    correo: str | None
    estado_antecedentes: ID | None
    estado_antecedentes_v1: ID | None
    estado_antecedentes_v2: ID | None
    estado_antecedentes_v3: ID | None
    estado_antecedentes_v4: ID | None
    estado_antecedentes_v5: ID | None
    estado_antecedentes_v6: ID | None
    estado_antecedentes_v7: ID | None
    estado_antecedentes_v8: ID | None
    estado_antecedentes_v9: ID | None
    estado_antecedentes_v10: ID | None
    estado_antecedentes_v11: ID | None
    estado_antecedentes_fk: ID | None
    autorizacion_antecedentes_srcei: ID | None
    certificado_de_nacimiento: ID | None
    rut: str | None
    estado_certificado_antecedentes_fk: ID | None
    carnet_de_identidad: ID | None
    nombres: str | None
    declaracion_jurada_simple_inhabilidades: ID | None
    sexo_fk: ID | None
    nivel_educacional: ID | None
    certificado_de_estudios: ID | None
    apellidos: str | None


class GenPruebaHonorarios2(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_prueba_honorarios_2`."""

    created_by: ID | None
    created_at: datetime | None
    autorizacion_antecedentes_srcei: ID | None
    rut: str | None
    curriculum: ID | None
    sexo_fk: ID | None
    certificado_de_estudios: ID | None
    apellidos: str | None
    estado_certificado_antecedentes_fk: ID | None
    nivel_educacional: ID | None
    nombres: str | None
    carnet_de_identidad: ID | None
    estado_antecedentes: ID | None
    usuario_fk: ID | None
    correo: str | None
    profesion_fk: ID | None
    certificado_de_nacimiento: ID | None
    declaracion_jurada_simple_inhabilidades: ID | None


class GenPruebaHonorarios2EstadoCertificadoAn(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_prueba_honorarios_2_estado_certificado_an`."""

    created_by: ID | None
    created_at: datetime | None


class GenPruebaHonorarios2ProfesionFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_prueba_honorarios_2_profesion_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenPruebaHonorarios2SexoFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_prueba_honorarios_2_sexo_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenPruebaHonorarios2UsuarioFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_prueba_honorarios_2_usuario_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenPruebaHonorariosEstadoAntecedentesFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_prueba_honorarios_estado_antecedentes_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenPruebaHonorariosEstadoCertificadoAnte(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_prueba_honorarios_estado_certificado_ante`."""

    created_by: ID | None
    created_at: datetime | None


class GenPruebaHonorariosProfesionFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_prueba_honorarios_profesion_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenPruebaHonorariosSexoFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_prueba_honorarios_sexo_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenPruebaHonorariosUsuarioFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_prueba_honorarios_usuario_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenPruebaNuevaTablaDeCometidos(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_prueba_nueva_tabla_de_cometidos`."""

    created_by: ID | None
    created_at: datetime | None
    fecha_inicio: datetime | None
    horas_semanales: float | None
    numero_taller: int | None
    fecha_cambio: datetime | None
    valor_periodo_imp: int | None
    renta_mensual: int | None
    solicitud: ID | None
    observaciones: str | None
    prueba_solicitudes_nuevas: ID | None
    defecto_n_a_1_fk: ID | None
    cometido_especifico: ID | None
    vigencia_imp: str | None
    cometido_generico: ID | None
    nuevo_termino: datetime | None
    cometido_reemplazado: ID | None
    fecha_termino: datetime | None
    valor_mensual_imp: int | None
    nivel: int | None
    cambio: int | None
    valor_periodo_liquido: int | None
    valor_hora: int | None
    valor_periodo: int | None
    nuevas_horas: int | None
    estado_cometido: ID | None
    copia_solicitudes: ID | None
    gen_prueba_solicitudes_nuevas_id: ID | None
    sh_entidad_1n_default_id: ID | None


class GenPruebaNuevaTablaDeCometidosDefectoN(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_prueba_nueva_tabla_de_cometidos_defecto_n`."""

    created_by: ID | None
    created_at: datetime | None


class GenPruebaNuevaTablaDeCometidosV1(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_prueba_nueva_tabla_de_cometidos_v1`."""

    created_by: ID | None
    created_at: datetime | None
    fecha_inicio: datetime | None
    horas_semanales: float | None
    numero_taller: int | None
    fecha_cambio: datetime | None
    valor_periodo_imp: int | None
    renta_mensual: int | None
    solicitud: ID | None
    observaciones: str | None
    prueba_solicitudes_nuevas: ID | None
    defecto_n_a_1_fk: ID | None
    cometido_especifico: ID | None
    vigencia_imp: str | None
    cometido_generico: ID | None
    nuevo_termino: datetime | None
    cometido_reemplazado: ID | None
    fecha_termino: datetime | None
    valor_mensual_imp: int | None
    nivel: int | None
    cambio: int | None
    valor_periodo_liquido: int | None
    valor_hora: int | None
    valor_periodo: int | None
    nuevas_horas: int | None
    estado_cometido: ID | None
    copia_solicitudes: ID | None
    gen_prueba_solicitudes_nuevas_id: ID | None
    sh_entidad_1n_default_id: ID | None


class GenPruebaNuevaTablaDeCometidosV1Defect(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_prueba_nueva_tabla_de_cometidos_v1_defect`."""

    created_by: ID | None
    created_at: datetime | None


class GenPruebaScriptDecision(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_prueba_script_decision`."""

    created_by: ID | None
    created_at: datetime | None
    texto_prueba: str | None
    _status: str | None


class GenPruebaSolicitudesNuevas(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_prueba_solicitudes_nuevas`."""

    created_by: ID | None
    created_at: datetime | None
    monto_liquido_solicitud: int | None
    usuario_director_fk: ID | None
    imputar: int | None
    usuario_jefe_de_contrato_fk: ID | None
    honorario: ID | None
    contrato: ID | None
    subprograma: ID | None
    estado_solicitud: str | None
    programa_contrato: ID | None
    documento: ID | None
    plantilla_fk: ID | None
    nombres: ID | None
    fecha_revision_director: datetime | None
    rut: ID | None
    apellido: ID | None
    observacion_jefe_contratos: str | None
    fecha_revision_contratos: datetime | None
    observacion_director: str | None
    observacion_confirmacion: str | None
    monto_bruto_solicitud: int | None
    usuario: ID | None
    modificacion: str | None
    monto_bruto_modificacion: int | None
    monto_liquido_odificacion: int | None


class GenPruebaSolicitudesNuevasPlantillaFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_prueba_solicitudes_nuevas_plantilla_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenPruebaSolicitudesNuevasUsuarioDirecto(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_prueba_solicitudes_nuevas_usuario_directo`."""

    created_by: ID | None
    created_at: datetime | None


class GenPruebaSolicitudesNuevasUsuarioJefeDe(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_prueba_solicitudes_nuevas_usuario_jefe_de`."""

    created_by: ID | None
    created_at: datetime | None


class GenRegiones(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_regiones`."""

    created_by: ID | None
    created_at: datetime | None


class GenRenovarCometido(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_renovar_cometido`."""

    created_by: ID | None
    created_at: datetime | None
    cometido_generico: str | None
    disminucion: int | None
    observaciones: str | None
    valor_periodo: int | None
    fecha_termino: datetime | None
    horas_semanales: int | None
    cometido_especifico: str | None
    fecha_inicio: datetime | None
    nivel: str | None
    valor_hora: int | None
    id_fk: ID | None
    renta_mensual: int | None


class GenRenovarCometidoIdFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_renovar_cometido_id_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenRenovarCometidoV1(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_renovar_cometido_v1`."""

    created_by: ID | None
    created_at: datetime | None
    observaciones: str | None
    cometido_especifico: str | None
    cometido_generico: str | None
    fecha_inicio: datetime | None
    nivel: int | None
    fecha_termino: datetime | None
    id_fk: ID | None
    renta_mensual: int | None
    horas_semanales: int | None
    aumento: int | None
    valor_periodo: int | None
    valor_hora: int | None


class GenRenovarCometidoV1IdFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_renovar_cometido_v1_id_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenRetencion(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_retencion`."""

    created_by: ID | None
    created_at: datetime | None
    retencion: float | None


class GenSolicitud(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_solicitud`."""

    created_by: ID | None
    created_at: datetime | None
    usuario_director: ID | None
    usuario_jefe_de_contrato: ID | None
    subprograma: ID | None
    programa_contrato: ID | None
    honorario: ID | None
    fecha_revision_director: datetime | None
    observacion_jefe_contratos: str | None
    fecha_revision_contratos: datetime | None
    observacion_director: str | None
    estado_solicitud: ID | None
    observacion_confirmacion: str | None
    usuario: ID | None
    honorario_v1: ID | None
    contrato: ID | None
    _status: str | None
    generated_document: str | None
    gen_plantilla: str | None
    imputar: int | None
    blocked: int
    gen_informeimputacion_id: ID | None
    sh_entidad_1n_default_id: ID | None
    monto_liquido_solicitud: int | None
    monto_bruto_solicitud: int | None
    numero_imputacion: str | None
    monto_modificacion_liquido: int | None
    monto_modificacion_bruto: int | None
    id_solicitud_anterior: str | None
    tabla_pago_meses: str | None
    texto_bruto: str | None
    texto_liquido: str | None
    decreto_multiple_fk: ID | None
    tipo_de_solicitud: ID | None
    tipo_de_solicitud_v1: ID | None
    tabla_pago_meses_v1: str | None
    apellido_materno: ID | None
    numero_certificado_imputacion: str | None
    fecha_aprobacion: datetime | None
    rut: str | None
    apellido_paterno: str | None
    apellido_materno_v1: str | None
    nombres: str | None
    contador: int | None
    sexo: ID | None
    sexo_v1: ID | None
    gen_informeimputacion_id_v1: ID | None
    fecha_aprobacion_v1: datetime | None


class GenSolicitudDecretoMultipleFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_solicitud_decreto_multiple_fk`."""

    created_by: ID | None
    created_at: datetime | None
    gen_solicitud_id: ID | None


class GenSolicitudDeContratos(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_solicitud_de_contratos`."""

    created_by: ID | None
    created_at: datetime | None
    departamento_fk: ID | None
    nombre: str | None
    tipo_de_contrato_fk: ID | None
    programa_fk: ID | None
    subprograma_fk: ID | None
    programa_contrato_fk: ID | None
    datos_del_contrato: str | None
    programa_fk_v1: ID | None
    profesion: str | None
    grado_academico: int | None
    rut: str | None
    nombre_v1: int | None
    nombre_fk: ID | None
    grado_academico_v1: str | None
    contrato_vigente: ID | None
    nombre_v2: str | None
    decreto_vigente: ID | None
    observaciones: str | None
    rut_v1: str | None
    motivo: str | None
    fecha_de_renuncia: datetime | None


class GenSolicitudDeContratosdepartamentoFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_solicitud_de_contratosdepartamento_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenSolicitudDeContratosnombreFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_solicitud_de_contratosnombre_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenSolicitudDeContratosprogramaContratoF(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_solicitud_de_contratosprograma_contrato_f`."""

    created_by: ID | None
    created_at: datetime | None


class GenSolicitudDeContratosprogramaFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_solicitud_de_contratosprograma_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenSolicitudDeContratosprogramaFkV1(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_solicitud_de_contratosprograma_fk_v1`."""

    created_by: ID | None
    created_at: datetime | None


class GenSolicitudDeContratossubprogramaFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_solicitud_de_contratossubprograma_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenSolicitudDeContratostipoDeContratoFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_solicitud_de_contratostipo_de_contrato_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenSolicitudRenuncia(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_solicitud_renuncia`."""

    created_by: ID | None
    created_at: datetime | None
    fecha_renuncia: datetime | None
    solicitante: ID | None
    decreto_fk: ID | None
    honorario: ID | None
    estado_renuncia: ID | None
    documento: ID | None
    observacion: str | None
    contrato: ID | None


class GenSolicitudRenunciaDecretoFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_solicitud_renuncia_decreto_fk`."""

    created_by: ID | None
    created_at: datetime | None
    documento_firmado: ID | None
    fecha_emision: datetime | None
    codigo: str | None
    documento: ID | None
    imputacion: ID | None
    contrato: ID | None
    plantilla_fk: ID | None
    documento_v1: ID | None
    solicitud_fk: ID | None
    gen_informe_de_imputacion: str | None


class GenSolicitudRenunciaDecretoFkPlantillaF(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_solicitud_renuncia_decreto_fk_plantilla_f`."""

    created_by: ID | None
    created_at: datetime | None


class GenSolicitudRenunciaDecretoFkSolicitudF(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_solicitud_renuncia_decreto_fk_solicitud_f`."""

    created_by: ID | None
    created_at: datetime | None


class GenSubprograma(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_subprograma`."""

    created_by: ID | None
    created_at: datetime | None
    programa_fk: ID | None


class GenSubprogramaProgramaFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_subprograma_programa_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenTablaContratoMeses(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_tabla_contrato_meses`."""

    created_by: ID | None
    created_at: datetime | None
    liquido: int | None
    bruto: int | None
    solicitud: ID | None
    mes: str | None


class GenTest2DenunciaConOpciones(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_2_denuncia_con_opciones`."""

    created_by: ID | None
    created_at: datetime | None
    caso: str | None
    gen_test_2_solicitud_con_opciones_id: ID | None


class GenTest2SolicitudConOpciones(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_2_solicitud_con_opciones`."""

    created_by: ID | None
    created_at: datetime | None


class GenTest3DenunciaConTablaIntermedia(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_3_denuncia_con_tabla_intermedia`."""

    created_by: ID | None
    created_at: datetime | None
    caso: str | None


class GenTest3SolicitudConTablaIntermedia(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_3_solicitud_con_tabla_intermedia`."""

    created_by: ID | None
    created_at: datetime | None
    denuncia_fk: ID | None


class GenTest3SolicitudConTablaIntermediaDen(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_3_solicitud_con_tabla_intermedia_den`."""

    created_by: ID | None
    created_at: datetime | None
    gen_test_3_solicitud_con_tabla_intermedia_id: ID | None


class GenTest4SolicitudConTablaIntermediaSol(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_4_solicitud_con_tabla_intermedia_sol`."""

    created_by: ID | None
    created_at: datetime | None
    test4denuncias_fk: ID | None


class GenTest4SolicitudConTablaIntermediaSolV1(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_4_solicitud_con_tabla_intermedia_sol_v1`."""

    created_by: ID | None
    created_at: datetime | None
    gen_test_4_solicitud_con_tabla_intermedia_sol_id: ID | None


class GenTestBpm(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_bpm`."""

    created_by: ID | None
    created_at: datetime | None
    observaciones: str | None


class GenTestBpms10(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_bpms_10`."""

    created_by: ID | None
    created_at: datetime | None
    taller: str | None
    _status: str | None


class GenTestBpms11(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_bpms_11`."""

    created_by: ID | None
    created_at: datetime | None
    taller: str | None


class GenTestBpms12(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_bpms_12`."""

    created_by: ID | None
    created_at: datetime | None
    taller: str | None
    _status: str | None


class GenTestBpms13(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_bpms_13`."""

    created_by: ID | None
    created_at: datetime | None
    taller: str | None
    _status: str | None


class GenTestBpms14(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_bpms_14`."""

    created_by: ID | None
    created_at: datetime | None
    taller: str | None
    _status: str | None


class GenTestBpms17(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_bpms_17`."""

    created_by: ID | None
    created_at: datetime | None
    departamento: str | None
    apellido: str | None
    taller: str | None
    nivel: int | None
    paso_1: ID | None


class GenTestBpms18(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_bpms_18`."""

    created_by: ID | None
    created_at: datetime | None
    taller: str | None
    _status: str | None


class GenTestBpms19(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_bpms_19`."""

    created_by: ID | None
    created_at: datetime | None
    cas: str | None
    _status: str | None


class GenTestBpms2(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_bpms_2`."""

    created_by: ID | None
    created_at: datetime | None
    observaciones: str | None
    _status: str | None


class GenTestBpms20(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_bpms_20`."""

    created_by: ID | None
    created_at: datetime | None
    caso: str | None
    _status: str | None


class GenTestBpms22(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_bpms_22`."""

    created_by: ID | None
    created_at: datetime | None
    caso: str | None
    _status: str | None


class GenTestBpms23(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_bpms_23`."""

    created_by: ID | None
    created_at: datetime | None
    caso: str | None
    _status: str | None


class GenTestBpms3Simple(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_bpms_3_simple`."""

    created_by: ID | None
    created_at: datetime | None
    cometido_especifico: str | None
    cometido_generico: str | None


class GenTestBpms4(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_bpms_4`."""

    created_by: ID | None
    created_at: datetime | None
    cometido_especifico: str | None
    cometido_generico: str | None
    _status: str | None
    estado: str | None


class GenTestBpms5(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_bpms_5`."""

    created_by: ID | None
    created_at: datetime | None
    cometido_especifico: str | None
    cometido_generico: str | None
    _status: str | None


class GenTestBpms7(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_bpms_7`."""

    created_by: ID | None
    created_at: datetime | None
    cometido_especifico: str | None
    cometido_generico: str | None
    _status: str | None


class GenTestBpms8(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_bpms_8`."""

    created_by: ID | None
    created_at: datetime | None
    taller: str | None
    _status: str | None


class GenTestBpms9(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_bpms_9`."""

    created_by: ID | None
    created_at: datetime | None
    taller: str | None


class GenTestBpmsModificaciones(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_bpms_modificaciones`."""

    created_by: ID | None
    created_at: datetime | None
    caso: str | None
    _status: str | None


class GenTestDenuncia(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_denuncia`."""

    created_by: ID | None
    created_at: datetime | None
    id_v1: int | None
    caso: str | None
    gen_test_solicitud_1_id: ID | None


class GenTestDocumentos(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_documentos`."""

    created_by: ID | None
    created_at: datetime | None
    plantilla_fk: ID | None
    nombre_persona: str | None
    documento: ID | None


class GenTestDocumentos2(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_documentos_2`."""

    created_by: ID | None
    created_at: datetime | None
    nivel_educacional: ID | None
    otros_niveles_educacionales_fk: ID | None
    documento: ID | None
    plantilla: ID | None


class GenTestDocumentos2OtrosNivelesEducacion(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_documentos_2_otros_niveles_educacion`."""

    created_by: ID | None
    created_at: datetime | None


class GenTestDocumentosPlantillaFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_documentos_plantilla_fk`."""

    created_by: ID | None
    created_at: datetime | None


class GenTestSolicitud1(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_solicitud_1`."""

    created_by: ID | None
    created_at: datetime | None
    id_v1: int | None


class GenTestSolicitud2(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_solicitud_2`."""

    created_by: ID | None
    created_at: datetime | None
    id_v1: int | None
    denuncias_fk: ID | None


class GenTestSolicitud2DenunciasFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_solicitud_2_denuncias_fk`."""

    created_by: ID | None
    created_at: datetime | None
    gen_test_solicitud_2_id: ID | None


class GenTestTodoEn1(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_todo_en_1`."""

    created_by: ID | None
    created_at: datetime | None
    dueno: str | None
    resultados_test_todo_en_1_fk: ID | None
    local: str | None
    resultados: ID | None
    informe_resultados: str | None


class GenTestTodoEn1ResultadosTestTodoEn1(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_test_todo_en_1_resultados_test_todo_en_1_`."""

    created_by: ID | None
    created_at: datetime | None
    gen_test_todo_en_1_id: ID | None


class GenTipoContrato(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_tipo_contrato`."""

    created_by: ID | None
    created_at: datetime | None


class GenTipoDeContrato(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_tipo_de_contrato`."""

    created_by: ID | None
    created_at: datetime | None
    tipo_de_contrato: str | None


class GenTipoDocumento(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_tipo_documento`."""

    created_by: ID | None
    created_at: datetime | None


class GenTipoSolicitud(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_tipo_solicitud`."""

    created_by: ID | None
    created_at: datetime | None


class GenUnidadDeOrigen(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_unidad_de_origen`."""

    created_by: ID | None
    created_at: datetime | None


class GenValorHora(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gen_valor_hora`."""

    created_by: ID | None
    created_at: datetime | None
    porcentaje: float | None
    valor_hora: int | None
    ano: int | None
    valor_mensual: int | None
    horas_semanales: float | None
    nivel: int | None


class GptHonorarioOtraProfesionFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gpt_honorario_otra_profesion_fk`."""

    honorario_id: ID
    honorario_otra_profesion_fk_id: ID
    created_by: ID | None
    created_at: datetime | None


class GptNominaDeHonorariosEstadoAntecedentes(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gpt_nomina_de_honorarios_estado_antecedentes_`."""

    nomina_de_honorarios_id: ID
    nomina_de_honorariosestado_antecedentes_f_id: ID
    created_by: ID | None
    created_at: datetime | None


class GptNominaDeHonorariosEstadoCertificadoD(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gpt_nomina_de_honorarios_estado_certificado_d`."""

    nomina_de_honorarios_id: ID
    nomina_de_honorariosestado_certificado_de_id: ID
    created_by: ID | None
    created_at: datetime | None


class GptNuevosCometidosCometidoEspecificoFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gpt_nuevos_cometidos_cometido_especifico_fk`."""

    nuevos_cometidos_id: ID
    nuevos_cometidos_cometido_especifico_fk_id: ID
    created_by: ID | None
    created_at: datetime | None


class GptSolicitudId(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gpt_solicitud_id`."""

    solicitud_id: ID
    sh_entidad_1n_default_id: ID | None
    created_by: ID | None
    created_at: datetime | None


class GptSolicitudIdV1(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gpt_solicitud_id_v1`."""

    solicitud_id: ID
    sh_entidad_1n_default_id: ID | None
    created_by: ID | None
    created_at: datetime | None


class GptSolicitudRenunciaDecretoFkId(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gpt_solicitud_renuncia_decreto_fk_id`."""

    solicitud_renuncia_decreto_fk_id: ID
    sh_entidad_1n_default_id: ID | None
    created_by: ID | None
    created_at: datetime | None


class GptTestDocumentos2OtrosNivelesEducacion(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `gpt_test_documentos_2_otros_niveles_educacion`."""

    test_documentos_2_id: ID
    test_documentos_2_otros_niveles_educacion_id: ID
    created_by: ID | None
    created_at: datetime | None


class Jobs(TypedDict):
    """Diccionario tipado generado para la tabla `jobs`."""

    id: int
    queue: str
    payload: str
    attempts: int
    reserved_at: int | None
    available_at: int
    created_at: int


class Lane(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `lane`."""

    process_id: ID
    role_id: ID | None
    variable_type: str | None
    created_by: ID | None


class Language(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `language`."""

    created_by: ID | None


class Map(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `map`."""

    created_by: ID | None
    has_show_this_zone: int
    has_draw_toolbar: int | None
    column_latitude: str | None
    column_longitude: str | None
    created_at: datetime | None
    entity_type_id: ID | None
    medium_cluster_size_starts_at: int | None
    large_cluster_size_starts_at: int | None
    search_component: str | None
    search_component_config: str | None
    latitud: float | None
    longitud: float | None
    zoom: int
    show_legend: int | None


class MapHasLayerType(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `map_has_layer_type`."""

    created_by: ID | None
    map_id: ID | None
    map_layer_type_id: ID | None
    gen_group: str | None
    gen_subgroup: str | None
    group_selection_limit: int | None
    gen_order: int | None
    layer_url: str | None
    image: ID | None
    point_image: ID | None
    gen_metric: str | None
    calculation_id: ID | None
    gen_geoserver_layer: str | None
    bi_url: str | None
    geojson_col_reference: str | None
    dimension_col_reference: str | None
    property_keys: str | None
    is_default: int | None
    entity_type_id: ID | None
    custom_styles: str | None
    interval_delay_seconds: int | None
    gen_clustering_zoom: int | None
    filter_layers: str | None
    quick_layer: int | None
    classification_column: ID | None
    source_icon_classification: ID | None
    column_icon: ID | None


class MapLayerType(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `map_layer_type`."""

    created_by: ID | None
    type: str | None
    created_at: datetime | None
    gen_source: str | None
    gen_url: str | None
    gen_code: str | None


class MesesNEsp(TypedDict):
    """Diccionario tipado generado para la tabla `meses_n_esp`."""

    name: str
    number: int


class Metric(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `metric`."""

    short_name: str | None
    description: str | None
    format: str | None
    table: str | None
    is_staging: int | None
    column_format: int | None
    column: str | None
    date_dim: str | None
    tags_id: ID | None
    created_by: ID | None
    source_db: int | None
    measure_id: ID | None
    numerator_id: ID | None
    calculation_id: ID | None
    proceso: str | None
    etl_path: str | None
    capitulo_fk: ID | None
    metric_filter: str | None


class MetriccapituloFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `metriccapitulo_fk`."""

    created_by: ID | None


class MetricExcludeSection(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `metric_exclude_section`."""

    section_id: ID
    metric_id: ID | None
    created_by: ID | None


class MetricFormat(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `metric_format`."""

    created_by: ID | None


class MetricHasDimension(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `metric_has_dimension`."""

    dimension_id: ID
    metric_id: ID | None
    column_name: str | None
    created_by: ID | None


class MetricHasDimensionFilter(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `metric_has_dimension_filter`."""

    metric_id: ID | None
    created_by: ID | None
    dimension_id: ID | None
    dimension_value_id: int | None


class MetricHasSource(TypedDict):
    """Diccionario tipado generado para la tabla `metric_has_source`."""

    metric_id: ID | None
    source_id: ID | None
    id: ID


class MetricMonthValue(TypedDict):
    """Diccionario tipado generado para la tabla `metric_month_value`."""

    periodo: int
    metric_id: ID
    value: Any  # double
    name: str | None
    color: str | None
    text_color: str | None
    area_id: ID | None
    owner_id: ID | None
    created_by: ID | None
    valid: int


class MetricWithView(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `metric_with_view`."""

    view_id: ID | None
    short_name: str | None
    description: str | None
    format: str | None
    table: str | None
    is_staging: int | None
    column_format: int | None
    column: str | None
    date_dim: str | None
    tags_id: ID | None
    created_by: ID | None
    source_db: int | None
    measure_id: ID | None
    calculation_id: ID | None
    proceso: str | None
    etl_path: str | None
    capitulo_fk: ID | None


class Migrations(TypedDict):
    """Diccionario tipado generado para la tabla `migrations`."""

    id: int
    migration: str
    batch: int


class OauthAccessTokens(TypedDict):
    """Diccionario tipado generado para la tabla `oauth_access_tokens`."""

    id: str
    user_id: ID | None
    client_id: ID
    name: str | None
    scopes: str | None
    revoked: int
    created_at: Any | None  # timestamp
    updated_at: Any | None  # timestamp
    expires_at: datetime | None


class OauthAuthCodes(TypedDict):
    """Diccionario tipado generado para la tabla `oauth_auth_codes`."""

    id: str
    user_id: int
    client_id: ID
    scopes: str | None
    revoked: int
    expires_at: datetime | None


class OauthClients(TypedDict):
    """Diccionario tipado generado para la tabla `oauth_clients`."""

    id: ID
    user_id: int | None
    name: str
    secret: str | None
    provider: str | None
    redirect: str
    personal_access_client: int
    password_client: int
    revoked: int
    created_at: Any | None  # timestamp
    updated_at: Any | None  # timestamp


class OauthPersonalAccessClients(TypedDict):
    """Diccionario tipado generado para la tabla `oauth_personal_access_clients`."""

    id: int
    client_id: ID
    created_at: Any | None  # timestamp
    updated_at: Any | None  # timestamp


class OauthRefreshTokens(TypedDict):
    """Diccionario tipado generado para la tabla `oauth_refresh_tokens`."""

    id: str
    access_token_id: str
    revoked: int
    expires_at: datetime | None


class PasswordResets(TypedDict):
    """Diccionario tipado generado para la tabla `password_resets`."""

    email: str
    token: str
    created_at: Any | None  # timestamp


class Process(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `process`."""

    entity_type_id: ID | None
    ficha_form_id: ID | None
    created_by: ID | None


class ProcessInstance(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `process_instance`."""

    initiated_by_user_id: ID
    process_id: ID
    created_at: datetime | None
    canceled_at: datetime | None
    entity_type_id: ID
    canceled_by_user_id: ID | None
    ficha_form_id: ID | None
    finished_at: datetime | None
    last_action_at: datetime | None
    last_action: ID | None
    process_status: str | None
    entity_id: ID | None
    created_by: ID | None


class Replace(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `replace`."""

    created_by: ID | None


class Role(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `role`."""

    parent_role_id: ID | None
    path_id: str
    created_at: datetime
    id_ref: int | None
    created_by: ID | None


class RoleHierarchy(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `role_hierarchy`."""

    child_id: ID
    role_id: ID | None
    created_by: ID | None


class Script(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `script`."""

    language_id: ID | None
    created_by: ID | None


class Section(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `section`."""

    view_id: ID | None
    nav_bar_name: str | None
    description: str | None
    visible: str | None
    is_header: int | None
    layout_id: ID | None
    layout_param: str | None
    order: str | None
    created_by: ID | None
    dimention_id: ID | None
    data_source: str | None
    visualization_id: ID | None
    filter_last_period: int
    filters_single_period: int | None
    default_filters: str | None


class SectionHasAgregation(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `section_has_agregation`."""

    dimension_id: ID | None
    section_has_visualization_id: ID
    created_by: Any | None  # binary(0)
    order: int


class SectionHasDescription(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `section_has_description`."""

    metric_id: ID | None
    section_id: ID | None
    created_by: ID | None


class SectionHasDimensionDescription(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `section_has_dimension_description`."""

    metric_id: ID | None
    section_id: ID | None
    dimension_id: ID | None
    dimension_value: ID | None
    description: str | None
    created_by: ID | None


class SectionHasFilters(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `section_has_filters`."""

    dimension_id: ID
    section_id: ID | None
    type: str | None
    created_by: ID | None


class SectionHasVisualization(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `section_has_visualization`."""

    order: int | None
    visualization_id: ID | None
    section_id: ID | None
    calculation_id: ID | None
    first_aggregation_id: ID | None
    second_aggregation_id: ID | None
    metric_order: str
    created_by: ID | None
    width: int | None
    has_period_sub_filter: int | None
    calc_over_total: int | None
    has_drill_down_first_dim: int | None


class SheetsBiDimensionAssociatedToFormField(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `sheets_bi_dimension_associated_to_form_field`."""

    dimension_id: ID | None
    column_id: ID | None
    created_by: ID | None


class SheetsBiDimensionCalculatedFromColumn(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `sheets_bi_dimension_calculated_from_column`."""

    dimension_id: ID | None
    column_id: ID | None
    created_by: ID | None
    dim_generated_from_column: int
    dictionary_table: ID | None
    transformation_table: ID | None
    original_table: ID | None
    updates_dimension: int | None


class SheetsBiMetricCalculatedFromColumn(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `sheets_bi_metric_calculated_from_column`."""

    metric_id: ID | None
    column_id: ID | None
    created_by: ID | None
    calculation_id: ID | None


class SheetsTemplateClone(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `sheets_template_clone`."""

    created_by: ID | None
    created_at: datetime | None
    tipo_de_clonacion_fk: ID | None
    template_a_clonar_fk: ID | None


class SheetsTemplateCloneTipoDeClonacionFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `sheets_template_clone_tipo_de_clonacion_fk`."""

    created_by: ID | None
    created_at: datetime | None


class SheetsTemplateColumn(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `sheets_template_column`."""

    created_by: ID | None
    created_at: datetime | None
    sheets_template_entity_type_id: ID | None
    column_id: ID | None
    sheets_template_column_format_id: ID | None
    sheets_template_opciones_id: ID | None
    sheets_template_tabla_id: ID | None
    order: int
    row: str | None
    section: str | None
    tamao_fk: ID | None
    requerido: int | None
    descripcion_del_campo: str | None
    url: str | None
    url_nombre: str | None
    es_dimension: int | None
    es_metrica: int | None
    es_filtro_fk: ID | None
    alternativas: str | None


class SheetsTemplateColumntamaoFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `sheets_template_columntamao_fk`."""

    created_by: ID | None


class SheetsTemplateColumnFiltroFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `sheets_template_column_filtro_fk`."""

    created_by: ID | None


class SheetsTemplateColumnFormat(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `sheets_template_column_format`."""

    mapeo: str | None
    es_1a1: int
    es_1an: int
    es_na1: int
    es_nan: int
    type: str | None
    created_by: ID | None
    created_at: datetime | None


class SheetsTemplateDeletedColumn(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `sheets_template_deleted_column`."""

    template_entity_type_id: ID | None
    column_id: ID | None
    column_name: str | None
    column_type: str | None
    template_column_format_id: ID | None
    created_by: ID | None
    order: int


class SheetsTemplateEntityType(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `sheets_template_entity_type`."""

    group_name: str | None
    subgroup_name: str | None
    create_form: ID | None
    entity_type: ID | None
    created_by: ID | None
    created_at: datetime | None
    is_main: int
    url_formulairo: str | None
    tipo_de_mapa_fk: ID | None
    tipo_de_bi_fk: ID | None
    vista_fk: ID | None
    formulario_de_filtros_fk: ID | None
    mapa_fk: ID | None


class SheetsTemplateEntityTypeTipoDeBiFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `sheets_template_entity_type_tipo_de_bi_fk`."""

    created_by: ID | None


class SheetsTemplateEntityTypeTipoDeMapaFk(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `sheets_template_entity_type_tipo_de_mapa_fk`."""

    created_by: ID | None


class SheetsTemplatePermission(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `sheets_template_permission`."""

    sheets_template_entity_type_id: ID | None
    role_id: ID | None
    created_at: datetime | None
    show_in_interface: int
    read: int
    create: int | None
    update: int | None
    delete: int | None
    created_by: ID | None


class ShComponentType(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `sh_component_type`."""

    code: str | None
    endpoint_config: str | None
    endpoint_data: str | None
    require_all_data: int | None
    entity_type_id: ID | None


class ShEntidad1nDefault(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `sh_entidad_1n_default`."""

    created_by: ID | None


class ShEntityLog(TypedDict):
    """Diccionario tipado generado para la tabla `sh_entity_log`."""

    id: ID
    id_entity: ID | None
    id_entity_type: ID | None
    action: str | None
    action_date: datetime | None
    action_responsible: ID | None
    valid: int | None
    details: str | None


class ShHome(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `sh_home`."""

    text_middle: str | None
    text_footer: str | None
    bg_img: ID | None
    created_by: ID | None


class ShNavbar(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `sh_navbar`."""

    content: str | None
    created_by: ID | None


class ShPage(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `sh_page`."""

    sub_title: str | None
    html: str | None
    form_id: ID | None
    form_height: int | None
    bg_img: ID | None
    created_by: ID | None
    wp_post_id: int | None


class Slots(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `slots`."""

    template_id: ID | None
    code: str | None


class Source(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `source`."""

    description: str | None
    format: str | None
    downloads: int | None
    visits: int | None
    table: str | None
    author: str | None
    size: str | None
    source_type_id: ID | None
    publication_date: datetime | None
    created_by: ID | None
    visible: int
    order: int | None


class SourceHasDocument(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `source_has_document`."""

    source_id: ID | None
    document_id: ID | None
    created_by: ID | None


class SourceType(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `source_type`."""

    created_by: ID | None
    background_id: ID | None


class Tag(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `tag`."""

    created_by: ID | None


class Template(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `template`."""

    code: str | None
    custom_styles: str | None
    wp_post_id: int | None


class TransbankOrders(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `transbank_orders`."""

    order_id: str
    transbank_payment_id: str | None
    amount: Any  # decimal(65,2)
    created_by: str | None
    created_at: datetime | None
    updated_at: datetime | None
    on_checkout: ID | None


class TransbankPayments(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `transbank_payments`."""

    created_by: str | None
    vci: str | None
    buy_order: str
    session_id: str
    amount: Any  # decimal(17,0)
    status: str | None
    card_detail: str | None
    authorization_code: str | None
    payment_type_code: str | None
    response_code: int | None
    installments_number: int | None
    accounting_date: str | None
    transaction_date: datetime | None
    created_at: datetime | None
    updated_at: datetime | None


class User(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `user`."""

    email: str
    password: str | None
    is_admin: int
    created_at: datetime
    area_main: ID | None
    created_by: ID | None
    id_ref: int | None
    request_new_pass: int | None


class UserRole(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `user_role`."""

    user_id: ID | None
    role_id: ID | None
    created_at: datetime
    created_by: ID | None
    area_id_role: ID | None


class View(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `view`."""

    icon: ID | None
    image: ID | None
    default_metric: ID | None
    visible: int | None
    order: int | None
    description: str | None
    created_by: ID | None


class ViewHasMetrics(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `view_has_metrics`."""

    metric_id: ID | None
    view_id: ID | None
    calculation_id: ID
    created_by: ID | None
    order: int


class ViewTablaContratoMeses2(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `view_tabla_contrato_meses_2`."""

    solicitud_id: ID
    month_number: int
    month_name: str
    total_bruto: Any | None  # decimal(37,0)
    total_liquido: Any | None  # double(17,0)
    created_by: Any | None  # binary(0)
    created_at: Any | None  # binary(0)
    sh_entidad_1n_default_id: str


class ViewTablaDecreto(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `view_tabla_decreto`."""

    person_rut: str | None
    cometido_especifico: str
    fecha_contrato: str | None
    vigencia: str | None
    valor_periodo: int | None
    informe_imputacion_n: str | None
    created_by: Any | None  # binary(0)
    created_at: Any | None  # binary(0)
    sh_entidad_1n_default_id: str
    decreto_id: ID


class Visualization(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `visualization`."""

    type: str | None
    created_by: ID | None


class WpPosts(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `wp_posts`."""

    post_author: int
    post_date: datetime | None
    post_date_gmt: datetime | None
    post_content: str
    post_title: str
    post_excerpt: str
    post_status: str
    comment_status: str
    ping_status: str
    post_password: str
    post_name: str
    to_ping: str
    pinged: str
    post_modified: datetime | None
    post_modified_gmt: datetime | None
    post_content_filtered: str
    post_parent: int
    guid: str
    menu_order: int
    post_type: str
    post_mime_type: str
    comment_count: int
    compile_to_template: int | None
    created_by: ID | None


class WpPostsCache(TypedDict):
    """Diccionario tipado generado para la tabla `wp_posts_cache`."""

    id: int
    post_title: str
    post_modified: datetime
    html: str | None


class WpPostsHasEntityType(BaseEntity):
    """Diccionario tipado generado para la tabla entidad `wp_posts_has_entity_type`."""

    wp_post_id: int | None
    entity_type_id: ID | None
    created_by: ID | None
