from simulacion import generar_simulacion
import pandas as pd
import os

os.makedirs("data", exist_ok=True)

datos_simulados = generar_simulacion(20)
df = pd.DataFrame(datos_simulados)

df.to_csv("data/postulacion_sucio.csv", index=False)

print("Archivo generado: data/postulacion_sucio.csv")
print("Cantidad de registros generados:", len(df))
print(df.head())