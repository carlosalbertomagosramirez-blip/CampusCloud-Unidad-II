-- Antes: revisar registro especifico.
SELECT detalle
FROM campuscloud_eventos.eventos_por_estudiante
WHERE estudiante_id = 'EST-001' AND periodo = '2026-11'
AND fecha_evento = '2026-11-10T10:00:00Z'
AND evento_id = 11111111-1111-4111-8111-111111111104;

-- Actualizacion por la clave primaria COMPLETA (evita crear otra fila).
UPDATE campuscloud_eventos.eventos_por_estudiante
SET detalle = 'Ingreso al laboratorio verificado'
WHERE estudiante_id = 'EST-001' AND periodo = '2026-11'
AND fecha_evento = '2026-11-10T10:00:00Z'
AND evento_id = 11111111-1111-4111-8111-111111111104;

-- Despues: confirmar valor.
SELECT detalle
FROM campuscloud_eventos.eventos_por_estudiante
WHERE estudiante_id = 'EST-001' AND periodo = '2026-11'
AND fecha_evento = '2026-11-10T10:00:00Z'
AND evento_id = 11111111-1111-4111-8111-111111111104;
