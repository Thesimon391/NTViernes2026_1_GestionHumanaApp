import pandas as pd

def limpiar_datos_personas(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()

    data_frame_limpio["nombre"]=data_frame_limpio["nombre"].astype("string").str.strip().str.lower()
    data_frame_limpio["correo"]=data_frame_limpio["correo"].astype("string").str.strip().str.lower()

    valores_esperados_nombre=["juan manuel perez","juan david orozco", "david martinez manso","diego orlando perez", "pepito perez mendez"]
    data_frame_limpio["nombre"]=data_frame_limpio["nombre"].where(
            data_frame_limpio["nombre"].isin(valores_esperados_nombre),
            pd.NA
        )
    
    valores_esperados_correo=["juanchoma@gmail.com","juanchitodav@gmail.com","diebitmar@gmail.com","diegorlyspe@gmail.com","pepitopan@hotmail.com"]
    data_frame_limpio["correo"]=data_frame_limpio["correo"].where(
            data_frame_limpio["correo"].isin(valores_esperados_correo),
            pd.NA
    )

    
    data_frame_limpio["Id_cliente"]=pd.to_numeric(data_frame_limpio["Id_cliente"])
    data_frame_limpio["cedula"]=pd.to_numeric(data_frame_limpio["cedula"])
    data_frame_limpio["telefono"]=pd.to_numeric(data_frame_limpio["telefono"])


    data_frame_limpio=data_frame_limpio[data_frame_limpio["Id_cliente"]>0]
    data_frame_limpio=data_frame_limpio[data_frame_limpio["cedula"].astype(str).str.len()==10]
    data_frame_limpio=data_frame_limpio[data_frame_limpio["telefono"].astype(str).str.len()<=10]

    columnas_obligatorias=["Id_cliente","cedula","telefono","nombre", "correo"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

    return data_frame_limpio
