// Modificacion controlada de una relacion: numero de visitas.
MATCH (e:Estudiante {id:'EST-001'})-[r:UTILIZA]->(s:Servicio {id:101})
RETURN e.nombre AS estudiante, s.nombre AS servicio, r.visitas AS antes;

MATCH (e:Estudiante {id:'EST-001'})-[r:UTILIZA]->(s:Servicio {id:101})
SET r.visitas=6, r.ultimaVisita=date('2026-11-12')
RETURN e.nombre AS estudiante, s.nombre AS servicio,
       r.visitas AS despues, r.ultimaVisita AS fecha;
