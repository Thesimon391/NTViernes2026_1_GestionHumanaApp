import pandas as pd

def transformar_postulaciones(ruta_archivo="data/postulacion_limpio.csv"):
    try:
        df = pd.read_csv(ruta_archivo)
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta_archivo}")
        return None

    print("=== TRANSFORMACIÓN DE DATOS CON query() ===")

    # 1. Postulaciones aceptadas
    aceptadas = df.query("estado == 'aceptado'")
    print("\n1. Postulaciones aceptadas")
    print("Cantidad:", len(aceptadas))
    print(aceptadas)
    print("Validación:", (aceptadas["estado"] == "aceptado").all() if not aceptadas.empty else True)

    # 2. Postulaciones en revisión
    en_revision = df.query("estado == 'en revisión'")
    print("\n2. Postulaciones en revisión")
    print("Cantidad:", len(en_revision))
    print(en_revision)
    print("Validación:", (en_revision["estado"] == "en revisión").all() if not en_revision.empty else True)

    # 3. Postulaciones por LinkedIn
    linkedin = df.query("medio_postulacion == 'linkedin'")
    print("\n3. Postulaciones por LinkedIn")
    print("Cantidad:", len(linkedin))
    print(linkedin)
    print("Validación:", (linkedin["medio_postulacion"] == "linkedin").all() if not linkedin.empty else True)

    # 4. Postulaciones con nivel universitario
    universitarios = df.query("nivel_estudios == 'universitario'")
    print("\n4. Postulaciones con nivel universitario")
    print("Cantidad:", len(universitarios))
    print(universitarios)
    print("Validación:", (universitarios["nivel_estudios"] == "universitario").all() if not universitarios.empty else True)

    # 5. Postulaciones para una vacante específica
    vacante_1 = df.query("id_vacante == 1")
    print("\n5. Postulaciones para la vacante 1")
    print("Cantidad:", len(vacante_1))
    print(vacante_1)
    print("Validación:", (vacante_1["id_vacante"] == 1).all() if not vacante_1.empty else True)

    # 6. Filtro combinado
    filtro_combinado = df.query("estado == 'aceptado' and medio_postulacion == 'linkedin'")
    print("\n6. Postulaciones aceptadas desde LinkedIn")
    print("Cantidad:", len(filtro_combinado))
    print(filtro_combinado)
    print(
        "Validación:",
        (
            (filtro_combinado["estado"] == "aceptado") &
            (filtro_combinado["medio_postulacion"] == "linkedin")
        ).all() if not filtro_combinado.empty else True
    )

    # 7. Filtro con OR
    proceso_activo = df.query("estado == 'en revisión' or estado == 'entrevista'")
    print("\n7. Postulaciones en proceso activo")
    print("Cantidad:", len(proceso_activo))
    print(proceso_activo)
    print(
        "Validación:",
        proceso_activo["estado"].isin(["en revisión", "entrevista"]).all() if not proceso_activo.empty else True
    )

    return {
        "aceptadas": aceptadas,
        "en_revision": en_revision,
        "linkedin": linkedin,
        "universitarios": universitarios,
        "vacante_1": vacante_1,
        "filtro_combinado": filtro_combinado,
        "proceso_activo": proceso_activo
    }


if __name__ == "__main__":
    transformar_postulaciones()