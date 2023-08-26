import dash
from dash import html, dcc, Input, Output, dash_table
import pandas as pd

dash.register_page(
    __name__,
    path='/analytics_DataFrame',
    title='Overview of Data Set',
    name='Data Set'
)

df = pd.read_csv("./data/movies_high_income.csv")
df = df.drop(df.columns[[0]],axis=1)

layout = html.Div(children=[
    html.H2('Data Set Overview'),
    dash_table.DataTable(id = "df", data=df.to_dict('records'), page_size=30),
    # html.Iframe(src="../assets/dataset.html",
    #             style={"height": "1067px", "width": "100%"})
    html.H2("Source"),
    html.Div("The original full data set we choose to use is Top 100 popular movies from 2003 to 2022 (iMDB). \
             Specifically in VA system, we focus on displaying high income movies. So our data set is the sub \
             data set that the income of those movies are all higher than 256.70.")
])