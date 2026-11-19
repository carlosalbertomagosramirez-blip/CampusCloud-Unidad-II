// Ejecutar ANTES y DESPUES de docker compose restart neo4j.
MATCH (e:Estudiante)
WITH count(e) AS estudiantes
MATCH (s:Servicio)
WITH estudiantes, count(s) AS servicios
MATCH ()-[r:UTILIZA]->()
RETURN estudiantes, servicios, count(r) AS relaciones;

MATCH (e:Estudiante {id:'EST-001'})-[r:UTILIZA]->(s:Servicio {id:101})
RETURN e.nombre AS estudiante, s.nombre AS servicio, r.visitas AS visitas;
