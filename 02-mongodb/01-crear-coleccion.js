// Uso: mongosh --file 01-crear-coleccion.js (en el contenedor).
// SQL Server conserva Estudiantes, Servicios y Solicitudes;
// MongoDB guarda solo los detalles extensibles de un servicio.
const campus = db.getSiblingDB("campuscloud_nosql");
const nombre = "detalles_servicios";

if (!campus.getCollectionNames().includes(nombre)) {
  campus.createCollection(nombre, {
    validator: {
      $jsonSchema: {
        bsonType: "object",
        required: ["_id", "servicioId", "nombre", "categoria", "recursos", "configuracion"],
        properties: {
          _id: { bsonType: "string" },
          servicioId: { bsonType: "int" },
          nombre: { bsonType: "string" },
          categoria: { enum: ["Academico", "Bienestar", "Administrativo"] },
          recursos: { bsonType: "array" },
          configuracion: { bsonType: "object" }
        }
      }
    }
  });
  print("Coleccion detalles_servicios creada.");
} else {
  print("La coleccion detalles_servicios ya existia.");
}

campus[nombre].createIndex({ servicioId: 1 }, { unique: true });
campus[nombre].createIndex({ categoria: 1 });
printjson(campus.getCollectionInfos({ name: nombre }).map(x => ({
  nombre: x.name,
  tipo: x.type
})));
