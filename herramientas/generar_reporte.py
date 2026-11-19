#!/usr/bin/env python3
"""Reporte CampusCloud. Genera un BORRADOR; no inventa ejecuciones."""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table,
    TableStyle, PageBreak, KeepTogether, HRFlowable
)

BASE = Path(__file__).resolve().parents[1]
DESTINO = BASE / "reportes" / "unidad-ii" / "Magos_Carlos_ReportePracticas_NoSQL.pdf"
DESTINO.parent.mkdir(parents=True, exist_ok=True)

FUENTES = [
    ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
     "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
    ("C:/Windows/Fonts/arial.ttf", "C:/Windows/Fonts/arialbd.ttf"),
]
par = next(((r, b) for r, b in FUENTES if Path(r).exists() and Path(b).exists()), None)
if par is None:
    raise RuntimeError("Se requiere DejaVu Sans (Linux) o Arial (Windows) para el PDF.")
FUENTE, FUENTE_B = par
pdfmetrics.registerFont(TTFont("DejaVu", FUENTE))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", FUENTE_B))

NAVY = colors.HexColor("#12243B")
BLUE = colors.HexColor("#1C4B78")
TEAL = colors.HexColor("#12A89D")
LIGHT = colors.HexColor("#EFF5F9")
GRAY = colors.HexColor("#536779")
MUTED = colors.HexColor("#66788A")
RED = colors.HexColor("#A63D3D")
WHITE = colors.white

ESTILOS = {
  "h1": ParagraphStyle("h1", fontName="DejaVu-Bold", fontSize=17, leading=23,
                       textColor=NAVY, spaceAfter=12),
  "h2": ParagraphStyle("h2", fontName="DejaVu-Bold", fontSize=10.6, leading=15,
                       textColor=BLUE, spaceBefore=11, spaceAfter=5),
  "body": ParagraphStyle("body", fontName="DejaVu", fontSize=8.6, leading=13.5,
                         textColor=NAVY, spaceAfter=7),
  "small": ParagraphStyle("small", fontName="DejaVu", fontSize=7.4, leading=11,
                          textColor=NAVY, spaceAfter=3),
  "table": ParagraphStyle("table", fontName="DejaVu", fontSize=7.2, leading=10.7,
                          textColor=NAVY),
  "tablehead": ParagraphStyle("tablehead", fontName="DejaVu-Bold", fontSize=7.1,
                              leading=10.7, textColor=WHITE),
  "caption": ParagraphStyle("caption", fontName="DejaVu", fontSize=7.1, leading=10,
                            textColor=MUTED, spaceAfter=5),
  "alert": ParagraphStyle("alert", fontName="DejaVu-Bold", fontSize=8.2, leading=13,
                          textColor=RED),
  "cover": ParagraphStyle("cover", fontName="DejaVu-Bold", fontSize=25,
                          leading=32, textColor=WHITE, alignment=TA_LEFT),
  "coversub": ParagraphStyle("coversub", fontName="DejaVu", fontSize=12,
                             leading=19, textColor=WHITE),
}

ANCHO = letter[0] - 2 * 49
contenido = []

def p(txt, style="body"):
    contenido.append(Paragraph(txt, ESTILOS[style]))

def h1(txt): p(txt, "h1")
def h2(txt): p(txt, "h2")
def space(h=10): contenido.append(Spacer(1,h))

def grid(headers, rows, widths=None):
    vals = [[Paragraph(str(x), ESTILOS["tablehead"]) for x in headers]]
    vals += [[Paragraph(str(x), ESTILOS["table"]) for x in row] for row in rows]
    t = Table(vals, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), BLUE),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT]),
        ("GRID", (0,0), (-1,-1), 0.35, colors.HexColor("#D9E2EB")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    contenido.append(t)
    space(8)

def alert(txt):
    t = Table([[Paragraph(txt, ESTILOS["alert"])]], colWidths=[ANCHO])
    t.setStyle(TableStyle([
       ("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#FFF2EF")),
       ("BOX",(0,0),(-1,-1),0.6,colors.HexColor("#EFCCC6")),
       ("LEFTPADDING",(0,0),(-1,-1),12),
       ("RIGHTPADDING",(0,0),(-1,-1),12),
       ("TOPPADDING",(0,0),(-1,-1),10),
       ("BOTTOMPADDING",(0,0),(-1,-1),10),
    ]))
    contenido.append(t)
    space(9)

