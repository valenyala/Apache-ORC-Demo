import pyarrow as pa
import pyarrow.orc as orc
import pandas as pd
import os

print("Creando datos de ejemplo")
datos = {
    'id_transaccion': list(range(1, 100001)),
    'usuario': ['usuario_' + str(i % 1000) for i in range(100000)],  # Repetición para demostrar compresión
    'producto': ['producto_' + str(i % 50) for i in range(100000)],
    'precio': [round(10 + (i % 100) * 0.5, 2) for i in range(100000)],
    'cantidad': [1 + (i % 5) for i in range(100000)],
    'timestamp': pd.date_range('2024-01-01', periods=100000, freq='1min'),
    'categoria': ['Electrónica', 'Ropa', 'Hogar', 'Deportes', 'Libros'] * 20000
}

df = pd.DataFrame(datos)
print(f"✓ Dataset creado: {len(df):,} filas, {len(df.columns)} columnas")
print(f"  Columnas: {list(df.columns)}")
print(f"\nPrimeras 3 filas:")
print(df.head(3))

print("Escribiendo archivo ORC")

# Convertir a Arrow Table (necesario para ORC)
table = pa.Table.from_pandas(df)

# Escribir con diferentes configuraciones
configs = {
    'sin_compresion.orc': {'compression': "UNCOMPRESSED"},
    'con_zlib.orc': {'compression': 'ZLIB'},
    'con_snappy.orc': {'compression': 'SNAPPY'},
    'con_lz4.orc': {'compression': 'LZ4'},
}

print("\nEscribiendo archivos con diferentes compresiones...")
for filename, config in configs.items():
    orc.write_table(
        table, 
        filename,
        compression=config['compression'],
        compression_strategy="COMPRESSION",
        stripe_size=128 * 1024,  # se usa este tamaño para generar mas de un stripe
        compression_block_size=256 * 1024,  # 256 KB (default)
    )
    size_mb = os.path.getsize(filename) / (1024 * 1024)
    print(f"  ✓ {filename}: {size_mb:.2f} MB")


