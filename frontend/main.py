import dash #Se importa dash
import dash_bootstrap_components as dbc #Se importa complementos de dash

from navegador.navegador import navegador # Se importa la funcion navegardor de la hoja de navegador
from derecho.derecho import derecho # Se importa la función derecho de la hoja derecho
from izquierdo.izquierdo import izquierdo # se importa la función derecho de la hoja derecho

layout = dbc.Container ([ #Se define el estilo de la aplicación, los campos que este tendra
    dbc.Row([ #Se crean 3 espacios para el layout de la aplización
        dbc.Col (navegador,md=12 , style={'background-color':'White'}), #Columna para la función navegador
        dbc.Col (izquierdo,md=8 , style={'background-color':'lightgray'}), #Columna para la función izquierdo
        dbc.Col (derecho,md=4 , style={'background-color':'lightblue'}) #Columna para la función derecho 
    ])

 ])