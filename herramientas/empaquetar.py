#!/usr/bin/env python3
"""Crea dos ZIP seguros y reproducibles sin leer .env ni carpetas antiguas."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT.parent / "output"
OUT.mkdir(exist_ok=True)
ACTIVIDAD = "Magos_Carlos_NoSQL_Practicas_CampusCloud"
INTEGRACION = "CampusCloud_UnidadII_Integracion"

PERMITIDAS = [
    ROOT / ".gitignore",
    ROOT / "README.md",
    ROOT / "docker" / "compose.yaml",
    ROOT / "docker" / ".env.example",
    *sorted((ROOT / "mongodb").glob("*.js")),
    *sorted((ROOT / "neo4j").glob("*.cypher")),
    *sorted((ROOT / "cassandra").glob("*.cql")),
    *sorted((ROOT / "docs").glob("*.md")),
    ROOT / "seguridad" / "README.md",
    ROOT / "reportes" / "unidad-ii" / "LEEME.md",
    ROOT / "tools" / "generar_reporte.py",
    ROOT / "tools" / "empaquetar.py",
    *sorted(p for p in (ROOT / "evidencias" / "unidad-ii").rglob("*") if p.is_file()),
]

def seguro(path):
    rel = path.relative_to(ROOT)
    if path.name == ".env" or ".git" in rel.parts or "node_modules" in rel.parts:
        raise ValueError(f"Archivo prohibido en ZIP: {rel}")
    if path.suffix.lower() in {".tar", ".pem", ".key", ".pfx"}:
        raise ValueError(f"Archivo no permitido: {rel}")
    return rel

def ruta_actividad(rel):
    p = rel.parts
    if p[0] == "docker":
        return Path("01-configuracion") / Path(*p[1:])
    if p[0] == "mongodb":
        return Path("02-mongodb") / Path(*p[1:])
    if p[0] == "neo4j":
        return Path("03-neo4j") / Path(*p[1:])
    if p[0] == "cassandra":
        return Path("04-columnas-anchas") / Path(*p[1:])
    if p[0] == "evidencias":
        return Path("05-evidencias") / Path(*p[2:])
    if p[0] == "docs":
        return Path("documentacion") / Path(*p[1:])
    if p[0] == "seguridad":
        return Path("documentacion") / "seguridad.md"
    if p[0] == "reportes":
        return Path("documentacion") / "reporte-LEEME.md"
    if p[0] == "tools":
        return Path("herramientas") / Path(*p[1:])
    return rel

def crear(nombre, destino):
    archivo = OUT / f"{nombre}.zip"
    with ZipFile(archivo, "w", ZIP_DEFLATED, compresslevel=8) as z:
        for source in PERMITIDAS:
            rel = seguro(source)
            if not source.exists():
                raise FileNotFoundError(source)
            z.write(source, arcname=str(Path(nombre) / destino(rel)))
    return archivo

for arch in [
    crear(ACTIVIDAD, ruta_actividad),
    crear(INTEGRACION, lambda rel: rel),
]:
    with ZipFile(arch) as z:
        listado = z.namelist()
        assert not any(s.endswith("/.env") for s in listado)
        capturas = [s for s in listado if s.lower().endswith((".png", ".jpg", ".jpeg"))]
        print(f"{arch.name}: {len(listado)} archivos, {len(capturas)} capturas reales")
        if not capturas:
            print("AVISO: Faltan las capturas reales que exige el maestro.")
