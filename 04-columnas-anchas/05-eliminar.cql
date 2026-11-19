-- Antes: evento de prueba, por clave primaria completa.
SELECT *
FROM campuscloud_eventos.eventos_por_estudiante
WHERE estudiante_id = 'EST-003' AND periodo = '2026-11'
AND fecha_evento = '2026-11-13T08:20:00Z'
AND evento_id = 33333333-3333-4333-8333-333333333304;

DELETE FROM campuscloud_eventos.eventos_por_estudiante
WHERE estudiante_id = 'EST-003' AND periodo = '2026-11'
AND fecha_evento = '2026-11-13T08:20:00Z'
AND evento_id = 33333333-3333-4333-8333-333333333304;

-- Despues: debe aparecer (0 rows) para esa clave.
SELECT *
FROM campuscloud_eventos.eventos_por_estudiante
WHERE estudiante_id = 'EST-003' AND periodo = '2026-11'
AND fecha_evento = '2026-11-13T08:20:00Z'
AND evento_id = 33333333-3333-4333-8333-333333333304;
