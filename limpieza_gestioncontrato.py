import pandas as pd

def limpiar_datos_gestion_contrato(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()

    data_frame_limpio["TipoContrato"]=data_frame_limpio["TipoContrato"].astype("string").str.strip().str.lower()
    data_frame_limpio["EstadoContrato"]=data_frame_limpio["EstadoContrato"].astype("string").str.strip().str.lower()

    valores_esperados_tipo=["indefinido","fijo","prestacion de servicios","temporal"]
    data_frame_limpio["TipoContrato"]=data_frame_limpio["TipoContrato"].where(
            data_frame_limpio["TipoContrato"].isin(valores_esperados_tipo),
            pd.NA
        )

    valores_esperados_estado=["activo","finalizado","pendiente"]
    data_frame_limpio["EstadoContrato"]=data_frame_limpio["EstadoContrato"].where(
            data_frame_limpio["EstadoContrato"].isin(valores_esperados_estado),
            pd.NA
    )

    data_frame_limpio["IdContrato"]=pd.to_numeric(data_frame_limpio["IdContrato"])
    data_frame_limpio["Salario"]=pd.to_numeric(data_frame_limpio["Salario"])

    data_frame_limpio["FechaInicio"]=pd.to_datetime(data_frame_limpio["FechaInicio"])
    data_frame_limpio["FechaFin"]=pd.to_datetime(data_frame_limpio["FechaFin"])

    data_frame_limpio=data_frame_limpio[data_frame_limpio["IdContrato"]>0]
    data_frame_limpio=data_frame_limpio[data_frame_limpio["Salario"]>0]

    columnas_obligatorias=["IdContrato","TipoContrato","FechaInicio","FechaFin","Salario","EstadoContrato"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

    return data_frame_limpio