import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd
import plotly.express as px

import plotly.graph_objects as go
from plotly.subplots import make_subplots

dash.register_page(
    __name__,
    path='/analytics_story_line',
    title='Dynamic Visulization',
    name='Dynamic Visulization'
)

df = pd.read_csv("./data/movies_high_income.csv")
all_directors = df['Directors'].unique()
years = df['Year'].unique()
years_num = years.astype(int)
df['Year'] = df['Year'].astype(int)


def render_income_year():
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    avg = []
    num_dit = []
    sum = []
    #print(years)
    for i in years:
        df_sub2 = df[df['Year'] == int(i)]
        sum2 = 0
        num_dit.append(len(df_sub2['Directors'].unique()))
        for e in df_sub2['Income_million']:
            sum2 += e
        avg.append(round(sum2/df_sub2.shape[0],2))
        sum.append(sum2)
        #print(i, sum2, df_sub2['Directors'].unique())
    # Add traces
    #fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig = go.Figure(
    data=[
        go.Bar(name='Total Income/$Million', x=years, y=sum, yaxis='y', offsetgroup=1),
        go.Bar(name='Number of Directors', x=years, y=num_dit, yaxis='y2', offsetgroup=2)
    ],
    layout={
        'yaxis': {'title': 'Total Income/$Million'},
        'yaxis2': {'title': 'Number of Directors', 'overlaying': 'y', 'side': 'right'}
    }
)

    # Add figure title
    fig.update_layout(
        title_text="Directors and Income",
        barmode='group',
        xaxis =dict(tickmode = 'array',
                    tickvals = years)
    )

    # Set x-axis title
    fig.update_xaxes(title_text="Year")

    return html.Div(dcc.Graph(figure = fig))


layout = html.Div(children=[
    html.H2("Story Line of Movie Data from "+str(years_num.min())+" to "+str(years_num.max())),
    html.H3("Overview"),
    render_income_year(),
    html.H3("Dynamic Visulisations of High Income Movies by Years"),
    html.Div([
         "Select to visualize graph in each year: ",
        dcc.RadioItems(
                       years,
        value="2022",
        id='year-select', inline=True),
        html.Div(id='year-output'),
        dcc.Graph(id = 'year-graph', figure={}),
        html.Br(),
        html.Div("Click the play button in the below graph to view the animation version",
                 className="Note"),
        html.Iframe(
                src="./assets/dynamic2.html",
                style={"height": "1067px", "width": "100%"},
            )
    ]),
    html.Br(),
    html.H3(children='Dynamic Visulisations of High Income Movies by Directors'),
	html.Div([
        "Select Directors: ",
        dcc.Dropdown(all_directors,
        value="Steven Spielberg",
        id='director-select')
    ]),
    html.Div(id='director-output'),
    dcc.Graph(id = 'director_graph', figure={})
])


@callback(
    Output(component_id='director-output', component_property='children'),
    Input(component_id='director-select', component_property='value')
)
def update_director_selected(input_value):
    return f'You selected: {input_value}'

@callback(
    Output(component_id='year-output', component_property='children'),
    Input(component_id='year-select', component_property='value')
)
def update_year_selected(input_value):
    df_sub2 = df[df['Year'] == int(input_value)]
    sum = 0
    num_dit = len(df_sub2['Directors'].unique())
    for e in df_sub2['Income_million']:
        sum += e
    avg = round(sum/df_sub2.shape[0],2)
    return f'The total income of {input_value} is {sum}, average is {avg} and {num_dit} directors produce new movies'

@callback(
    Output(component_id="year-graph", component_property="figure"),
    Input(component_id='year-select', component_property="value"))

def update_year_graph(input):
    #print(type(input))
    dfsub = df[df['Year'] == int(input)]
    print(dfsub.head)
    fig = px.bar(dfsub, x="Directors", y="Income_million", 
             color="Genre",
           hover_data=['Directors','Title', 'Stars'],
           title="Movie Data by Directors in "+str(input))
    fig.update_traces(width = 0.5)
    return fig

@callback(
        Output(component_id="director_graph", component_property="figure"),
        Input(component_id='director-select', component_property="value"))

def update_bar_chart(input_value):
    df_director = df.query("Directors == @input_value")
    min_year = df_director['Year'].min()
    max_year = df_director['Year'].max()

    fig = px.bar(df_director, x = "Year", y="Income_million", 
                 color="Title", hover_data=["Stars", "Genre", "Rating", "Runtime"],
                 title="High Income Movies Directored by "+str(input_value))
    fig.update_traces(width=0.5)
    if min_year != max_year:
        fig.update_layout(yaxis_title = "Income/$Million",
                        legend_title = "Movie names",
                        xaxis = dict(
                                tickmode = 'linear',
                                tick0 = min_year,
                                dtick = 1
                            ))
    else:
        fig.update_layout(yaxis_title = "Income/$Million",
                        legend_title = "Movie names",
                        xaxis = dict(
                                tickmode = 'array',
                                tickvals = [min_year],
                            ))
    return fig