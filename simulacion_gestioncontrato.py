import random
from datetime import datetime, timedelta

def generar_contratos(numero_contratos):

    tipos_contrato = ["Indefinido", "Temporal", "Obra", "Practicante"]
    estados = ["Activo", "Finalizado", "Suspendido"]
    salarios = [1200000, 1500000, 2000000, 2500000, 3000000]

    fecha_inicio_base = datetime(2026, 1, 1)

    contratos = []

    for i in range(numero_contratos):

        fecha_inicio = fecha_inicio_base + timedelta(days=random.randint(0, 60))
        fecha_fin = fecha_inicio + timedelta(days=random.randint(30, 365))

        contrato = {
            "id_contrato": random.randint(1, 5000),
            "tipo_contrato": random.choice(tipos_contrato),
            "fecha_inicio": fecha_inicio.strftime("%Y-%m-%d"),
            "fecha_fin": fecha_fin.strftime("%Y-%m-%d"),
            "salario": random.choice(salarios),
            "estado_contrato": random.choice(estados),
            "id_empleado": random.randint(1, 5000)
        }

        contratos.append(contrato)

    return contratos

    lista = generar_contratos(5)

for contrato in lista:
    print(contrato)