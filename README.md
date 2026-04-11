# Proyecto Integrador - Contratación

## Módulo: Postulación

Este módulo corresponde al subproceso de **Postulación** dentro del proyecto integrador de **Contratación**.

### Funcionalidades implementadas

- simulación de datos sintéticos de postulación
- exportación de datos a formatos CSV y JSON
- limpieza del set de datos
- descripción exploratoria con Pandas
- transformación de datos con `query()`
- agrupación y resumen de datos con `groupby()`

### Historias de usuario desarrolladas

- **HU 1.3** Limpieza de set de datos (Postulación)
- **HU 2.3** Descripción exploratoria con Pandas (Postulación)
- **HU 3.3** Simulación y exportación de datos (Postulación)
- **HU 4.3** Transformación de datos con `query()` de Pandas (Postulación)
- **HU 5.3** Agrupación y resumen de datos (Postulación)

### Estructura del módulo

- `main.py`: genera el dataset sintético y exporta a CSV y JSON
- `simulacion.py`: crea registros simulados con errores controlados
- `limpieza.py`: limpia, corrige y normaliza el dataset
- `exploracion.py`: realiza análisis exploratorio del dataset limpio
- `transformacion.py`: aplica filtros con `query()`
- `resumen.py`: agrupa y resume los datos con `groupby()`

### Requisitos

- Python 3.x
- pandas
- numpy

### Ejecución

Ejecutar los archivos en el siguiente orden:

```bash
python main.py
python limpieza.py
python exploracion.py
python transformacion.py
python resumen.py
```
