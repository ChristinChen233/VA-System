import dash
from dash import html, dcc, callback, Input, Output, dash_table, Dash
import pandas as pd
import plotly.express as px

dash.register_page(
    __name__,
    path='/analytics_highD',
    title='High Dimensional Data Visulization',
    name='High Dimensional Data Visulization'
)


layout = html.Div(children=[
    html.H1("High Dimensional Data Visualisation"),
    html.Iframe(
            src="./assets/highD.html",
            style={"height": "1067px", "width": "100%"},
        ),
    html.H1(),
    html.Iframe(
            src="./assets/highD_scatter.html",
            style={"height": "1067px", "width": "100%"},
        ),
])
