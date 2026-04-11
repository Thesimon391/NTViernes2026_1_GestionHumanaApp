import pandas as pd

def limpiar_postulaciones(
    ruta_entrada="data/postulacion_sucio.csv",
    ruta_salida="data/postulacion_limpio.csv"
):
    try:
        df = pd.read_csv(ruta_entrada)
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta_entrada}")
        return None

    print("=== DATASET ORIGINAL ===")
    print(df.head())
    print("\nDimensiones originales:", df.shape)

    # Normalizar nombres de columnas
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Limpiar texto: espacios y minúsculas
    columnas_texto = ["estado", "medio_postulacion", "nivel_estudios"]
    for col in columnas_texto:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.lower()

    # Corregir valores inconsistentes
    if "medio_postulacion" in df.columns:
        df["medio_postulacion"] = df["medio_postulacion"].replace({
            "linked in": "linkedin",
            "pagina web": "página web",
            "facebook ": "facebook"
        })

    if "estado" in df.columns:
        df["estado"] = df["estado"].replace({
            "en revision": "en revisión",
            "aceptado ": "aceptado"
        })

    # Convertir columnas numéricas
    for col in ["id", "id_postulante", "id_vacante"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Eliminar IDs inválidos
    if "id" in df.columns:
        df = df[df["id"] > 0]

    if "id_postulante" in df.columns:
        df = df[df["id_postulante"].notna()]
        df = df[df["id_postulante"] > 0]

    if "id_vacante" in df.columns:
        df = df[df["id_vacante"] > 0]

    # Tratar nulos en nivel de estudios
    if "nivel_estudios" in df.columns:
        df["nivel_estudios"] = df["nivel_estudios"].replace(["none", "nan"], pd.NA)
        df["nivel_estudios"] = df["nivel_estudios"].fillna("no especificado")

    # Limpiar fechas
    if "fecha_postulacion" in df.columns:
      df["fecha_postulacion"] = pd.to_datetime(df["fecha_postulacion"], errors="coerce")
      df = df[df["fecha_postulacion"].notna()]
      df["fecha_postulacion"] = df["fecha_postulacion"].dt.strftime("%Y-%m-%d")

    # Eliminar duplicados
    df = df.drop_duplicates()

    print("\n=== DATASET LIMPIO ===")
    print(df.head())
    print("\nDimensiones finales:", df.shape)
    print("\nValores nulos:")
    print(df.isnull().sum())

    # Guardar archivo limpio
    df.to_csv(ruta_salida, index=False)
    print(f"\nArchivo limpio guardado en: {ruta_salida}")

    return df


if __name__ == "__main__":
    limpiar_postulaciones()