import pyarrow.orc as orc
import time

print("Leyendo archivo ORC completo")

with open('con_snappy.orc', 'rb') as f:
    orc_reader = orc.ORCFile(f)
    tabla_leida = orc_reader.read()
    df_leido = tabla_leida.to_pandas()

print(f"✓ Archivo leído: {len(df_leido):,} filas")
print(f"\nPrimeras 3 filas leídas:")
print(df_leido.head(3))


print("Leyendo solo columnas específicas")
# Leer TODAS las columnas
start = time.time()
with open('con_snappy.orc', 'rb') as f:
    tabla_completa = orc.ORCFile(f).read()
tiempo_completo = time.time() - start

# Leer SOLO 2 columnas
start = time.time()
with open('con_snappy.orc', 'rb') as f:
    tabla_parcial = orc.ORCFile(f).read(columns=['usuario', 'precio'])
tiempo_parcial = time.time() - start

print(f"\n TIEMPOS DE LECTURA:")
print(f"  Todas las columnas : {tiempo_completo:.4f}s")
print(f"  Solo 2 columnas: {tiempo_parcial:.4f}s")
print(f"  Mejora: {tiempo_completo/tiempo_parcial:.2f}x más rápido")

