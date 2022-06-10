
#Función que cambia las siglas para mejor entendimiento del usuario
def cambiar(string):
    puntos_cardinales = {'O':'Oeste','S':'Sur','E':'Este','N':'Norte',
                    'NO':'Noroeste','SO':'Suroeste','NE':'Noreste','SE':'Sureste'}
    puntos = ['O','S','N','E','NO','SO','NE','SE']

    for item in puntos:
        if item in string:
            new_string = string.replace(item,puntos_cardinales[item])

    return new_string


if __name__ == '__main__':
    print(cambiar('70 km al O de Tongoy'))

