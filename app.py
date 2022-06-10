from flask import Flask, render_template
from get_request import get_info
import datetime

app = Flask(__name__)

#Consumiendo la API
response = get_info('https://api.gael.cloud/general/public/sismos')
#Se ordena en una lista de diccionarios las variables necesarias para la construcción
#de las tablas y el gráfico
response_ordenado = []
for i, item in enumerate(response, 1):
    response_ordenado.append({'slug': str(i), 'fecha':(datetime.datetime.strptime(item['Fecha'], '%Y-%m-%d %H:%M:%S')).strftime('%d %b %Y - %H:%M:%S'),
    'profundidad':item['Profundidad'], 'magnitud':item['Magnitud'], 'refGeografica':item['RefGeografica']})

#Se ordena en una lista de tuplas los valores que iran en abscisa y ordenada
grafico_data = []
for item in response_ordenado:
    grafico_data.append((item['fecha'],float(item['magnitud'].split(' ')[0])))
#Se separan los valores de abscisa o ordenada para cargar en el template
labels = [row[0] for row in grafico_data]
values = [row[1] for row in grafico_data]
#Método que renderiza el consumo de la API
@app.route('/')
def index():
    return render_template('index.html', data = response_ordenado, labels = labels, values = values)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000,debug=True)