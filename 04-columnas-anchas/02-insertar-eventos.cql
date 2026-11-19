-- 13 eventos ficticios, 3 estudiantes. Reejecucion: mismas claves = no duplica.
INSERT INTO campuscloud_eventos.eventos_por_estudiante
(estudiante_id, periodo, fecha_evento, evento_id, servicio_id, tipo_evento, detalle, origen)
VALUES ('EST-001','2026-11','2026-11-07T08:00:00Z',11111111-1111-4111-8111-111111111101,101,'CONSULTA','Ingreso a biblioteca digital','web');
INSERT INTO campuscloud_eventos.eventos_por_estudiante
(estudiante_id, periodo, fecha_evento, evento_id, servicio_id, tipo_evento, detalle, origen)
VALUES ('EST-001','2026-11','2026-11-08T09:15:00Z',11111111-1111-4111-8111-111111111102,102,'RESERVA','Aparto equipo de laboratorio','web');
INSERT INTO campuscloud_eventos.eventos_por_estudiante
(estudiante_id, periodo, fecha_evento, evento_id, servicio_id, tipo_evento, detalle, origen)
VALUES ('EST-001','2026-11','2026-11-09T12:30:00Z',11111111-1111-4111-8111-111111111103,101,'DESCARGA','Descargo material de estudio','movil');
INSERT INTO campuscloud_eventos.eventos_por_estudiante
(estudiante_id, periodo, fecha_evento, evento_id, servicio_id, tipo_evento, detalle, origen)
VALUES ('EST-001','2026-11','2026-11-10T10:00:00Z',11111111-1111-4111-8111-111111111104,102,'ACCESO','Ingreso al laboratorio','web');
INSERT INTO campuscloud_eventos.eventos_por_estudiante
(estudiante_id, periodo, fecha_evento, evento_id, servicio_id, tipo_evento, detalle, origen)
VALUES ('EST-001','2026-11','2026-11-11T15:45:00Z',11111111-1111-4111-8111-111111111105,101,'CONSULTA','Consulto bibliografia','movil');

INSERT INTO campuscloud_eventos.eventos_por_estudiante
(estudiante_id, periodo, fecha_evento, evento_id, servicio_id, tipo_evento, detalle, origen)
VALUES ('EST-002','2026-11','2026-11-07T11:00:00Z',22222222-2222-4222-8222-222222222201,104,'INSCRIPCION','Inscripcion a futbol','web');
INSERT INTO campuscloud_eventos.eventos_por_estudiante
(estudiante_id, periodo, fecha_evento, evento_id, servicio_id, tipo_evento, detalle, origen)
VALUES ('EST-002','2026-11','2026-11-08T16:10:00Z',22222222-2222-4222-8222-222222222202,104,'ASISTENCIA','Entrenamiento','movil');
INSERT INTO campuscloud_eventos.eventos_por_estudiante
(estudiante_id, periodo, fecha_evento, evento_id, servicio_id, tipo_evento, detalle, origen)
VALUES ('EST-002','2026-11','2026-11-10T07:50:00Z',22222222-2222-4222-8222-222222222203,101,'CONSULTA','Abrio biblioteca','web');
INSERT INTO campuscloud_eventos.eventos_por_estudiante
(estudiante_id, periodo, fecha_evento, evento_id, servicio_id, tipo_evento, detalle, origen)
VALUES ('EST-002','2026-11','2026-11-12T13:00:00Z',22222222-2222-4222-8222-222222222204,105,'CITA','Solicito orientacion','movil');

INSERT INTO campuscloud_eventos.eventos_por_estudiante
(estudiante_id, periodo, fecha_evento, evento_id, servicio_id, tipo_evento, detalle, origen)
VALUES ('EST-003','2026-11','2026-11-08T10:25:00Z',33333333-3333-4333-8333-333333333301,105,'CITA','Agendo orientacion','web');
INSERT INTO campuscloud_eventos.eventos_por_estudiante
(estudiante_id, periodo, fecha_evento, evento_id, servicio_id, tipo_evento, detalle, origen)
VALUES ('EST-003','2026-11','2026-11-09T09:40:00Z',33333333-3333-4333-8333-333333333302,101,'CONSULTA','Consulto revista','movil');
INSERT INTO campuscloud_eventos.eventos_por_estudiante
(estudiante_id, periodo, fecha_evento, evento_id, servicio_id, tipo_evento, detalle, origen)
VALUES ('EST-003','2026-11','2026-11-11T14:00:00Z',33333333-3333-4333-8333-333333333303,105,'ASISTENCIA','Acudio a orientacion','web');
INSERT INTO campuscloud_eventos.eventos_por_estudiante
(estudiante_id, periodo, fecha_evento, evento_id, servicio_id, tipo_evento, detalle, origen)
VALUES ('EST-003','2026-11','2026-11-13T08:20:00Z',33333333-3333-4333-8333-333333333304,101,'CONSULTA','Evento que se eliminara en prueba','movil');

SELECT estudiante_id, periodo, fecha_evento, tipo_evento
FROM campuscloud_eventos.eventos_por_estudiante
WHERE estudiante_id = 'EST-001' AND periodo = '2026-11';
