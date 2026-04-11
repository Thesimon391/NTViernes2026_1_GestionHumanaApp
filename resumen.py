import pandas as pd

def resumir_postulaciones(ruta_archivo="data/postulacion_limpio.csv"):
    try:
        df = pd.read_csv(ruta_archivo)
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta_archivo}")
        return None

    print("=== AGRUPACIÓN Y RESUMEN DE DATOS ===")

    # 1. Agrupación por estado
    if "estado" in df.columns:
        resumen_estado = (
            df.groupby("estado")
            .size()
            .reset_index(name="cantidad")
            .sort_values("cantidad", ascending=False)
        )
        print("\n1. Postulaciones por estado")
        print(resumen_estado)
    else:
        resumen_estado = pd.DataFrame()

    # 2. Agrupación por medio de postulación
    if "medio_postulacion" in df.columns:
        resumen_medio = (
            df.groupby("medio_postulacion")
            .size()
            .reset_index(name="cantidad")
            .sort_values("cantidad", ascending=False)
        )
        print("\n2. Postulaciones por medio de postulación")
        print(resumen_medio)
    else:
        resumen_medio = pd.DataFrame()

    # 3. Agrupación por nivel de estudios
    if "nivel_estudios" in df.columns:
        resumen_nivel = (
            df.groupby("nivel_estudios")
            .size()
            .reset_index(name="cantidad")
            .sort_values("cantidad", ascending=False)
        )
        print("\n3. Postulaciones por nivel de estudios")
        print(resumen_nivel)
    else:
        resumen_nivel = pd.DataFrame()

    # 4. Agrupación por vacante
    if "id_vacante" in df.columns:
        resumen_vacante = (
            df.groupby("id_vacante")
            .size()
            .reset_index(name="cantidad")
            .sort_values("id_vacante")
        )
        print("\n4. Postulaciones por vacante")
        print(resumen_vacante)
    else:
        resumen_vacante = pd.DataFrame()

    # 5. Agrupación combinada: estado y medio de postulación
    if "estado" in df.columns and "medio_postulacion" in df.columns:
        resumen_estado_medio = (
            df.groupby(["estado", "medio_postulacion"])
            .size()
            .reset_index(name="cantidad")
            .sort_values("cantidad", ascending=False)
        )
        print("\n5. Postulaciones por estado y medio de postulación")
        print(resumen_estado_medio)
    else:
        resumen_estado_medio = pd.DataFrame()

    # 6. Agrupación por postulante
    if "id_postulante" in df.columns:
        resumen_postulante = (
            df.groupby("id_postulante")
            .size()
            .reset_index(name="cantidad")
            .sort_values("cantidad", ascending=False)
        )
        print("\n6. Postulaciones por postulante")
        print(resumen_postulante.head(10))
    else:
        resumen_postulante = pd.DataFrame()

    return {
        "resumen_estado": resumen_estado,
        "resumen_medio": resumen_medio,
        "resumen_nivel": resumen_nivel,
        "resumen_vacante": resumen_vacante,
        "resumen_estado_medio": resumen_estado_medio,
        "resumen_postulante": resumen_postulante
    }


if __name__ == "__main__":
    resumir_postulaciones()