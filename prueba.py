###################################################
# ESTE MODULO ES SOLO PARA PROBAR FUNCIONALIDADES #
###################################################


from get_request import get_info
import datetime

#Consumiendo la API
response = get_info('https://api.gael.cloud/general/public/sismos')
#Se ordena en una lista de diccionarios las variables necesarias para la construcción
#de las tablas y el gráfico
response_ordenado = []
for i, item in enumerate(response, 1):
    response_ordenado.append({'slug': str(i), 'fecha':item['Fecha'],'profundidad':item['Profundidad'],
    'magnitud':item['Magnitud'], 'refGeografica':item['RefGeografica']})

lista_fechas = []
for i,item in enumerate(response_ordenado,1):
    lista_fechas.append({i:item['fecha']})

#Buscando el formato ideal para mostrar en el render
fecha = lista_fechas[0][1]
fecha_dt = datetime.datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
print(fecha_dt)
new_fecha = fecha_dt.strftime('  %d %b %Y\na las %H:%M:%S')
print(new_fecha)