import pandas as pd
import numpy as np
import altair as alt
from dash import Dash, dcc, html, Input, Output, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go


app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css', '/style.css'])
app.title = "Olympic athletes dashboard"
server = app.server

df = pd.read_csv('data/processed/clean_data.csv')

tab_style = {'padding': '6px', 'fontWeight': 'bold', 'background': 'rgb(31, 5, 43)', 'color': 'white', 'border': 'none'}
tab_selected_style = {'border': 'none', 'borderBottom': '3px solid #EE334E',  'padding': '7px', 'fontWeight': 'bold', 'color': 'black', 'background': '#FCB131'}

app.layout = html.Div([
        html.Div('HELP', id = 'help_btn'),
        dbc.Tooltip(
                    children = [html.H5('Olympics Dashboard User Guide'), 
                                html.Hr(), 
                                'This is a dashboard which allows you to observe the distribution of athlete profiles based on their sports, competition years, competition seasons and nationalities.', html.Br(), html.Br(),
                                'After filtering with the main filters on the left, you can further examine the distribution within each country by clicking on the map, which will update the histograms accordingly. Shift click to select multiple countries. Click on the country again to reset the map.', html.Br(), html.Br(),
                                'If you want to look at the athlete information in detail, you can click into the Data Table tab, which will display all the rows of data based on your selected filters.'],
                    target="help_btn",
                    placement = 'left',
                    className = 'tooltip',
                    id = 'help_tooltip',
                    style = {'font-size': '14px'}
                ),
        html.Div([
            html.H1("Who Are in the Olympics?",
                    style = {'color': '#f5f5f5', 'text-align': 'left', 'padding': '0px 0px 0px 20px', 'margin-bottom': '-10px'}),
            html.H4("Insights for Olympic Athlete Information since 1896", 
                    style = {'color': '#f5f5f5', 'text-align': 'left', 'padding': '0px 0px 10px 20px'}),
        ], id = 'header'),
        # Main Container Div
        html.Div([

            # Sidebar (Filter) Div
            html.Div([
                html.H2("Filters", style = {'flex-grow': '1', 
                                            'margin': '0px',
                                            'border-bottom': '2px solid #f5f5f5', 
                                            'line-height': '1'}),
                html.P('Hover over filters for help!', 
                    style={'color': 'white'}),
                html.P(
                    children=[''],
                    id = 'warning',
                    style = {'width': '100%', 'flex-grow': '1', 'color': '#EE334E'}
                ),
                html.Div([
                    html.H5("Drag Slider To Select Years"),
                    dcc.RangeSlider(
                        min = 1896, max = 2016,
                        marks = {i: {'label': f'{i+4}', 'style': {'transform': 'rotate(90deg)', 'color': '#f5f5f5'}} for i in range(1896, 2016, 8)},
                        id = 'year_range',
                        value = [1896, 2016],
                        tooltip={"placement": "top", "always_visible": True}
                    )
                ], style = {'width': '100%', 'flex-grow': '2'}),
                html.Div([
                    html.H5("Select Sports", id = 'sport_help'),
                    dcc.Dropdown(
                        options=['All'] + np.sort(df.Sport.unique()).tolist(),
                        value=['All'],
                        multi=True,
                        id='sport'
                    )
                ], style = {'width': '100%', 'color': 'black', 'flex-grow': '1.5'}),
                html.Div([
                    html.H5("Select Countries", id = 'country_help'),
                    dcc.Dropdown(
                        options=['All'] + np.sort(df.Team.unique()).tolist(),
                        value=['All'],
                        multi=True,         
                        id='country'
                    )
                ], style = {'width': '100%', 'color': 'black', 'flex-grow': '1.5'}),
                html.Div([
                    html.H5("Medal Filter", id = 'medal_help'),
                    dcc.RadioItems(
                        options=['Gold', 'Silver', 'Bronze'] + ['All'],
                        value='All',
                        id='medals',
                        inline=True
                    )
                ], style = {'width': '100%', 'flex-grow': '1', 'color': '#f5f5f5'}),
                html.Div([
                    html.H5("Season Filter", id = 'season_help'),
                    dcc.RadioItems(
                        options=df.Season.unique().tolist() + ['Both'],
                        value='Both',
                        id='season',
                        inline=True
                    )
                ], style = {'width': '100%', 'flex-grow': '1', 'color': '#f5f5f5'}),
                html.Div([
                    html.H5("Animation Toggle", id = 'animation_help'),
                    dcc.RadioItems(
                        options=['Animate', 'Fixed'],
                        value='Fixed',
                        id='animation',
                        inline=True
                    )
                ], style = {'width': '100%', 'flex-grow': '1', 'color': '#f5f5f5'}),
                dbc.Tooltip(
                    "Choose whether or not to animate the world map by year",
                    target="animation_help",
                    placement = 'right',
                    className = 'tooltip'
                ),
                dbc.Tooltip(
                    "Choose to include summer olympics athletes, winter olympics athletes, or both",
                    target="season_help",
                    placement = 'right',
                    className = 'tooltip'
                ),
                dbc.Tooltip(
                    "Choose to see only athletes who have won specific medals, or all athletes (whether or not they have won medals)",
                    target="medal_help",
                    placement = 'right',
                    className = 'tooltip'
                ),
                dbc.Tooltip(
                    "Select which countries to filter by. Multiple countries can be selected. Choose 'All' to show all countries",
                    target="country_help",
                    placement = 'right',
                    className = 'tooltip'
                ),
                dbc.Tooltip(
                    "Select which sports to filter by. Multiple sports can be selected. Choose 'All' to show all sports",
                    target="sport_help",
                    placement = 'right',
                    className = 'tooltip'
                ),
            ], style = {'width': '20%', 'margin-top': '0px', 'padding': '25px', 
                    'background-color': '#544F78', 'border-radius': '10px',
                    'display': 'flex', 'justify-content': 'space-around', 'flex-direction': 'column'}, id = 'sidebar'), 

            # Graph Container Div         
            html.Div([
                dcc.Tabs([
                    dcc.Tab(label='Plots', children=[
                        dcc.Loading(
                            id = 'loading_hist',
                            children = [
                                dcc.Graph(id='hist', 
                                        style = {'height': '300px', 'width': '33%', 'display': 'inline-block'},
                                        config={
                                            'displayModeBar':False
                                }),
                                dcc.Graph(id='hist2', 
                                        style = {'height': '300px', 'width': '33%', 'display': 'inline-block'},
                                        config={
                                            'displayModeBar':False
                                }),
                                dcc.Graph(id='hist3', 
                                        style = {'height': '300px', 'width': '33%', 'display': 'inline-block'},
                                        config={
                                            'displayModeBar':False
                                })
                            ], type = 'circle', color = '#EE334E'
                        ),
                        dcc.Loading(
                            id = 'loading_map',
                            children = [
                                dcc.Graph(id='map', 
                                        style = {'height': '420px', 'width': '99%'},
                                        config={
                                            'displayModeBar':False
                                })
                            ], type = 'circle', color = '#EE334E'
                        )
                        ],
                            className='custom-tab',
                            selected_className='custom-tab--selected',
                            style = tab_style, selected_style=tab_selected_style),
                    dcc.Tab(label='Data Table', children = [
                        html.Br(),
                        dash_table.DataTable(data=df.sample(50).to_dict('records'), 
                                    columns=[{"name": i, "id": i} for i in df.columns[1:]], 
                                    id = 'tbl', 
                                    style_cell = {'color': 'black', '#f5f5f5Space': 'normal'}, 
                                    style_header = {'color': '#f5f5f5', 'backgroundColor': '#322c4a', 'border': '0px solid #f5f5f5', 'fontWeight': 'bold', 'textAlign': 'left'},
                                    style_data = {'backgroundColor': '#96293F', 'color': '#f5f5f5', 'height': 'auto', 'whiteSpace': 'normal', 'font-size': '10.5px'},
                                    style_data_conditional = [
                                        {
                                            'if': {'column_id': ['ID', 'Sex', 'Height', 'Team', 'Games', 'Season', 'Sport', 'Medal']},
                                            'backgroundColor': '#B33951'
                                        },
                                        {
                                            'if': {
                                                'filter_query': '{Medal} = Gold',
                                                'column_id': 'Medal'
                                            },
                                            'backgroundColor': 'gold',
                                            'color': 'black'
                                        },
                                        {
                                            'if': {
                                                'filter_query': '{Medal} = Silver',
                                                'column_id': 'Medal'
                                            },
                                            'backgroundColor': 'silver',
                                            'color': 'black'
                                        },
                                        {
                                            'if': {
                                                'filter_query': '{Medal} = Bronze',
                                                'column_id': 'Medal'
                                            },
                                            'backgroundColor': 'brown',
                                        }
                                    ],
                                    page_action='native', 
                                    page_size=20)
                    
                        ],
                            className='custom-tab',
                            selected_className='custom-tab--selected',
                            style = tab_style, selected_style=tab_selected_style)
                ], style = {'height': '40px'})
                
                ], style = {'width': '73%', 'overflow': 'hidden', 'height': '780px', 
                            'background-color': '#544F78', 'border-radius': '10px', 
                            'padding': '1%'}, id = 'graph_container')
            ], style = {'display': 'flex', 'justify-content': 'space-around'})
        ], style = {'display': 'fixed', 'height': '100%'}, id = 'main_container')



