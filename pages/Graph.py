import dash
from dash import html, dcc, callback, Input, Output, dash_table, Dash
import pandas as pd
import plotly.express as px

dash.register_page(
    __name__,
    path='/analytics_graph',
    title='Graph Visulization',
    name='Graph Visulization'
)

layout = html.Div(children=[
    html.Iframe(
            src="./assets/graph2.html",
            style={"height": "1067px", "width": "100%"},
        )
])