def evidence_box(txt):
    celda = Paragraph(
        "<b>ESPACIO RESERVADO PARA EVIDENCIA REAL</b><br/><br/>" + txt,
        ESTILOS["caption"]
    )
    t = Table([[celda]], colWidths=[ANCHO], rowHeights=[115])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), LIGHT),
        ("BOX", (0,0), (-1,-1), 0.8, colors.HexColor("#A9BAC8")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("LEFTPADDING", (0,0), (-1,-1), 22),
    ]))
    contenido.append(t)
    space(7)

def page(): contenido.append(PageBreak())

class Reporte(BaseDocTemplate):
    def __init__(self, filename):
        super().__init__(str(filename), pagesize=letter, leftMargin=49,
                         rightMargin=49, topMargin=57, bottomMargin=51,
                         title="CampusCloud - Reporte de Prácticas NoSQL (BORRADOR)",
                         author="Carlos Alberto Magos Ramírez")
        marco = Frame(49, 51, ANCHO, letter[1] - 108,
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates(PageTemplate(id="normal", frames=marco, onPage=self.fondo))

    def fondo(self, can, doc):
        w, hh = letter
        if doc.page == 1:
            can.setFillColor(NAVY)
            can.rect(0, 0, w, hh, stroke=0, fill=1)
            can.setFillColor(TEAL)
            can.rect(49, hh - 116, 70, 5, stroke=0, fill=1)
            return
        can.setFillColor(NAVY)
        can.rect(0, hh-29, w, 29, stroke=0, fill=1)
        can.setFont("DejaVu-Bold", 8)
        can.setFillColor(WHITE)
        can.drawString(49, hh-18, "CAMPUSCLOUD  /  BASES DE DATOS EN LA NUBE")
        can.setStrokeColor(colors.HexColor("#D8E3EB"))
        can.line(49, 38, w-49, 38)
        can.setFont("DejaVu", 7.0)
        can.setFillColor(RED)
        can.drawString(49, 26, "BORRADOR - faltan ejecuciones y capturas reales")
        can.setFillColor(GRAY)
        can.drawRightString(w-49, 26, f"{doc.page}")

# 1. Portada
space(108)
p("ACTIVIDAD DE EVALUACIÓN 2<br/>PRÁCTICAS INTEGRADAS NoSQL", "cover")
space(14)
p("CampusCloud · Unidad II<br/>MongoDB · Neo4j · Apache Cassandra", "coversub")
space(52)
for item in [
    "<b>Universidad:</b> Universidad Tecnológica de Tula-Tepeji",
    "<b>Asignatura:</b> Bases de Datos en la Nube",
    "<b>Docente:</b> Ing. José Luis Herrera Gallardo, MTI",
    "<b>Estudiante:</b> Carlos Alberto Magos Ramírez",
    "<b>Periodo:</b> noviembre de 2026",
]:
    par = Paragraph(item, ParagraphStyle(
        "coverinfo", parent=ESTILOS["body"], fontSize=10.3, leading=18,
        textColor=WHITE, spaceAfter=5))
    contenido.append(par)
space(48)
p("<b>ESTADO DEL DOCUMENTO:</b> borrador técnico con scripts preparados. "
  "Las pruebas deben ejecutarse en Docker Desktop y las capturas se deben "
  "integrar antes de entregar en Classroom.", "coversub")
page()

# 2. Contexto
h1("01  Problema y arquitectura propuesta")
p("En la Unidad I, CampusCloud empleó SQL Server para administrar información "
  "estructurada de estudiantes, servicios y solicitudes. Al aumentar los casos "
  "de uso aparecieron datos semiestructurados, relaciones entre usuarios y "
  "servicios y eventos de actividad que requieren patrones de consulta distintos. "
  "No es necesario sustituir la base relacional: se propone complementarla "
  "mediante persistencia políglota.")
h2("Selección justificada de modelos")
grid(["Necesidad", "Modelo / motor", "Justificación"], [
    ["Atributos distintos por servicio", "Documental / MongoDB",
     "Permite recursos en arreglos y configuración como subdocumento sin alterar tablas transaccionales."],
    ["Afinidad y recomendaciones", "Grafo / Neo4j",
     "Facilita recorrer relaciones Estudiante-UTILIZA-Servicio y encontrar vecinos en común."],
    ["Bitácora por estudiante y mes", "Columnas anchas / Cassandra",
     "Agrupa eventos por clave de partición y ordena fechas dentro de cada partición."],
], widths=[150,130,ANCHO-280])
h2("Separación de responsabilidades")
grid(["SQL Server (Unidad I)", "Nuevos motores (Unidad II)"], [
    ["Identidad del estudiante, catálogo base, solicitudes y operaciones transaccionales.",
     "Solo extensiones documentales, conexiones del grafo y registros de eventos ficticios."]
], widths=[ANCHO/2,ANCHO/2])
p("Los identificadores <b>servicioId</b> y <b>estudiante_id</b> se usan como "
  "referencias lógicas. La demostración no crea llaves foráneas entre motores "
  "ni pretende que los datos ficticios estén presentes en el SQL Server original.")
h2("Criterios de éxito")
p("Se evaluarán operaciones reproducibles, consultas que devuelvan resultados "
  "verificables, persistencia después de reiniciar contenedores, acceso básico "
  "y manejo responsable de credenciales.")
page()

# 3. Configuración
h1("02  Configuración general de Docker")
p("La propuesta agrega tres servicios a un archivo <b>docker/compose.yaml</b> "
  "conservando las definiciones originales de PostgreSQL, pgAdmin y SQL Server. "
  "El proyecto incorpora un ejemplo de variables <b>.env.example</b> sin "
  "secretos reales, volúmenes persistentes y una red Docker externa.")
grid(["Servicio nuevo", "Puerto local", "Volumen persistente"], [
    ["MongoDB 7", "127.0.0.1:28018", "campuscloud_u2_mongodb_data"],
    ["Neo4j 5 Community", "127.0.0.1:7475 y :7688", "campuscloud_u2_neo4j_data"],
    ["Cassandra 5.0", "127.0.0.1:9042", "campuscloud_u2_cassandra_data"],
], widths=[139,150,ANCHO-289])
h2("Procedimiento operativo")
p("1. Iniciar Docker Desktop y verificar la red externa. 2. Copiar "
  "<b>docker/.env.example</b> a <b>docker/.env</b> y completar las claves "
  "localmente. 3. Iniciar un gestor a la vez. 4. Ejecutar los scripts "
  "numerados. 5. Registrar salidas reales y capturas. "
  "6. Reiniciar MongoDB y Neo4j y verificar que la información permanezca.")
h2("Prevención de conflictos")
p("Se eligieron puertos y nombres distintos para las prácticas nuevas porque "
  "en el proyecto de clase había una instalación independiente de Neo4j y "
  "una conexión previa de MongoDB por el puerto 28017. No se detienen ni se "
  "eliminan automáticamente los contenedores existentes. Los gestores de "
  "Unidad I se arrancarán solamente si el estudiante confirma su configuración.")
h2("Seguridad básica")
p("MongoDB dispone de autenticación administrativa y Neo4j exige acceso con "
  "contraseña. Cassandra se instala como laboratorio de un nodo sin "
  "autenticación CQL; no debe exponerse públicamente. Los puertos nuevos "
  "están enlazados a 127.0.0.1, y las claves reales no se incluyen en ZIP, "
  "GitHub, scripts ni capturas.")
alert("Prueba todavía pendiente: comprobar docker compose ps, conexiones a cada cliente y persistencia real.")
page()

# 4. MongoDB
h1("03  MongoDB: sector documental")
p("La colección <b>campuscloud_nosql.detalles_servicios</b> almacena solo la "
  "información extendida de servicios. Los documentos incluyen identificador "
  "de referencia, categoría, arreglo de recursos y subdocumento de configuración. "
  "Esto permite que Biblioteca, Laboratorio y Deportes tengan campos específicos.")
grid(["Archivo", "Operación / salida que se debe comprobar"], [
    ["01-crear-coleccion.js", "Crea colección e índices, uno único por servicioId."],
    ["02-insertar-documentos.js", "Carga inicial de 7 documentos en 3 categorías, sin duplicar en reejecuciones."],
    ["03-consultas-filtros.js", "Filtra por categoría, por campo anidado y por elemento en arreglo."],
    ["04-actualizar.js", "Muestra DET-002 antes y después del cambio de capacidad 32 a 36."],
    ["05-eliminar.js", "Elimina DET-007 por _id y verifica su ausencia."],
    ["06-agregacion.js", "Agrupa y cuenta documentos por categoría."],
    ["07-verificar-persistencia.js", "Recupera conteo y dato actualizado antes y después del reinicio."],
], widths=[167,ANCHO-167])
h2("Lógica de diseño")
p("El identificador <b>servicioId</b> referencia un servicio del catálogo "
  "relacional sin duplicar sus transacciones. Se incluyen mínimo tres "
  "categorías, arreglos y documentos anidados. La agregación hace "
  "<b>$group</b> por categoría y <b>$sum</b> para el total.")
h2("Resultados esperados (no son evidencia de ejecución)")
p("Siete documentos iniciales; después del borrado queda una colección de seis "
  "documentos. La capacidad modificada del laboratorio debe conservarse tras "
  "reiniciar el contenedor gracias al volumen Docker.")
alert("Pendiente: capturas M01-M08 de Compass/terminal, filtros con salida, antes-después, agregación y reinicio.")
evidence_box("Capturas reales de MongoDB Compass o consola con el resultado de filtros y cambios.")
page()

# 5. Neo4j
h1("04  Neo4j: red de conexiones")
p("La implementación introduce cinco nodos <b>Estudiante</b>, cuatro nodos "
  "<b>Servicio</b> y once relaciones dirigidas <b>UTILIZA</b> con propiedades "
  "de visitas y fecha. Los nombres e identificadores son ficticios.")
grid(["Consulta / acción", "Pregunta que resuelve"], [
    ["Creación", "MERGE de 9 nodos y 11 aristas; restricciones únicas por id."],
    ["Consulta 1", "¿Qué servicios utiliza EST-001? Devuelve nombres y visitas."],
    ["Consulta 2", "¿Qué pares de estudiantes comparten un mismo servicio?"],
    ["Consulta 3", "¿Qué servicios usan sus pares y EST-001 todavía no utiliza?"],
    ["Actualización", "La relación EST-001 con Biblioteca cambia de 5 a 6 visitas."],
    ["Persistencia", "Se comprueban conteos y propiedades antes y después del reinicio."],
], widths=[121,ANCHO-121])
h2("Recomendación sencilla")
p("Se parte de EST-001 y se buscan otros estudiantes conectados al mismo "
  "servicio. Luego se localizan servicios que estos compañeros usan y el "
  "estudiante inicial todavía no utiliza. La consulta evita recomendar "
  "servicios ya usados y ordena por el número de estudiantes que los comparten.")
h2("Modelo conceptual")
p("<b>Estudiante</b> -[<b>UTILIZA</b> {visitas, ultimaVisita}]-&gt; "
  "<b>Servicio</b>. No se importa toda la base relacional: solamente "
  "identificadores y propiedades pertinentes al grafo de prueba.")
h2("Resultados esperados (no verificados)")
p("El grafo presenta nueve nodos y once relaciones; la consulta de "
  "recomendación devuelve opciones de bienestar para EST-001 y después del "
  "reinicio la relación de Biblioteca conserva seis visitas.")
alert("Pendiente: captura del grafo en Neo4j Browser, tres tablas Cypher, actualización y reinicio.")
evidence_box("Grafo real de Neo4j Browser y resumen de las consultas con resultados tabulares.")
page()

# 6. Cassandra
h1("05  Cassandra: bitácora de eventos")
p("El registro se diseñó a partir de la pregunta: <b>¿qué actividades registró "
  "un estudiante durante un periodo determinado?</b> Se usa el keyspace "
  "<b>campuscloud_eventos</b> y la tabla <b>eventos_por_estudiante</b>.")
grid(["Elemento", "Diseño", "Justificación"], [
    ["Partition key", "(estudiante_id, periodo)", "Una partición por alumno y mes; limita crecimiento temporal."],
    ["Clustering", "fecha_evento DESC, evento_id ASC", "Recorrido temporal y unicidad incluso con igual fecha."],
    ["Otros campos", "servicio_id, tipo_evento, detalle, origen", "Descripción suficiente de cada interacción ficticia."],
], widths=[120,169,ANCHO-289])
h2("Carga y operaciones CQL")
p("Se prepararon trece <b>INSERT</b> de tres estudiantes, una consulta por "
  "estudiante y rango de fechas compatible con la clave, una actualización "
  "<b>UPDATE</b> por clave completa y una eliminación <b>DELETE</b> controlada. "
  "Tras la eliminación deben quedar doce eventos. Los scripts tienen "
  "identificadores UUID fijos para no duplicar filas por una reejecución.")
h2("Limitaciones y decisión de diseño")
p("Cassandra no debe tratarse como SQL Server. Consultar globalmente por tipo "
  "de evento, sin estudiante y periodo, no corresponde a esta tabla. "
  "Para otra consulta frecuente se diseñaría otra tabla o vista de consulta. "
  "Se evita <b>ALLOW FILTERING</b> porque no resuelve el modelo de acceso.")
h2("Configuración local")
p("Se utiliza un solo nodo de Cassandra con replicación SimpleStrategy "
  "factor 1, suficiente para demostrar CQL en clase pero sin tolerancia real "
  "a fallos. El servicio se limita a la máquina local y requiere esperar "
  "su arranque antes de ejecutar cqlsh.")
alert("Pendiente: capturas C01-C06 con CREATE, carga, SELECT, antes/después de UPDATE y DELETE.")
evidence_box("Resultados reales de cqlsh para CREATE TABLE, SELECT, UPDATE y DELETE.")
page()

# 7. Verificaciones
h1("06  Conectividad, persistencia y diagnóstico")
p("Las pruebas se documentarán en <b>docs/pruebas.md</b>, incluyendo fecha, "
  "comando, resultado real, archivo de captura y solución cuando exista "
  "una incidencia. Una captura del código sin su salida no demuestra el "
  "funcionamiento solicitado.")
grid(["Control", "Procedimiento verificable"], [
    ["Conectividad", "docker compose ps, cliente del gestor, host/puerto y consulta de lectura."],
    ["Persistencia MongoDB", "Leer DET-002; reiniciar contenedor; leer el mismo identificador y capacidad."],
    ["Persistencia Neo4j", "Contar nodos/relaciones; reiniciar; recuperar los mismos conteos y visitas."],
    ["Acceso MongoDB/Neo4j", "Autenticación en clientes y protección de claves en .env local."],
    ["Cassandra", "cqlsh local; identificar de forma transparente la ausencia de autenticación CQL."],
    ["Incidencia", "Documentar una falla real o una prueba preventiva, su causa y la mitigación."],
], widths=[130,ANCHO-130])
h2("Prueba preventiva sugerida")
p("Intentar una autenticación con contraseña deliberadamente incorrecta "
  "en uno de los gestores protegidos y comprobar que el acceso se rechaza. "
  "No se registra ni captura la contraseña usada; solo el mensaje de rechazo. "
  "Después se repite el acceso autorizado. Esta prueba deberá ejecutarse "
  "realmente antes de redactarla como resultado.")
h2("Reglas de protección de información")
p("No publicar archivos .env, historial con contraseñas, URI que incluyan "
  "claves, carpetas de datos ni imágenes exportadas de Docker. Usar usuarios "
  "y servicios ficticios. Nunca destruir volúmenes para obtener una captura; "
  "reiniciar mantiene los datos.")
alert("Incidencia y controles: resultados aún por llenar en la bitácora real de pruebas.")
evidence_box("Captura de persistencia o autenticación, con registro del error real o prueba preventiva.")
page()

# 8. Nube
h1("07  Docker local frente a nube")
p("Docker es un entorno de ejecución y orquestación local, no un servicio "
  "administrado equivalente a las bases de datos ofrecidas por proveedores "
  "cloud. La elección futura depende de volumen, latencia, región, soporte, "
  "presupuesto y compatibilidad de consultas.")
grid(["Modelo", "AWS", "Azure", "Google Cloud"], [
    ["Documental", "DocumentDB (compatible con MongoDB)", "Cosmos DB for MongoDB", "MongoDB Atlas sobre GCP (tercero)"],
    ["Grafos", "Neptune con openCypher", "Cosmos DB for Apache Gremlin", "Neo4j Aura como tercero en GCP"],
    ["Columnas anchas", "Keyspaces compatible con Cassandra", "Managed Instance for Cassandra", "Bigtable, distinto de Cassandra"],
], widths=[93,143,145,ANCHO-381])
h2("Límites de equivalencia")
p("Amazon DocumentDB y Cosmos DB for MongoDB declaran compatibilidad con "
  "consultas de MongoDB, que se debe comprobar funcionalmente. Neptune "
  "acepta openCypher, pero no es una instalación de Neo4j; Azure Gremlin "
  "emplea un lenguaje diferente. Bigtable no ejecuta automáticamente "
  "los mismos comandos CQL de Cassandra.")
h2("Quién administra qué")
p("<b>En Docker local:</b> el estudiante administra hardware, instalación, "
  "parches, red, usuarios, discos, backups y fallos. <b>En cloud administrado:</b> "
  "el proveedor opera parte de la infraestructura, mantenimiento y escalado "
  "según el servicio. El cliente conserva responsabilidades sobre modelos "
  "de datos, identidad, permisos, clasificación, privacidad, costos y retención.")
h2("Evaluación para CampusCloud")
p("La opción local es adecuada para aprender y demostrar consultas de forma "
  "controlada. Para producción se compararía el precio real, la compatibilidad "
  "de cada operación, la residencia de los datos, el soporte de recuperación "
  "y la conectividad privada antes de elegir una plataforma.")
page()

# 9. Cierre
h1("08  Conclusiones y referencias")
h2("Conclusiones técnicas personales")
p("El ejercicio permite comprender que no conviene guardar todos los datos "
  "universitarios con el mismo modelo. MongoDB se adapta a propiedades "
  "opcionales de servicios; Neo4j representa relaciones necesarias para "
  "recomendaciones; Cassandra obliga a diseñar la tabla desde la consulta "
  "que realmente se hará. SQL Server sigue siendo el punto central de las "
  "operaciones estructuradas de CampusCloud.")
p("Otro aprendizaje es la importancia de la reproducibilidad. Un proyecto "
  "no se termina únicamente al escribir consultas: también debe permitir "
  "a otra persona levantar contenedores, obtener resultados, reiniciar, "
  "comprobar el acceso y documentar incidentes. <b>Estas conclusiones se "
  "refieren al diseño preparado; la demostración real todavía está pendiente.</b>")
h2("Lista final para Classroom")
grid(["Entregable", "Estado actual"], [
    ["ZIP de scripts, Compose, .env.example, README", "Preparado; falta insertar capturas reales."],
    ["PDF técnico (6 a 10 páginas)", "Borrador; completar resultados y evidencias."],
    ["GitHub y comprobación en vivo", "Sin publicar; sincronizar después de verificar."],
], widths=[ANCHO*0.62,ANCHO*0.38])
h2("Referencias oficiales consultadas (noviembre de 2026)")
refs = [
    "AWS. Amazon DocumentDB y compatibilidad MongoDB. docs.aws.amazon.com/documentdb/latest/devguide/compatibility.html",
    "AWS. Amazon Neptune con openCypher. docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher.html",
    "AWS. Amazon Keyspaces. docs.aws.amazon.com/keyspaces/latest/devguide/",
    "Microsoft. Cosmos DB para MongoDB. learn.microsoft.com/azure/cosmos-db/mongodb-introduction",
    "Microsoft. Cosmos DB para Gremlin. learn.microsoft.com/azure/cosmos-db/graph-introduction",
    "Microsoft. Managed Instance for Apache Cassandra. learn.microsoft.com/azure/managed-instance-apache-cassandra/introduction",
    "Google Cloud. Bigtable overview. docs.cloud.google.com/bigtable/docs/overview",
]
for i, ref in enumerate(refs, 1):
    p(f"{i}. {ref}", "small")
space(6)
alert("No entregar este PDF como prueba completa hasta incorporar resultados auténticos y las capturas requeridas.")

doc = Reporte(DESTINO)
doc.build(contenido)
print(DESTINO)
