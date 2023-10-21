import dash # Se importa dash
import dash_bootstrap_components as dbc #se importa complementos de dash
from dash.dependencies import Input, Output #se importa complementos de dash
import math # Se importa math

app = dash.Dash(__name__,external_stylesheets=[ dbc.themes.BOOTSTRAP]) # Se inicializa la aplicación Dash con el tema Bootstrap
server = app.server

from frontend.main import layout #Se importa la función layout de la hoja main
 
app.layout = layout # Establece el diseño de la aplicación como el layout importado

@app.callback( # Definir la función de devolución de llamada para actualizar 'salidaPisos' basado en 'entradaPisos'
    Output('salidaPisos', 'children'),  # La salida es el contenido de 'salidaPisos'
    Input('entradaPisos', 'value')  # La entrada es el valor de 'entradaPisos'
)
def numeroPisos(entradaPisos): # Se crea función para determinar el número de exploracions y profundidad
    if 1 <= entradaPisos <= 3: # de 1 a 3 pisos
        categoria = 'categoria baja' #Se define la categoria 
        cargasMaximas = 'menores a 800 KN' # Se define las cargas maximas de servicio 
        exploraciones = '3' # Se define el número de exploraciones
        profundidad ='6 metros' # Se define la profundidad minima para las exploraciones 
    elif 4 <= entradaPisos <= 10:
        categoria = 'categoria media' #Se define la categoria 
        cargasMaximas = 'entre 801 y 4000 KN' # Se define las cargas maximas de servicio 
        exploraciones = '4' # Se define el número de exploraciones
        profundidad ='15 metros' # Se define la profundidad minima para las exploraciones 
    elif 11 <= entradaPisos <= 20:
        categoria = 'categoria alta' #Se define la categoria 
        cargasMaximas = 'entre 4001 y 8000 KN' # Se define las cargas maximas de servicio 
        exploraciones = '4' # Se define el número de exploraciones
        profundidad ='25 metros' # Se define la profundidad minima para las exploraciones 
    elif entradaPisos >20:
        categoria = 'categoria especial' #Se define la categoria 
        cargasMaximas = 'mayores a 4000 KN' # Se define las cargas maximas de servicio 
        exploraciones = '5' # Se define el número de exploraciones
        profundidad ='30 metros' # Se define la profundidad minima para las exploraciones 
    else: 
        mensaje = 'Ingrese un dato valido' # Se solcita ingresar un dato valdido 
    mensaje = f'EDIFICIO: {categoria}, las cargas máximas de servicio en las columnas son {cargasMaximas}.\n' # Mensaje de tipo de estructura
    mensaje += f'La cantidad mínima de exploraciones son: {exploraciones}, y la profundidad mínima es {profundidad}.' # Mensaje  de la cantidad de exploraciones y profundifda
 
    return mensaje # Se muestra el mensaje



if __name__ == '__main__': # script principal, ejecuta la aplicación
    app.run_server(debug=True)  # Ejecuta la aplicación en modo de depuración
