-- Ejecutar ANTES y DESPUES de reiniciar el contenedor.
SELECT fecha_evento, tipo_evento, detalle
FROM campuscloud_eventos.eventos_por_estudiante
WHERE estudiante_id = 'EST-001' AND periodo = '2026-11';
