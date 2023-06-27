from datetime import datetime


# Obtener la fecha actual
fecha_actual = datetime.now()
# Convertir la fecha en un formato legible para la web
fecha_formateada = fecha_actual.strftime('%d/%m/%Y %H:%M:%S')

print(fecha_formateada)