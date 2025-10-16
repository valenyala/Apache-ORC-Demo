# Demo Lectura y Escritura Apache ORC

## Instrucciones:
 - instalar pyarrow y pandas como dependencias
 - Ejecutar primero escritura.py para obtener los archivos .orc
 - Ejecutar lectura_datos.py y lectura_metadatos.py para analizar estructura interna y velocidad de lectura.
Creando datos de ejemplo
✓ Dataset creado: 100,000 filas, 7 columnas
  Columnas: ['id_transaccion', 'usuario', 'producto', 'precio', 'cantidad', 'timestamp', 'categoria']

Primeras 3 filas:
   id_transaccion    usuario  ...           timestamp    categoria
0               1  usuario_0  ... 2024-01-01 00:00:00  Electrónica
1               2  usuario_1  ... 2024-01-01 00:01:00         Ropa
2               3  usuario_2  ... 2024-01-01 00:02:00        Hogar

[3 rows x 7 columns]
Escribiendo archivo ORC

Escribiendo archivos con diferentes compresiones...
  ✓ sin_compresion.orc: 3.68 MB
  ✓ con_zlib.orc: 0.04 MB
  ✓ con_snappy.orc: 0.24 MB
  ✓ con_lz4.orc: 0.04 MB
Leyendo archivo ORC completo
✓ Archivo leído: 100,000 filas

Primeras 3 filas leídas:
   id_transaccion    usuario  ...           timestamp    categoria
0               1  usuario_0  ... 2024-01-01 00:00:00  Electrónica
1               2  usuario_1  ... 2024-01-01 00:01:00         Ropa
2               3  usuario_2  ... 2024-01-01 00:02:00        Hogar

[3 rows x 7 columns]
Leyendo solo columnas específicas

 TIEMPOS DE LECTURA:
  Todas las columnas : 0.0077s
  Solo 2 columnas: 0.0021s
  Mejora: 3.74x más rápido
Explorando metadata del archivo ORC

INFORMACIÓN GENERAL:
  - Número de filas: 100,000
  - Número de stripes: 2
  - Tamaño archivo: 0.24 MB

ESQUEMA:
  id_transaccion: int64
usuario: string
producto: string
precio: double
cantidad: int64
timestamp: timestamp[ns]
categoria: string

STRIPES:
  Stripe 0:
    - Offset: 72704 bytes
    - Filas: 72,704
  Stripe 1:
    - Offset: 27296 bytes
    - Filas: 27,296
