# Main dashboard screen

# importing libraries
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

# dash app
app = dash.Dash(__name__)

# Dash layout
app.layout = html.Div(
    children=[
        html.H1(
            children='Spotify Analysis'
        ),

        html.Div(
            children='''
            Dashboard for songs listening pattern.
            '''
        ),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)