import dash #se importar dash
import dash_bootstrap_components as dbc #Se importa un complemento de dash
from dash import html, dcc # se importan complemnetos de dash


derecho = dbc.Container( # Contenedor para la sección de datos del proyecto en el lado derecho de la interfaz
    [
        html.Hr(),  # Línea horizontal
        html.H2('Datos del proyecto', style={'color':'White'}),  # Título de nivel 2 
        html.Hr(style={'color':'White'}),  # línea horizontal 
        html.Label('Nombre:', style={'color':'White'}),  # Etiqueta para el campo de entrada del nombre 
        dbc.Input(value="Nombre"),  # Input para colocar nombre
        html.Label('Localización:', style={'color':'White'}),  # Etiqueta para el campo de entrada de localización 
        dbc.Input(value="Localización"),  #  Input para colocar la localización c
        html.Label('Fecha Inicio:', style={'color':'White'}),  # Etiqueta para el campo de entrada de fecha de inicio 
        dbc.Input(value="Fecha", type="date"),  #  Input para colocar la fecha de inicio 
        html.Label('Fecha Fin:', style={'color':'White'}),  # Etiqueta para el campo de entrada de fecha de fin
        dbc.Input(value="Fecha", type="date"),  #  Input para colocar la fecha de fin
        html.Hr(),  # línea horizontal
            ]
)