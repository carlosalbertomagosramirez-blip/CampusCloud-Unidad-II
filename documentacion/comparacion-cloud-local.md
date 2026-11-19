# Contraste entre Docker local y servicios cloud

Consulta documental: noviembre de 2026. La práctica local **no** equivale a un servicio administrado. Las alternativas siguientes resuelven necesidades similares, pero pueden usar APIs, semánticas o motores distintos.

| Necesidad | Docker local | AWS | Microsoft Azure | Google Cloud |
|---|---|---|---|---|
| Documentos flexibles | MongoDB 7 | Amazon DocumentDB (compatibilidad MongoDB, revisar diferencias) | Azure Cosmos DB for MongoDB | MongoDB Atlas en infraestructura Google Cloud (servicio del proveedor asociado) |
| Relaciones de grafos | Neo4j Community 5 | Amazon Neptune (openCypher, **no** motor Neo4j idéntico) | Azure Cosmos DB for Apache Gremlin (**lenguaje distinto de Cypher**) | Neo4j Aura como opción de tercero sobre Google Cloud |
| Eventos de columnas anchas | Apache Cassandra 5 | Amazon Keyspaces, compatible con Apache Cassandra | Azure Managed Instance for Apache Cassandra o Cosmos DB for Apache Cassandra | Cloud Bigtable (**no** es Cassandra ni usa CQL nativo de forma equivalente) |

## Responsabilidades

**Local (estudiante/organización):** instalar Docker y el motor; decidir puertos; elegir volumen; controlar parches, respaldo, recuperación, disponibilidad, credenciales, red y monitoreo. El host se apaga cuando se apaga la laptop.

**Servicio administrado:** el proveedor asume una parte del aprovisionamiento, infraestructura, mantenimiento y disponibilidad según el servicio y contrato. **El cliente aún debe** diseñar su esquema, elegir regiones/capacidad, gestionar identidades y permisos, proteger datos, definir retención, cumplir privacidad y controlar costos. No asumir que todos los servicios proporcionan las mismas garantías.

## Selección técnica

Para una práctica universitaria pequeña, Docker facilita estudiar los motores sin una suscripción cloud de pago. Si CampusCloud creciera a una carga real, evaluaríamos escalabilidad, presupuesto, compatibilidad de consultas, respaldo, región y requisitos de protección antes de seleccionar proveedor. Una migración de Neo4j a Neptune o Gremlin, o de Cassandra a Bigtable, necesita revisar consultas y modelo; no es equivalencia 1 a 1.

## Referencias oficiales

1. Amazon DocumentDB, compatibilidad con MongoDB: https://docs.aws.amazon.com/documentdb/latest/devguide/compatibility.html
2. Amazon Neptune, openCypher: https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher.html
3. Amazon Keyspaces: https://docs.aws.amazon.com/keyspaces/latest/devguide/
4. Azure Cosmos DB for MongoDB: https://learn.microsoft.com/azure/cosmos-db/mongodb-introduction
5. Azure Cosmos DB for Gremlin: https://learn.microsoft.com/azure/cosmos-db/graph-introduction
6. Azure Managed Instance for Apache Cassandra: https://learn.microsoft.com/azure/managed-instance-apache-cassandra/introduction
7. Cloud Bigtable: https://docs.cloud.google.com/bigtable/docs/overview
8. MongoDB Atlas y Google Cloud (alianza): https://cloud.google.com/blog/topics/partners/mongodb-expands-partnership-with-google-cloud
