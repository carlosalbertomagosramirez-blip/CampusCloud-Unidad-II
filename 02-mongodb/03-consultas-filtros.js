const campus = db.getSiblingDB("campuscloud_nosql");
const servicios = campus.detalles_servicios;

print("FILTRO 1: servicios de categoria Academico");
printjson(servicios.find(
  { categoria: "Academico" }, { _id: 0, nombre: 1, categoria: 1 }
).toArray());

print("FILTRO 2: servicios con modalidad Presencial dentro del subdocumento");
printjson(servicios.find(
  { "configuracion.modalidad": "Presencial" },
  { _id: 0, nombre: 1, "configuracion.modalidad": 1 }
).toArray());

print("FILTRO 3: servicios cuyo array recursos contiene Reserva de equipo");
printjson(servicios.find(
  { recursos: "Reserva de equipo" }, { _id: 0, nombre: 1, recursos: 1 }
).toArray());
