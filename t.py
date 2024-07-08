from datetime import datetime
from chlib.base_types import ID, BaseEntity


class Gen_cometido(BaseEntity):
    """Diccionario tipado generado para la tabla gen_cometido."""

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


class Area(BaseEntity):
    """Diccionario tipado generado para la tabla area."""

    path_id: str
    parent_area_id: ID | None
    created_by: ID | None
    created_at: datetime
    id_ref: int | None
