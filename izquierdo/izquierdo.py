import dash #se importar dash
import dash_bootstrap_components as dbc #Se importa un complemento de dash
from dash import html, dcc # se importan complemnetos de dash
import dash_table #Se importa para generar tablas
import pandas as pd #Se importa pandas
 
tabla = {'': ['Numero de sondeos','Profundidad'], #Se crea la tabla de pronfundidad y numero de exploraiones
        'Categoria baja': ['3','6 metros'] , # Columna categoria baja
        'Categoria media': ['4','15 metros'],  # Columna categoria media
        'Categoria alta': ['4','25 metros'], # Columna categoria alta
        'Categoria Especial': ['5','30 metros']} # Columna categoria especial

df = pd.DataFrame(tabla) #se crea dataframe con la tabla


izquierdo = dbc.Container([ #Se crea el lado izquierdo de la aplicación 
    html.Hr(),  # Línea horizontal
    html.H1('DATOS DE LA ESTRUCTURA'),  # Título principal
    html.Hr(),  #línea horizontal
    html.Div([
        html.Label('Número de plantas de la estructura', style={'fontSize': '30px'}),  # Etiqueta para el número de pisos
        html.Hr(style={'color': 'lightgray'}),  # Línea horizontal con estilo
        dcc.Input(id='entradaPisos', value=1, type='number'),  # Entrada para el número de pisos
        html.Hr(style={'color': 'lightgray'}),  # línea horizontal con estilo
        html.Label(id='salidaPisos'),  # Etiqueta para mostrar el resultado
        html.Hr(),  # Línea horizontal      
        html.H3('NÚMERO MINIMO DE SONDEOS Y PROFUNDIDAD'), # Título para la tabla
        dash_table.DataTable(  # Tabla de datos
            id='tabla-datos', #Se nombra la tabla de datos
            columns=[{'name': col, 'id': col} for col in df.columns],  # Definir las columnas de la tabla
            data=df.to_dict('records'),  # Convertir DataFrame a formato compatible con la tabla
            editable=False  # No se permite que la tabla sea editable
        ),
        
        html.Hr(style={'color': 'lightgray'})  #línea horizontal al final
    ])
])

