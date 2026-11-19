# Arquitectura de CampusCloud - Unidad II

CampusCloud aplica persistencia políglota: cada tecnología responde a una consulta o necesidad concreta. La identidad del estudiante y las operaciones transaccionales permanecen en SQL Server (Unidad I); no se copian todas las tablas a los motores NoSQL.

| Responsabilidad | Datos | Tecnología |
|---|---|---|
| Núcleo transaccional | Estudiantes, Servicios, Solicitudes | SQL Server |
| Detalles de un servicio | Atributos variables, listas de recursos, configuraciones | MongoDB |
| Relaciones y afinidades | Estudiantes -[UTILIZA]-> Servicios | Neo4j |
| Bitácoras por fecha | Eventos por estudiante y mes | Cassandra |

## Referencias lógicas

MongoDB guarda `servicioId` como referencia ficticia a `Servicios.id` de SQL Server. Neo4j usa `Estudiante.id` y `Servicio.id` como identificadores lógicos. Cassandra conserva `estudiante_id`, `servicio_id` y fecha del evento. Estas referencias se usan solo en la demostración; **no se presupone que los registros ficticios ya estén en SQL Server**.

## Modelos elegidos

- **Documento:** cada servicio necesita recursos y configuración diferentes sin alterar una tabla relacional por cada atributo nuevo.
- **Grafo:** la recomendación de un servicio se calcula recorriendo estudiantes que comparten algún servicio, una pregunta más natural en un grafo que en múltiples uniones repetidas.
- **Columnas anchas:** la consulta más frecuente recupera eventos de un estudiante durante un mes; Cassandra prioriza la clave de partición y la ordenación de las fechas.

## Modelo de Cassandra

```text
PRIMARY KEY ((estudiante_id, periodo), fecha_evento, evento_id)
PARTICION: estudiante_id + periodo (por ejemplo EST-001, 2026-11)
CLUSTERING: fecha_evento DESC, evento_id ASC
```

Una consulta por estudiante y periodo localiza la partición; el rango de fechas se resuelve sobre el clustering. Consultas globales por tipo de evento o por nombre requerirían otra tabla diseñada para esa consulta. No se necesita clúster para esta práctica; se usa un nodo con replicación 1 solo en laboratorio.

## Persistencia y acceso

Cada nuevo gestor usa un volumen Docker diferente. MongoDB autentica en `admin`; Neo4j exige un usuario inicial; Cassandra se limita al entorno local, pero **el contenedor de laboratorio no configura autenticación CQL**, por lo que debe tratarse únicamente como práctica local. Los puertos nuevos se publican solo en `127.0.0.1` del equipo anfitrión.
