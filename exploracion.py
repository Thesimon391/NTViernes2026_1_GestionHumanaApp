import pandas as pd

def explorar_postulaciones(ruta_archivo="data/postulacion_limpio.csv"):
    try:
        df = pd.read_csv(ruta_archivo)
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta_archivo}")
        return

    print("=== EXPLORACIÓN DEL DATASET DE POSTULACIÓN ===")

    print("\n1. Primeras filas")
    print(df.head())

    print("\n2. Dimensiones")
    print(f"Filas: {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")

    print("\n3. Nombres de columnas")
    print(df.columns.tolist())

    print("\n4. Información general")
    df.info()

    print("\n5. Tipos de datos")
    print(df.dtypes)

    print("\n6. Valores nulos")
    print(df.isnull().sum())

    print("\n7. Duplicados")
    print(df.duplicated().sum())

    print("\n8. Estadísticas descriptivas")
    print(df.describe(include="all"))

    if "id" in df.columns:
        print("\n9. IDs únicos")
        print(df["id"].nunique())

    if "estado" in df.columns:
        print("\n10. Frecuencia por estado")
        print(df["estado"].value_counts())

    if "medio_postulacion" in df.columns:
        print("\n11. Frecuencia por medio de postulación")
        print(df["medio_postulacion"].value_counts())

    if "nivel_estudios" in df.columns:
        print("\n12. Frecuencia por nivel de estudios")
        print(df["nivel_estudios"].value_counts())

    if "id_vacante" in df.columns:
        print("\n13. Postulaciones por vacante")
        print(df["id_vacante"].value_counts().sort_index())

    if "id_postulante" in df.columns:
        print("\n14. Postulaciones por postulante")
        print(df["id_postulante"].value_counts().head(10))

    if "fecha_postulacion" in df.columns:
        print("\n15. Rango de fechas de postulación")
        fechas = pd.to_datetime(df["fecha_postulacion"], errors="coerce")
        print("Fecha mínima:", fechas.min())
        print("Fecha máxima:", fechas.max())


if __name__ == "__main__":
    explorar_postulaciones()