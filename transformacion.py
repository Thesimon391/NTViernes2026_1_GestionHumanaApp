import pandas as pd

def transformar_postulaciones(ruta_archivo="data/postulacion_limpio.csv"):
    df = pd.read_csv(ruta_archivo)

    print("=== TRANSFORMACIÓN DE DATOS CON query() ===")

    # 1. Postulaciones aceptadas
    aceptadas = df.query("estado == 'aceptado'")
    print("\n1. Postulaciones aceptadas")
    print(aceptadas)

    # 2. Postulaciones en revisión
    en_revision = df.query("estado == 'en revisión'")
    print("\n2. Postulaciones en revisión")
    print(en_revision)

    # 3. Postulaciones por LinkedIn
    linkedin = df.query("medio_postulacion == 'linkedin'")
    print("\n3. Postulaciones por LinkedIn")
    print(linkedin)

    # 4. Postulaciones con nivel universitario
    universitarios = df.query("nivel_estudios == 'universitario'")
    print("\n4. Postulaciones con nivel universitario")
    print(universitarios)

    # 5. Postulaciones para una vacante específica
    vacante_1 = df.query("id_vacante == 1")
    print("\n5. Postulaciones para la vacante 1")
    print(vacante_1)

    # 6. Filtro combinado
    filtro_combinado = df.query("estado == 'aceptado' and medio_postulacion == 'linkedin'")
    print("\n6. Postulaciones aceptadas desde LinkedIn")
    print(filtro_combinado)

    return {
        "aceptadas": aceptadas,
        "en_revision": en_revision,
        "linkedin": linkedin,
        "universitarios": universitarios,
        "vacante_1": vacante_1,
        "filtro_combinado": filtro_combinado
    }


if __name__ == "__main__":
    transformar_postulaciones()