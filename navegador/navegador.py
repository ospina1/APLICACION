import dash #se importa dash
import dash_bootstrap_components as dbc #Se importa complementos de dash
from dash import html #Se importa complementos de dash


navegador = dbc.Container([ # Contenedor para la sección de información en el navegador
    html.Hr(),  # Línea horizontal
    html.H2('NÚMERO DE EXPLORACIONES GEOTECNICAS'),  # Título 
    html.Hr(),  # línea horizontal
    html.H2('NSR 10'),  # Título 
    html.Hr(),  # línea horizontal
    html.H4('''Este aplicativo te permite calcular el numero de sondeos y su profundidad,'''),  # Texto de nivel 4
    html.H4('''con base en el área del proyecto, la cantidad de niveles y su carga.'''),  # Texto de nivel 4
    html.Hr()  # Línea horizontal
])