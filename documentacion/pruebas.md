# Bitácora de pruebas - llenar con ejecuciones reales

**IMPORTANTE:** los valores siguientes son objetivos o resultados esperados, NO ejecuciones verificadas por el autor de este paquete. Para entregar la misión debes completar cada registro con fecha, salida de consola y captura legible.

| ID | Motor | Prueba | Resultado esperado | Resultado real / fecha | Archivo de captura |
|---|---|---|---|---|---|
| M01 | MongoDB | Conexión/colección | Conexión y colección visible | PENDIENTE | mongodb/01-conexion.png |
| M02 | MongoDB | Carga | 7 documentos, 3 categorías | PENDIENTE | mongodb/02-documentos.png |
| M03 | MongoDB | 3 filtros | 3 conjuntos no vacíos | PENDIENTE | mongodb/03-filtros.png |
| M04 | MongoDB | UPDATE | Capacidad 32 a 36 | PENDIENTE | mongodb/04-actualizacion.png |
| M05 | MongoDB | DELETE | DET-007 eliminado | PENDIENTE | mongodb/05-eliminacion.png |
| M06 | MongoDB | Agregación | Conteo por categoría | PENDIENTE | mongodb/06-agregacion.png |
| M07 | MongoDB | Restart | 6 documentos persisten | PENDIENTE | mongodb/07-persistencia.png |
| M08 | MongoDB | Acceso | Autenticación habilitada | PENDIENTE | mongodb/08-autenticacion.png |
| N01 | Neo4j | Creación | 5 estudiantes, 4 servicios, 11 relaciones | PENDIENTE | neo4j/01-grafo.png |
| N02 | Neo4j | Tres consultas | Servicios, coincidencias, recomendaciones | PENDIENTE | neo4j/02-consultas.png |
| N03 | Neo4j | UPDATE | Visitas 5 a 6 | PENDIENTE | neo4j/03-modificacion.png |
| N04 | Neo4j | Restart | 9 nodos y 11 relaciones permanecen | PENDIENTE | neo4j/04-persistencia.png |
| C01 | Cassandra | Conexión/DDL | Keyspace y tabla disponibles | PENDIENTE | cassandra/01-creacion.png |
| C02 | Cassandra | Inserción | 13 eventos, 3 estudiantes | PENDIENTE | cassandra/02-eventos.png |
| C03 | Cassandra | Intervalo | EST-001 de 08 a 11 de noviembre | PENDIENTE | cassandra/03-consultas.png |
| C04 | Cassandra | UPDATE | Detalle modificado por PK completa | PENDIENTE | cassandra/04-actualizacion.png |
| C05 | Cassandra | DELETE | Evento exacto desaparece | PENDIENTE | cassandra/05-eliminacion.png |
| C06 | Cassandra | Acceso | CQL local, sin autenticar: limitación documentada | PENDIENTE | cassandra/06-conectividad.png |
| G01 | General | Incidencia | Problema real o prueba preventiva documentada | PENDIENTE | generales/01-incidencia.png |

## Registro de incidencia (obligatorio)

- Fecha/hora:
- Servicio:
- Error o prueba preventiva realizada:
- Comando o paso empleado:
- Resultado observado (literal, sin datos secretos):
- Causa identificada:
- Solución o medida de mitigación:
- Comprobación posterior:
- Captura:

## Evidencia de persistencia

1. Ejecutar el archivo de verificación del gestor y capturar el resultado **antes**.
2. Ejecutar `dc restart mongodb` o `dc restart neo4j`.
3. Esperar que responda y repetir la verificación.
4. Capturar la segunda salida. Comparar identificadores, conteos y propiedades.
5. No eliminar ni recrear volúmenes durante esta prueba.

## Evidencia de acceso y protección

- MongoDB: ingresar desde Compass con credenciales locales; si haces una prueba de contraseña errónea, documenta solo el mensaje de rechazo.
- Neo4j: verificar el acceso desde Browser o `cypher-shell` sin mostrar la clave.
- Cassandra: indicar explícitamente que el contenedor de un nodo se usa como laboratorio con acceso local, **sin autenticación CQL configurada**.
- Antes de GitHub o Classroom: revisar `.env`, capturas, historiales de consola y scripts SQL de Unidad I.