def filter_data(data, year_range=(1896, 2016), season='Both', medals='All', sport=['All'], country=['All']):
    
    year_filter = (df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])
    season_filter = True if season == 'Both' else (df['Season'] == season)
    medal_filter = True if medals == 'All' else (df['Medal'] == medals)
    sport_filter = True if 'All' in sport else (df['Sport'].isin(sport))
    country_filter = True if 'All' in country else (df['Team'].isin(country))
    
    data = data[year_filter & season_filter & sport_filter & country_filter & medal_filter]

    return data


@app.callback(
    Output('tbl', 'data'),
    Output('warning', 'children'),
    Input('year_range', 'value'),
    Input('sport', 'value'),
    Input('country', 'value'),
    Input('medals', 'value'),
    Input('season', 'value')
)
def update_table(year_range, sport, country, medals, season):
    filtered = filter_data(df, year_range=year_range, sport=sport, country=country, medals=medals, season=season)
    filtered.drop(columns = 'ID', inplace = True)
    msg = ''
    if len(filtered) >= 5000:
        return filtered.sample(5000).to_dict('records'), [msg]
    elif len(filtered) == 0:
        msg = 'No Available Data For Search Parameters'
    return filtered.to_dict('records'), [msg]
    


styling_template = {'title': {'font': {'size': 21, 'family': 'helvetica', 'color': '#f5f5f5'}, 'x': 0,
                        'xref':'paper', 'y': 1, 'yanchor': 'bottom', 'yref':'paper', 'pad':{'b': 20}},
                'legend': {'font': {'color': '#f5f5f5'}},
             'margin': dict(l=20, r=20, t=50, b=20),
             'paper_bgcolor': 'rgba(0,0,0,0)', 
             'plot_bgcolor': 'rgba(0,0,0,0)', 
             'colorway': ['black'],
             'xaxis': {
                 'color': '#f5f5f5'
             },
             'yaxis': {
                 'color': '#f5f5f5'
             }}

