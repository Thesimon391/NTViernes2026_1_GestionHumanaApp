#simulacion de datos de la tabla personas en python

import random

def generar_candidatos(numeroCandidatos):

    listaNombre=["juan manuel perez","juan david orozco", "david martinez manso","diego orlando perez", "pepito perez mendez"]
    listaCorreo=["juanchoma@gmail.com","juanchitodav@gmail.com","diebitmar@gmail.com","diegorlyspe@gmail.com","pepitopan@hotmail.com"]
    listaTelefono=["3125678909","3215467687","3116547896","3238245673","3029876543"]
    listaCedula=["1004587965","50956874","1008698541","1067874698","1045897452"]
    listaIdPersona=[]

    candidatos=[]
    for i in range(numeroCandidatos):
        pass
    candidatos={
    "Nombre":random.choice(listaNombre),
    "Correo":random.choice(listaCorreo),
    "Telefono":random.randint(0,200),
    "Cedula":random.randint(0,10),
    "Id_cliente":random.randint(0,100)
    }
    candidatos.append(candidatos)
    return candidatos