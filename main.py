from get_request import get_info


#Muestra la data en consola.
response = get_info('https://api.gael.cloud/general/public/sismos')
#print(response)

response_ordenado = []
for item in response:
    response_ordenado.append({'fecha':item['Fecha'],'profundidad':item['Profundidad'],
    'magnitud':item['Magnitud'], 'refGeografica':item['RefGeografica']})

print(response_ordenado)