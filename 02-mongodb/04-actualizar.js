const campus = db.getSiblingDB("campuscloud_nosql");
const servicios = campus.detalles_servicios;
print("ANTES de actualizar DET-002:");
printjson(servicios.findOne({ _id: "DET-002" }));

const resultado = servicios.updateOne(
  { _id: "DET-002" },
  { $set: { "configuracion.capacidad": 36, observacion: "Cupo ajustado para practicas" } }
);
printjson({ encontrados: resultado.matchedCount, modificados: resultado.modifiedCount });
print("DESPUES de actualizar DET-002:");
printjson(servicios.findOne({ _id: "DET-002" }));
