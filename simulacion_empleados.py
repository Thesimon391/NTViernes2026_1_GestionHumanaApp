import random
from datetime import datetime,timedelta

def generar_servicios(creacionEmpleados):

    listaNombres=["jose perez","esteban dido","pepito perez","cesar gaviria","fido gutierrez"]
    listaCargos=["Gerente area", "Servicios varios", "Supervisor", "Comunit manager", "Contratista"]
    listaDepartamentos=["DPtecnologia", "DPadministrativo", "DPaseo","DPventas","DPatencioncliente"]
    listaSalarioBase=[1051654,1654654,231854345,520000,2552211]
    fechaIngreso=datetime(2026,1,1)

    servicios=[]
    for _ in range(creacionEmpleados):

        fecha=fechaIngreso+timedelta(days=random.randint(0,60))

        servicio={
            "id_empleados": random.randint(0, 5000),
            "nombre": random.choice(listaNombres),
            "cargo": random.choice(listaCargos),
            "departamento": random.choice(listaDepartamentos),
            "salario": random.choice(listaSalarioBase),
            "fecha": fecha.strftime("%Y/%m%d")
        }
        servicios.append(servicio)
    return servicios 
