import dash
from dash import html, dcc

dash.register_page(
    __name__,
    path='/',
    title='Home Page',
    name='Main Board'
)

layout = html.Div(children=[
    html.Iframe(
            src="./assets/index.html",
            style={"height": "1067px", "width": "100%"},
        )
])