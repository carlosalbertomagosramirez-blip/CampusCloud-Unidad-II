// Datos totalmente ficticios. MERGE permite ejecutar el archivo nuevamente.
CREATE CONSTRAINT estudiante_id_u2 IF NOT EXISTS
FOR (e:Estudiante) REQUIRE e.id IS UNIQUE;

CREATE CONSTRAINT servicio_id_u2 IF NOT EXISTS
FOR (s:Servicio) REQUIRE s.id IS UNIQUE;

UNWIND [
  {id:'EST-001', nombre:'Luna Perez', carrera:'TI', semestre:4},
  {id:'EST-002', nombre:'Bruno Soto', carrera:'TI', semestre:3},
  {id:'EST-003', nombre:'Alma Ruiz', carrera:'Administracion', semestre:4},
  {id:'EST-004', nombre:'Tania Vega', carrera:'TI', semestre:2},
  {id:'EST-005', nombre:'Diego Solis', carrera:'Mecatronica', semestre:5}
] AS dato
MERGE (e:Estudiante {id:dato.id})
SET e.nombre=dato.nombre, e.carrera=dato.carrera, e.semestre=dato.semestre;

UNWIND [
  {id:101, nombre:'Biblioteca Digital', categoria:'Academico'},
  {id:102, nombre:'Laboratorio de Computo', categoria:'Academico'},
  {id:104, nombre:'Actividades Deportivas', categoria:'Bienestar'},
  {id:105, nombre:'Orientacion Estudiantil', categoria:'Bienestar'}
] AS dato
MERGE (s:Servicio {id:dato.id})
SET s.nombre=dato.nombre, s.categoria=dato.categoria;

UNWIND [
  {estudiante:'EST-001', servicio:101, visitas:5},
  {estudiante:'EST-001', servicio:102, visitas:3},
  {estudiante:'EST-002', servicio:101, visitas:2},
  {estudiante:'EST-002', servicio:104, visitas:7},
  {estudiante:'EST-002', servicio:105, visitas:1},
  {estudiante:'EST-003', servicio:101, visitas:4},
  {estudiante:'EST-003', servicio:105, visitas:2},
  {estudiante:'EST-004', servicio:102, visitas:6},
  {estudiante:'EST-004', servicio:104, visitas:2},
  {estudiante:'EST-005', servicio:104, visitas:3},
  {estudiante:'EST-005', servicio:105, visitas:4}
] AS dato
MATCH (e:Estudiante {id:dato.estudiante})
MATCH (s:Servicio {id:dato.servicio})
MERGE (e)-[r:UTILIZA]->(s)
ON CREATE SET r.visitas=dato.visitas, r.ultimaVisita=date('2026-11-10');

MATCH (e:Estudiante)
WITH count(e) AS estudiantes
MATCH (s:Servicio)
WITH estudiantes, count(s) AS servicios
MATCH ()-[r:UTILIZA]->()
RETURN estudiantes, servicios, count(r) AS relaciones;
