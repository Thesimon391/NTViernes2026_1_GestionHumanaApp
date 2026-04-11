from simulacion import generar_simulacion
import pandas as pd
import os

def main():
    os.makedirs("data", exist_ok=True)

    # Generar datos simulados
    datos_simulados = generar_simulacion(1000)
    df = pd.DataFrame(datos_simulados)

    # Rutas de salida
    ruta_csv = "data/postulacion_sucio.csv"
    ruta_json = "data/postulacion_sucio.json"

    # Exportar a CSV y JSON
    df.to_csv(ruta_csv, index=False)
    df.to_json(ruta_json, orient="records", indent=4, force_ascii=False)

    print("Archivo CSV generado:", ruta_csv)
    print("Archivo JSON generado:", ruta_json)
    print("Cantidad de registros generados:", len(df))
    print("\nPrimeras filas del dataset original:")
    print(df.head())

    # Recargar archivos exportados
    df_csv = pd.read_csv(ruta_csv)
    df_json = pd.read_json(ruta_json)

    print("\n=== VERIFICACIÓN DE RECARGA ===")
    print("Dimensiones CSV:", df_csv.shape)
    print("Dimensiones JSON:", df_json.shape)

    print("\nColumnas originales:")
    print(df.columns.tolist())

    print("\nColumnas CSV:")
    print(df_csv.columns.tolist())

    print("\nColumnas JSON:")
    print(df_json.columns.tolist())

    # Validar estructura
    misma_estructura_csv = df.columns.tolist() == df_csv.columns.tolist()
    misma_estructura_json = df.columns.tolist() == df_json.columns.tolist()

    print("\n¿CSV conserva la estructura?:", misma_estructura_csv)
    print("¿JSON conserva la estructura?:", misma_estructura_json)

if __name__ == "__main__":
    main()