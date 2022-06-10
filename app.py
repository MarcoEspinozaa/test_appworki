from flask import Flask, render_template
from get_request import get_info

app = Flask(__name__)

#Consumiendo la API
response = get_info('https://api.gael.cloud/general/public/sismos')
response_ordenado = []
for item in response:
    response_ordenado.append({'fecha':item['Fecha'],'profundidad':item['Profundidad'],
    'magnitud':item['Magnitud'], 'refGeografica':item['RefGeografica']})

@app.route('/')
def index():
    return render_template('index.html', data = response_ordenado)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000,debug=True)