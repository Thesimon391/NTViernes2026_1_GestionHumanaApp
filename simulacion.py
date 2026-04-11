import random
from datetime import datetime, timedelta

def generar_simulacion(cantidad):
    estados = ["postulado", "en revisión", "entrevista", "aceptado", "rechazado"]
    medios = ["linkedin", "computrabajo", "facebook", "pagina web", "referencia"]
    niveles = ["secundaria", "tecnico", "universitario", "maestria"]

    simulaciones = []

    for i in range(cantidad):
        fecha_base = datetime.now() - timedelta(days=random.randint(1, 60))

        postulacion = {
            "id": i + 1,
            "fecha_postulacion": fecha_base.strftime("%Y-%m-%d"),
            "estado": random.choice(estados),
            "medio_postulacion": random.choice(medios),
            "nivel_estudios": random.choice(niveles),
            "id_postulante": random.randint(1, 20),
            "id_vacante": random.randint(1, 10)
        }

        probabilidadError = random.random()

        if probabilidadError < 0.1:
            postulacion["estado"] = " " + postulacion["estado"] + " "
        elif probabilidadError < 0.2:
            postulacion["medio_postulacion"] = "linked in"
        elif probabilidadError < 0.3:
            postulacion["id"] = random.choice([-1, 0, -5])
        elif probabilidadError < 0.4:
            postulacion["fecha_postulacion"] = fecha_base.strftime("%d/%m")
        elif probabilidadError < 0.5:
            postulacion["nivel_estudios"] = None
        elif probabilidadError < 0.6:
            postulacion["estado"] = "EN REVISION"
        elif probabilidadError < 0.7:
            postulacion["id_postulante"] = None
        elif probabilidadError < 0.8:
            postulacion["id_vacante"] = 0

        simulaciones.append(postulacion)

    if len(simulaciones) >= 2:
        simulaciones.append(simulaciones[0].copy())

    return simulaciones