// Ejecutar ANTES del reinicio y DESPUES de reiniciar MongoDB.
const campus = db.getSiblingDB("campuscloud_nosql");
printjson({
  base: campus.getName(),
  coleccion: "detalles_servicios",
  total: campus.detalles_servicios.countDocuments({}),
  muestra: campus.detalles_servicios.findOne(
    { _id: "DET-002" }, { nombre: 1, "configuracion.capacidad": 1 }
  )
});
