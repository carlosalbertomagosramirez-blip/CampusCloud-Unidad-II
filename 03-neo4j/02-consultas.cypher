// CONSULTA 1 - Servicios que utiliza Luna (EST-001).
MATCH (e:Estudiante {id:'EST-001'})-[r:UTILIZA]->(s:Servicio)
RETURN e.nombre AS estudiante, s.nombre AS servicio, r.visitas AS visitas
ORDER BY s.nombre;

// CONSULTA 2 - Estudiantes que comparten un mismo servicio.
MATCH (a:Estudiante)-[:UTILIZA]->(s:Servicio)<-[:UTILIZA]-(b:Estudiante)
WHERE a.id < b.id
RETURN s.nombre AS servicio, a.nombre AS estudiante_1, b.nombre AS estudiante_2
ORDER BY servicio, estudiante_1;

// CONSULTA 3 - Recomendar servicios no usados por EST-001,
// encontrados a traves de estudiantes con un servicio en comun.
MATCH (yo:Estudiante {id:'EST-001'})-[:UTILIZA]->(:Servicio)<-[:UTILIZA]-(otro:Estudiante)
MATCH (otro)-[:UTILIZA]->(recomendado:Servicio)
WHERE NOT EXISTS {
  MATCH (yo)-[:UTILIZA]->(recomendado)
}
RETURN recomendado.nombre AS servicio_recomendado,
       count(DISTINCT otro) AS estudiantes_que_lo_utilizan
ORDER BY estudiantes_que_lo_utilizan DESC, servicio_recomendado;

// VISTA GRAFICA: pegar esta ultima consulta en Neo4j Browser.
MATCH (e:Estudiante)-[r:UTILIZA]->(s:Servicio)
RETURN e, r, s;
