-- Laboratorio de un nodo. SimpleStrategy RF=1 NO es para produccion.
CREATE KEYSPACE IF NOT EXISTS campuscloud_eventos
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

CREATE TABLE IF NOT EXISTS campuscloud_eventos.eventos_por_estudiante (
    estudiante_id text,
    periodo text,
    fecha_evento timestamp,
    evento_id uuid,
    servicio_id int,
    tipo_evento text,
    detalle text,
    origen text,
    PRIMARY KEY ((estudiante_id, periodo), fecha_evento, evento_id)
) WITH CLUSTERING ORDER BY (fecha_evento DESC, evento_id ASC);

-- Particion: estudiante + mes, evitando particiones enormes con el tiempo.
-- Clustering: fecha descendente y UUID para distinguir eventos simultaneos.
DESCRIBE KEYSPACE campuscloud_eventos;
