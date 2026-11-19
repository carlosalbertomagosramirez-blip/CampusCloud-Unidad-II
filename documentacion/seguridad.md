# Controles de seguridad en las prácticas

1. `docker/.env` se crea solo localmente; nunca forma parte del ZIP de entrega ni de GitHub.
2. `docker/.env.example` muestra nombres y claves ficticias; es seguro distribuirlo **solo sin sustituir por claves reales**.
3. Los puertos públicos de las nuevas bases se limitan a `127.0.0.1` del anfitrión, por lo que no se exponen directamente a otras máquinas de la red local. En Docker hay además una red interna compartida entre servicios.
4. MongoDB inicializa usuario administrador y contraseña local; Neo4j exige credencial inicial.
5. Cassandra de esta práctica **no configura autenticación CQL**. No desplegar la configuración tal cual en un servidor público o producción.
6. No copiar contraseñas reales a código, scripts, capturas o comandos que se documenten.
7. Los scripts históricos de SQL Server de la Unidad I deben revisarse por si contienen `CREATE LOGIN ... PASSWORD` con claves de ejemplo que se hayan convertido en reales.
8. No usar `docker compose down -v`, ni borrar volúmenes, durante pruebas de persistencia.
9. Hacer las pruebas con identificadores y datos ficticios; no extraer estudiantes reales de SQL Server.
