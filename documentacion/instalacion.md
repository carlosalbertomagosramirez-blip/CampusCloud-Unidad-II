# Instalación y resolución de problemas

1. Abrir el repositorio CampusCloud en VS Code. Incorporar las carpetas de este paquete **sin sustituir los archivos originales**.
2. Instalar e iniciar Docker Desktop. Ejecutar `docker version`.
3. Crear `docker/.env` desde `docker/.env.example` y establecer contraseñas locales; **no enviarlas**.
4. Revisar `docker network ls`. Si la red externa indicada en `DOCKER_NETWORK` no existe, crearla una sola vez.
5. En PowerShell, desde la raíz: `function dc { docker compose --env-file .\docker\.env -f .\docker\compose.yaml @args }`.
6. Comprobar `dc config --services` y luego `dc up -d mongodb`. No ejecutar `dc up -d` sin especificar servicios cuando los de Unidad I ya existan.
7. Completar MongoDB y tomar capturas. Detener el nuevo servicio si la laptop está limitada: `dc stop mongodb`.
8. Repetir para Neo4j; después Cassandra. No hace falta levantar los tres simultáneamente.

## Puertos

| Motor | Anfitrión | Puerto interno |
|---|---|---|
| PostgreSQL original | 54320 | 5432 |
| pgAdmin original | 8082 | 80 |
| SQL Server original | 14033 (variable) | 1433 |
| MongoDB nuevo | 127.0.0.1:28018 | 27017 |
| Neo4j Browser nuevo | 127.0.0.1:7475 | 7474 |
| Neo4j Bolt nuevo | 127.0.0.1:7688 | 7687 |
| Cassandra nuevo | 127.0.0.1:9042 | 9042 |

## Incidencias previsibles

| Mensaje o situación | Comprobación | Solución sin pérdida |
|---|---|---|
| `network ... not found` | `docker network ls` | Crear red con el nombre exacto o ajustar `DOCKER_NETWORK`. |
| `port is already allocated` | `docker ps` | Cambiar **solo** el puerto del nuevo servicio en `docker/.env`, no borrar el contenedor antiguo. |
| Neo4j rechaza contraseña | Revisar si el volumen ya existía | Las claves iniciales se establecen al crear la BD; recuperar la clave anterior o restablecerla mediante herramientas del gestor, sin eliminar el volumen. |
| Cassandra connection refused | `dc logs cassandra` | Esperar a que termine el arranque y repetir `cqlsh`. |
| MongoDB no acepta credenciales | Revisar usuario, clave y authSource | Autenticarse contra `admin`; evitar publicar la URI con contraseña. |
| `container name is already in use` | `docker ps -a` | Levantar solamente servicios de Unidad II; no eliminar los contenedores antiguos para despejar el nombre. |

## Nota sobre la red de clase

En el ZIP original, el Compose principal se encontraba en `campus-cloud-project/docker-compose.yml` y utilizaba una red externa. El nuevo Compose mantiene este concepto; comprueba que los nombres de volúmenes de PostgreSQL, pgAdmin y SQL Server en `docker/.env` coincidan con los originales **antes** de intentar operar los servicios de Unidad I desde este archivo.
