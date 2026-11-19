-- Consulta principal: actividad de un estudiante durante un periodo.
-- Ambas partes de la particion aparecen con igualdad y el rango usa clustering.
SELECT estudiante_id, fecha_evento, tipo_evento, detalle, servicio_id
FROM campuscloud_eventos.eventos_por_estudiante
WHERE estudiante_id = 'EST-001'
  AND periodo = '2026-11'
  AND fecha_evento >= '2026-11-08T00:00:00Z'
  AND fecha_evento < '2026-11-12T00:00:00Z';

-- Otro estudiante, misma ventana mensual.
SELECT fecha_evento, tipo_evento, detalle
FROM campuscloud_eventos.eventos_por_estudiante
WHERE estudiante_id = 'EST-002' AND periodo = '2026-11';

-- Prueba de lectura puntual por clave completa.
SELECT *
FROM campuscloud_eventos.eventos_por_estudiante
WHERE estudiante_id = 'EST-001'
  AND periodo = '2026-11'
  AND fecha_evento = '2026-11-10T10:00:00Z'
  AND evento_id = 11111111-1111-4111-8111-111111111104;
