# CampusCloud - Unidad II | Prácticas integradas NoSQL

**Estudiante:** Carlos Alberto Magos Ramírez  
**Materia:** Bases de Datos en la Nube  
**Docente:** Ing. José Luis Herrera Gallardo, MTI  
**Alcance:** MongoDB + Neo4j + Apache Cassandra. SQL Server continúa siendo la base principal.

> **Estado de la entrega:** scripts y configuración preparados. Deben ejecutarse en Docker Desktop y añadirse capturas **reales** antes de entregar al docente. Este paquete no incluye resultados fingidos.

## 1. Cómo integrar con el proyecto de clase

Este paquete se preparó a partir de la revisión de `CampusCloud(1).zip`. **No sustituye ni borra la carpeta original CampusCloud**: combina estas carpetas y archivos con tu repositorio actual. No copies contraseñas del ZIP original a GitHub. La carpeta `api/` de Node.js de clase no es necesaria para esta evaluación y puede conservarse sin cambios.

El archivo principal nuevo es `docker/compose.yaml`. Conserva las definiciones de PostgreSQL, pgAdmin y SQL Server y añade tres servicios separados de Unidad II. Para evitar chocar con instalaciones previas, los puertos **nuevos** son MongoDB 28018 y Neo4j 7475/7688; los viejos 28017 y 7474/7687 no se tocan. Cassandra utiliza 9042.

No hay que arrancar todos los servicios simultáneamente: si los contenedores antiguos de Unidad I ya están funcionando, **inicia solo** `mongodb`, `neo4j` o `cassandra` de este Compose.

## 2. Requisitos

- Windows + Docker Desktop en ejecución.
- PowerShell y Visual Studio Code.
- Al menos 4 GB disponibles para Docker (preferiblemente más al arrancar Cassandra).
- MongoDB Compass y navegador web son útiles, pero la ejecución también funciona por consola dentro de los contenedores.

## 3. Configuración inicial (PowerShell, desde la raíz)

```powershell
Copy-Item .\docker\.env.example .\docker\.env
notepad .\docker\.env
```

Sustituye **todas** las claves de ejemplo por contraseñas locales propias. No envíes ese archivo por chat, GitHub o Classroom. Si ya existe la red externa usada en clase, consérvala; si no existe, créala:

```powershell
docker network ls
docker network create campus-network
```

El segundo comando solo debe ejecutarse si no existe esa red. Ajusta `DOCKER_NETWORK` en `docker/.env` si la red real tiene otro nombre.

Para escribir menos comandos, define esta función en la terminal PowerShell **dentro de la raíz del proyecto**:

```powershell
function dc { docker compose --env-file .\docker\.env -f .\docker\compose.yaml @args }
dc config --services
```

**No captures ni publiques `docker compose config` completo**, porque expande variables y podría imprimir contraseñas.

## 4. MongoDB: ejecutar 7 scripts

```powershell
dc up -d mongodb
dc ps mongodb
dc exec mongodb sh -lc 'mongosh --quiet -u "$MONGO_INITDB_ROOT_USERNAME" -p "$MONGO_INITDB_ROOT_PASSWORD" --authenticationDatabase admin --file /practicas/mongodb/01-crear-coleccion.js'
dc exec mongodb sh -lc 'mongosh --quiet -u "$MONGO_INITDB_ROOT_USERNAME" -p "$MONGO_INITDB_ROOT_PASSWORD" --authenticationDatabase admin --file /practicas/mongodb/02-insertar-documentos.js'
dc exec mongodb sh -lc 'mongosh --quiet -u "$MONGO_INITDB_ROOT_USERNAME" -p "$MONGO_INITDB_ROOT_PASSWORD" --authenticationDatabase admin --file /practicas/mongodb/03-consultas-filtros.js'
dc exec mongodb sh -lc 'mongosh --quiet -u "$MONGO_INITDB_ROOT_USERNAME" -p "$MONGO_INITDB_ROOT_PASSWORD" --authenticationDatabase admin --file /practicas/mongodb/04-actualizar.js'
dc exec mongodb sh -lc 'mongosh --quiet -u "$MONGO_INITDB_ROOT_USERNAME" -p "$MONGO_INITDB_ROOT_PASSWORD" --authenticationDatabase admin --file /practicas/mongodb/05-eliminar.js'
dc exec mongodb sh -lc 'mongosh --quiet -u "$MONGO_INITDB_ROOT_USERNAME" -p "$MONGO_INITDB_ROOT_PASSWORD" --authenticationDatabase admin --file /practicas/mongodb/06-agregacion.js'
dc exec mongodb sh -lc 'mongosh --quiet -u "$MONGO_INITDB_ROOT_USERNAME" -p "$MONGO_INITDB_ROOT_PASSWORD" --authenticationDatabase admin --file /practicas/mongodb/07-verificar-persistencia.js'
dc restart mongodb
dc exec mongodb sh -lc 'mongosh --quiet -u "$MONGO_INITDB_ROOT_USERNAME" -p "$MONGO_INITDB_ROOT_PASSWORD" --authenticationDatabase admin --file /practicas/mongodb/07-verificar-persistencia.js'
```