map_styles = {
    'title': {'x': 0.1, 'pad':{'b': 10}},
    'geo': {'bgcolor': 'rgba(0,0,0,0)',
            'framecolor': 'rgba(0,0,0,0)', 
            'landcolor': '#fcf7e1', 
            'lakecolor': '#97c7f7'},
    'coloraxis': {
        'colorbar': {'title': {'font': {'color': '#f5f5f5', 'family': 'system-ui,-apple-system,"Segoe UI"'}},
                    'tickfont': {'color': '#f5f5f5', 'family': 'system-ui,-apple-system,"Segoe UI"'}}

    },
    'sliders': [{'font': {'color': '#f5f5f5'}, 'tickcolor': '#f5f5f5', 'pad': {'t': 0}}],
    'updatemenus': [{'font': {'color': '#f5f5f5'}, 'pad': {'t': 10}}]
}

# Function which takes filtered data and plots the two histograms
@app.callback(
    Output('hist', 'figure'),
    Output('hist2', 'figure'),
    Output('hist3', 'figure'),
    Input('year_range', 'value'),
    Input('sport', 'value'),
    Input('country', 'value'),
    Input('medals', 'value'),
    Input('season', 'value'),
    Input('map', 'selectedData'),
)
def update_graphs(year_range, sport, country, medals, season, select):

    title1 = 'Distribution of Athlete Heights'
    title2 = 'Distribution of Athlete Ages'
    title3 = 'Distribution of Athlete Weights'

    if select:
        country = [selection['location'] for selection in select['points']]
        title1 += f'<br><sup>{", ".join(country)}</sup>'
        title2 += f'<br><sup>{", ".join(country)}</sup>'
        title3 += f'<br><sup>{", ".join(country)}</sup>'

    filtered = filter_data(df, year_range=year_range, sport=sport, country=country, medals=medals, season=season)
    filtered = filtered.groupby(['ID', 'Games']).agg({'Age': 'mean', 'Height': 'mean', 'Weight': 'mean', 'Sex': 'first', 'Year': 'first'}).reset_index()

    fig = px.histogram(data_frame=filtered, nbins=50 ,
                        x='Height', color='Sex', opacity=0.8, 
                        barmode='overlay', title=title1,
                        color_discrete_map={'M':'#0081C8', 'F':'#EE334E'})
    fig.update_layout(styling_template)
    fig.update_layout({'xaxis': {'range': [110, 225], 'title': {'text': 'Height (cm)'}}})

    fig2 = px.histogram(data_frame=filtered, 
                        x='Age', color='Sex', opacity=0.8, 
                        barmode='overlay', title=title2,
                        color_discrete_map={'M':'#0081C8', 'F':'#EE334E'})
    fig2.update_layout(styling_template)
    fig2.update_layout({'xaxis': {'range': [10, 60], 'title': {'text': 'Age (years)'}}})

    fig3 = px.histogram(data_frame=filtered,nbins = 70,  
                        x='Weight', color='Sex', opacity=0.8, 
                        barmode='overlay', title=title3,
                        color_discrete_map={'M':'#0081C8', 'F':'#EE334E'})
    fig3.update_layout(styling_template)
    fig3.update_layout({'xaxis': {'range': [30, 200], 'title': {'text': 'Weight (kgs)'}}})

    return (fig, fig3, fig2)

