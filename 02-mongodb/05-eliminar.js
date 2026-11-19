const campus = db.getSiblingDB("campuscloud_nosql");
const servicios = campus.detalles_servicios;
print("ANTES de eliminar DET-007:");
printjson(servicios.findOne({ _id: "DET-007" }));
const resultado = servicios.deleteOne({ _id: "DET-007" });
printjson({ eliminados: resultado.deletedCount });
print("DESPUES: busqueda por el mismo identificador");
printjson(servicios.findOne({ _id: "DET-007" }));
printjson({ totalRestante: servicios.countDocuments({}) });