Para Compass: host `127.0.0.1`, puerto `28018`, autenticación de usuario/contraseña con la creada en `docker/.env` y origen de autenticación `admin`. Nunca muestres la contraseña en capturas.

**Resultado esperado, aún por verificar:** se cargan 7 documentos iniciales, se modifica DET-002, se elimina DET-007, y quedan 6. Tras reiniciar, se conserva DET-002 con capacidad 36.

## 5. Neo4j: ejecutar scripts Cypher

```powershell
dc up -d neo4j
dc ps neo4j
dc exec neo4j sh -lc 'cypher-shell -u neo4j -p "${NEO4J_AUTH#neo4j/}" -f /practicas/neo4j/01-crear-nodos-relaciones.cypher'
dc exec neo4j sh -lc 'cypher-shell -u neo4j -p "${NEO4J_AUTH#neo4j/}" -f /practicas/neo4j/02-consultas.cypher'
dc exec neo4j sh -lc 'cypher-shell -u neo4j -p "${NEO4J_AUTH#neo4j/}" -f /practicas/neo4j/03-actualizacion.cypher'
dc exec neo4j sh -lc 'cypher-shell -u neo4j -p "${NEO4J_AUTH#neo4j/}" -f /practicas/neo4j/04-verificar-persistencia.cypher'
dc restart neo4j
dc exec neo4j sh -lc 'cypher-shell -u neo4j -p "${NEO4J_AUTH#neo4j/}" -f /practicas/neo4j/04-verificar-persistencia.cypher'
```

Abre [Neo4j Browser](http://localhost:7475); conecta con usuario `neo4j` y tu contraseña local. Para la captura del grafo ejecuta:

```cypher
MATCH (e:Estudiante)-[r:UTILIZA]->(s:Servicio)
RETURN e, r, s;
```

**Resultado esperado, aún por verificar:** 5 estudiantes, 4 servicios, 11 relaciones; la recomendación para EST-001 encuentra actividades deportivas u orientación, y la relación EST-001/Biblioteca termina con 6 visitas.

## 6. Cassandra: ejecutar scripts CQL

Inicia solo Cassandra y espera a que termine el arranque (puede tardar varios minutos):

```powershell
dc up -d cassandra
dc logs --tail 30 cassandra
dc exec cassandra cqlsh -e "DESCRIBE KEYSPACES"
dc exec cassandra cqlsh -f /practicas/cassandra/01-crear-keyspace-tabla.cql
dc exec cassandra cqlsh -f /practicas/cassandra/02-insertar-eventos.cql
dc exec cassandra cqlsh -f /practicas/cassandra/03-consultas.cql
dc exec cassandra cqlsh -f /practicas/cassandra/04-actualizar.cql
dc exec cassandra cqlsh -f /practicas/cassandra/05-eliminar.cql
dc exec cassandra cqlsh -f /practicas/cassandra/06-verificar-persistencia.cql
```

Si aparece `Connection refused`, el servidor todavía puede estar iniciando: revisa `dc logs cassandra` y repite la conexión unos minutos después. No uses `ALLOW FILTERING` para resolver el diseño: la consulta debe indicar estudiante, periodo y rango de fecha.

**Resultado esperado, aún por verificar:** 13 eventos en 3 estudiantes inicialmente; una fila modificada y una eliminada por clave exacta, quedando 12.

## 7. Evidencias, seguridad y entrega

- Guarda capturas legibles con resultados reales en `evidencias/unidad-ii/` y registra resultado, fecha e incidencias en `docs/pruebas.md`.
- Para MongoDB y Neo4j muestra los datos antes y después de `dc restart mongodb` / `dc restart neo4j`.
- Anota al menos una incidencia **real** o una prueba preventiva explicada (por ejemplo, acceso denegado con contraseña incorrecta, sin exponer ninguna clave).
- No uses `docker compose down -v` ni `docker volume rm`: **eliminarían datos**.
- No entregues `.env`, `node_modules/`, imágenes `.tar` ni el directorio `.git/` en el ZIP.
- El PDF preparado se identifica como **borrador pendiente de evidencias**; debes completarlo con tus capturas reales antes de enviarlo.

Consulta el detalle en `docs/instalacion.md`, `docs/pruebas.md`, `docs/arquitectura-campuscloud.md` y `docs/comparacion-cloud-local.md`.

## 8. Regenerar los entregables (después de añadir evidencias)

Instala ReportLab si deseas volver a generar el PDF: `python -m pip install reportlab`.

```powershell
python .\tools\generar_reporte.py
python .\tools\empaquetar.py
```

El segundo comando crea el ZIP académico y el ZIP de integración en la carpeta superior `output/`. Incluye las capturas que efectivamente hayas guardado en `evidencias/unidad-ii/`, nunca archivos `.env` ni credenciales.