# Function which takes filtered data, does additional aggregation, and plots the choropleth
@app.callback(
    Output('map', 'figure'),
    Input('year_range', 'value'),
    Input('sport', 'value'),
    Input('country', 'value'),
    Input('medals', 'value'),
    Input('season', 'value'), 
    Input('animation', 'value')
)
def update_map(year_range, sport, country, medals, season, animation):
    filtered = filter_data(df, year_range=year_range, sport=sport, country=country, medals=medals, season=season)


    if animation=="Animate":
        grouped = filtered.groupby(['Team', 'Year']).agg({'Name': 'nunique'}).reset_index()
        grouped.rename(columns = {'Team': 'Country', 'Name': 'Number of Athletes'}, inplace = True)
        grouped.sort_values('Year', inplace=True)
        max = grouped['Number of Athletes'].max()
        map = px.choropleth(grouped,
                locations = 'Country',
                locationmode = 'country names',
                color = 'Number of Athletes',
                title='Number of Athletes Per Country<br><sup>Click on Country to Filter Histograms</sup>',
                  animation_frame='Year',
                color_continuous_scale=['#f5f5f5', '#00A651']
                )

        map.update_coloraxes({'cmax': max, 'cmin': 0})
        
    else: 
        grouped = filtered.groupby('Team')['Name'].nunique().reset_index()
        grouped.rename(columns = {'Team': 'Country', 'Name': 'Number of Athletes'}, inplace = True)

        map = px.choropleth(grouped,
                locations = 'Country',
                locationmode = 'country names',
                color = 'Number of Athletes',
                title='Number of Athletes Per Country<br><sup>Click on Country to Filter Histograms</sup>',
                color_continuous_scale=['#f5f5f5', '#00A651']
                )
        
    map.update_layout({'clickmode': 'event+select'})
    map.update_layout(styling_template)
    map.update_layout(map_styles)
    
    return map

if __name__ == '__main__':
    app.run_server(debug=True)