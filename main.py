from dash import Dash, html, dcc
import dash
import pandas as pd

#df = pd.read_csv("./movies_high_rating.csv")

app = Dash(__name__, use_pages=True)
app.title = "Visual Analysis System for high Income Movies"

app.layout = html.Div([
    html.H1(app.title),

    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']}", href=page["relative_path"]
                ),
            )
            for page in dash.page_registry.values()
        ],className="nav",
    ),

	dash.page_container
])

if __name__ == '__main__':
    app.run_server(debug=True)