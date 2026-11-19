const campus = db.getSiblingDB("campuscloud_nosql");
print("Conteo de detalles de servicio por categoria:");
printjson(campus.detalles_servicios.aggregate([
  { $group: { _id: "$categoria", total: { $sum: 1 } } },
  { $sort: { _id: 1 } }
]).toArray());
