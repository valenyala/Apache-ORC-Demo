import pyarrow.orc as orc
import os
print("Explorando metadata del archivo ORC")

with open('con_snappy.orc', 'rb') as f:
    orc_reader = orc.ORCFile(f)
    
    print(f"\nINFORMACIÓN GENERAL:")
    print(f"  - Número de filas: {orc_reader.nrows:,}")
    print(f"  - Número de stripes: {orc_reader.nstripes}")
    print(f"  - Tamaño archivo: {os.path.getsize('con_snappy.orc') / (1024*1024):.2f} MB")
    
    print(f"\nESQUEMA:")
    print(f"  {orc_reader.schema}")
    
    print(f"\nSTRIPES:")
    for i in range(orc_reader.nstripes):
        print(f"  Stripe {i}:")
        print(f"    - Offset: {orc_reader.read_stripe(i).num_rows} bytes")
        print(f"    - Filas: {orc_reader.read_stripe(i).num_rows:,}")
