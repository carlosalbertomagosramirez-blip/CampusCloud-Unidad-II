// Siete documentos ficticios, tres categorias, arrays y subdocumentos.
// Se usan upserts SOLO para la carga inicial: reejecutar no duplica registros.
const campus = db.getSiblingDB("campuscloud_nosql");
const coleccion = campus.detalles_servicios;
const documentos = [
  {
    _id: "DET-001", servicioId: NumberInt(101), nombre: "Biblioteca Digital",
    categoria: "Academico", activo: true,
    recursos: ["Libros digitales", "Revistas", "Reserva de sala"],
    configuracion: { modalidad: "Hibrida", horario: "08:00-20:00", capacidad: 80 },
    etiquetas: ["lectura", "investigacion"]
  },
  {
    _id: "DET-002", servicioId: NumberInt(102), nombre: "Laboratorio de Computo",
    categoria: "Academico", activo: true,
    recursos: ["Equipos", "Software", "Reserva de equipo"],
    configuracion: { modalidad: "Presencial", horario: "07:00-19:00", capacidad: 32 },
    etiquetas: ["programacion", "practicas"]
  },
  {
    _id: "DET-003", servicioId: NumberInt(103), nombre: "Tutorias Academicas",
    categoria: "Academico", activo: true,
    recursos: ["Asesoria", "Material de repaso"],
    configuracion: { modalidad: "En linea", horario: "09:00-17:00", capacidad: 25 },
    etiquetas: ["aprendizaje", "acompanamiento"]
  },
  {
    _id: "DET-004", servicioId: NumberInt(104), nombre: "Actividades Deportivas",
    categoria: "Bienestar", activo: true,
    recursos: ["Cancha", "Entrenador", "Material deportivo"],
    configuracion: { modalidad: "Presencial", horario: "15:00-20:00", capacidad: 40 },
    deportes: ["Futbol", "Basquetbol"]
  },
  {
    _id: "DET-005", servicioId: NumberInt(105), nombre: "Orientacion Estudiantil",
    categoria: "Bienestar", activo: true,
    recursos: ["Atencion personal", "Talleres"],
    configuracion: { modalidad: "Hibrida", horario: "08:00-16:00", capacidad: 20 },
    atencion: { citaPrevia: true, confidencial: true }
  },
  {
    _id: "DET-006", servicioId: NumberInt(106), nombre: "Control Escolar",
    categoria: "Administrativo", activo: true,
    recursos: ["Constancias", "Historial academico"],
    configuracion: { modalidad: "Presencial", horario: "09:00-15:00", capacidad: 15 },
    tramites: ["Constancia", "Inscripcion"]
  },
  {
    _id: "DET-007", servicioId: NumberInt(107), nombre: "Programa de Becas",
    categoria: "Administrativo", activo: true,
    recursos: ["Convocatorias", "Seguimiento"],
    configuracion: { modalidad: "En linea", horario: "09:00-17:00", capacidad: 100 },
    documentosRequeridos: ["Solicitud", "Comprobante"]
  }
];

const resultado = coleccion.bulkWrite(
  documentos.map(documento => {
    const { _id, ...datos } = documento;
    return {
      updateOne: {
        filter: { _id },
        update: { $setOnInsert: datos },
        upsert: true
      }
    };
  })
);
print("Carga terminada. Nuevos documentos insertados:");
printjson({ insertadosAhora: resultado.upsertedCount, totalActual: coleccion.countDocuments({}) });
printjson(coleccion.find({}, { _id: 1, servicioId: 1, categoria: 1 }).sort({ _id: 1 }).toArray());
