#simulando datos de una tabla en PYTHON

import random
from datetime import datetime, timedelta

def generar_gestion(num_empleados):
    listaRegistroEmpleado = ["Jorge","Camilo","yeison","alvaro","Daniel"]

    listaContrato = ["R004523", "F155135", "V445033", "L0055158", "R0025155"]
    
    fechaInicioContrato=datetime(2025,3,11)
    fechaFinalizaContrato=datetime(2026,2,15)
    gestion = []

    for i in range(num_empleados):
        fecha=fechaInicioContrato + timedelta(days=random).randint(0,60)
        num_empleados={
            "id": random.randint(1, 2000),
            "nombre": random.choice(listaRegistroEmpleado),
            ""
        }


