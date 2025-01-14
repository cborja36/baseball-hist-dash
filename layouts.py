# Dash components, html, and dash tables
from dash import dcc, html, dash_table

# Import Bootstrap components
import dash_bootstrap_components as dbc

# Import custom data.py
import data

# Import data from data.py file
teams_df = data.teams
# Hardcoded list that contain era names and marks
era_list = data.era_list
era_marks = data.era_marks


# Main applicaiton menu
appMenu = html.Div([
    dbc.Row(
        [
            dbc.Col(html.H4(style={'text-align': 'center'}, children='Select Era:'),
                xs={'size':'auto', 'offset':0}, sm={'size':'auto', 'offset':0}, md={'size':'auto', 'offset':3},
                lg={'size':'auto', 'offset':0}, xl={'size':'auto', 'offset':0}),
            dbc.Col(dcc.Dropdown(
                style = {'text-align': 'center', 'font-size': '18px', 'width': '210px'},
                id='era-dropdown',
                options=era_list,
                value=era_list[0]['value'],
                clearable=False),
                xs={'size':'auto', 'offset':0}, sm={'size':'auto', 'offset':0}, md={'size':'auto', 'offset':0},
                lg={'size':'auto', 'offset':0}, xl={'size':'auto', 'offset':0}),

            dbc.Col(html.H4(style={'text-align': 'center', 'justify-self': 'right'}, children='Select Team:'),
                xs={'size':'auto', 'offset':0}, sm={'size':'auto', 'offset':0}, md={'size':'auto', 'offset':3},
                lg={'size':'auto', 'offset':0}, xl={'size':'auto', 'offset':1}),
            dbc.Col(dcc.Dropdown(
                style = {'text-align': 'center', 'font-size': '18px', 'width': '210px'},
                id='team-dropdown',
                clearable=False),
                xs={'size':'auto', 'offset':0}, sm={'size':'auto', 'offset':0}, md={'size':'auto', 'offset':0},
                lg={'size':'auto', 'offset':0}, xl={'size':'auto', 'offset':0})
        ],
    ),
    dbc.Row(dbc.Col(html.P(style={'font-size': '16px', 'opacity': '70%'},
        children='''For continuity, some teams historical names where changed to match '''
        '''their modern counterpart. Available teams are updated based on Era selection.'''))),
],className='menu')


# Menu slider used, NOT independent, MUST be used with main menu
menuSlider = html.Div([
    dbc.Row(dbc.Col(dcc.RangeSlider(
        id='era-slider',
        min=1903,
        max=teams_df['year'].max(),
        marks=era_marks,
        tooltip={'always_visible': False, 'placement': 'bottom'}))),
    dbc.Row(dbc.Col(html.P(style={'font-size': '16px', 'opacity': '70%'},children='Adjust slider to desired range.'))),
],className='era-slider')


# Layout for Team Analysis page
teamLayout = html.Div([
    dbc.Row(dbc.Col(html.H3(children='Team Accolades'))),
    # Display Championship titles in datatable
    dbc.Row(dbc.Col(html.Div(id='team-data'), xs={'size':'auto', 'offset':0}, sm={'size':'auto', 'offset':0}, md={'size':7, 'offset':0}, lg={'size':'auto', 'offset':0},
                xl={'size':'auto', 'offset':0}),justify="center"),
    ### Graphs of Historical Team statistics ###
    dbc.Row(dbc.Col(html.H3(children='Team Analysis'))),
    # Bar Chart of Wins and Losses
    dbc.Row(dbc.Col(dcc.Graph(id='wl-bar', config={'displayModeBar': False}), xs={'size':12, 'offset':0}, sm={'size':12, 'offset':0}, md={'size': 12, 'offset': 0},lg={'size': 12, 'offset': 0})),
    # Line Chart of Batting Average, BABIP, and Strikeout Rate
    dbc.Row(dbc.Col(dcc.Graph(id='batting-line', config={'displayModeBar': False}), xs={'size':12, 'offset':0}, sm={'size':12, 'offset':0}, md={'size': 12, 'offset': 0},lg={'size': 12, 'offset': 0})),
    # Bar Char of Errors and Double Plays
    dbc.Row(dbc.Col(dcc.Graph(id='feild-line', config={'displayModeBar': False}), xs={'size':12, 'offset':0}, sm={'size':12, 'offset':0}, md={'size': 12, 'offset': 0},lg={'size': 12, 'offset': 0})),
    dbc.Row(dbc.Col(html.H4(children='Pitching Performance'))),
    dbc.Row(
        [
            # Line graph of K/BB ratio with ERA bubbles
            dbc.Col(dcc.Graph(id='pitch-bubble', config={'displayModeBar': False}), xs={'size':12, 'offset':0}, sm={'size':12, 'offset':0}, md={'size': 12, 'offset': 0},lg={'size': 6, 'offset': 0}),
            # Pie Chart, % of Completed Games, Shutouts, and Saves of Total Games played
            dbc.Col(dcc.Graph(id='pitch-pie', config={'displayModeBar': False}), xs={'size':12, 'offset':0}, sm={'size':12, 'offset':0}, md={'size': 12, 'offset': 0},lg={'size': 6, 'offset': 0}),
        ],
        class_name='g-0',
    ),
],className='app-page')


# Player menu used to select players after era and team are set
playerMenu = html.Div([
    dbc.Row(dbc.Col(html.H3(children='Player Profile and Statistics'))),
    dbc.Row(dbc.Col(html.P(style={'font-size': '16px', 'opacity': '70%'},
        children='Available players are updated based on team selection.'))),
    dbc.Row(
        [
            dbc.Row(dbc.Col(html.H4(style={'text-align': 'center'}, children='Select Player:'), xs={'size':'auto', 'offset':0}, sm={'size':'auto', 'offset':0},
                md={'size':'auto', 'offset':0}, lg={'size':'auto', 'offset':0}, xl={'size':'auto', 'offset':0})),
            dbc.Row(dbc.Col(dcc.Dropdown(
                style={'margin-left': '2%', 'text-align': 'center', 'font-size': '18px', 'width': '218px'},
                id='player-dropdown',
                clearable=False
                ), xs={'size':'auto', 'offset':0}, sm={'size':'auto', 'offset':0}, md={'size':'auto', 'offset':0}, lg={'size':'auto', 'offset':0},
                xl={'size':'auto', 'offset':0})),
        ],
        class_name='g-0',
    ),
    html.Br(),
    dbc.Row(dbc.Col(dash_table.DataTable(
            id='playerProfile',
            style_as_list_view=True,
            editable=False,
            style_table={
                'overflowY': 'scroll',
                'width': '100%',
                'minWidth': '100%',
            },
            style_header={
                    'backgroundColor': '#f8f5f0',
                    'fontWeight': 'bold'
                },
            style_cell={
                    'textAlign': 'center',
                    'padding': '8px',
                },
        ), xs={'size':'auto', 'offset':0}, sm={'size':'auto', 'offset':0}, md={'size':8, 'offset':0}, lg={'size':'auto', 'offset':0},
                xl={'size':'auto', 'offset':0}),justify="center"),
    html.Br()
],className = 'app-page')


# Batting statistics
battingLayout = html.Div([
    # Batting datatable
    dbc.Row(dbc.Col(
        dash_table.DataTable(
            id='batterTable',
            style_as_list_view=True,
            editable=False,
            style_table={
                'overflowY': 'scroll',
                'width': '100%',
                'minWidth': '100%',
            },
            style_header={
                    'backgroundColor': '#f8f5f0',
                    'fontWeight': 'bold'
                },
            style_cell={
                    'textAlign': 'center',
                    'padding': '8px',
                }
        ), xs={'size':12, 'offset':0}, sm={'size':12, 'offset':0}, md={'size':10, 'offset':0}, lg={'size':10, 'offset':0},
                xl={'size':10, 'offset':0}),justify="center"),


    dbc.Row(dbc.Col(html.H3(style={'margin-top': '1%', 'margin-bottom': '1%'},
            children='Player Analysis'))),
    dbc.Row(dbc.Col(html.P(style={'font-size': '16px', 'opacity': '70%'},
            children='Some statistics where not tracked until the 1950s, those statistics where artifically filled with 0\'s for simulation purposes'))),

    dbc.Row(
        [
            # Line/Bar Chart of On-Base Percentage, features; H BB HBP SF
            dbc.Col(dcc.Graph(id='obp-line', config={'displayModeBar': False}), xs={'size':12, 'offset':0}, sm={'size':12, 'offset':0}, md={'size': 12, 'offset': 0},lg={'size': 6, 'offset': 0}),
            # Line/Bar Chart of Slugging Average, features; 2B 3B HR
            dbc.Col(dcc.Graph(id='slg-line', config={'displayModeBar': False}), xs={'size':12, 'offset':0}, sm={'size':12, 'offset':0}, md={'size': 12, 'offset': 0},lg={'size': 6, 'offset': 0})
        ],
        class_name='g-0',
    ),
    # Line Chart of OPS, Features; OBP SLG
    dbc.Row(dbc.Col(dcc.Graph(id='ops-line', config={'displayModeBar': False}), xs={'size':12, 'offset':0}, sm={'size':12, 'offset':0},
        md={'size': 12, 'offset': 0},lg={'size': 12, 'offset': 0})),
],className = 'app-page')


# Feilding Statistics
fieldingLayout = html.Div([
    dbc.Row(dbc.Col(html.H3(style={'margin-bottom': '1%'},children='Feilding'))),
    # Feilding Datatable
    dbc.Row(dbc.Col(dash_table.DataTable(
            id='fieldTable',
            style_as_list_view=True,
            editable=False,
            style_table={
                'overflowY': 'scroll',
                'width': '100%',
                'minWidth': '100%',
            },
            style_header={
                    'backgroundColor': '#f8f5f0',
                    'fontWeight': 'bold'
                },
            style_cell={
                    'textAlign': 'center',
                    'padding': '8px',
                }
        ), xs={'size':12, 'offset':0}, sm={'size':12, 'offset':0}, md={'size':8, 'offset':0}, lg={'size':8, 'offset':0}, xl={'size':8, 'offset':0}),justify="center"),
    html.Br(),
    dbc.Row(dbc.Col(html.H3(style={'margin-bottom': '1%'}, children='Pitching'))),
    dbc.Row(dbc.Col(html.Div(id='pitch-data'), xs={'size':12, 'offset':0}, sm={'size':12, 'offset':0}, md={'size':10, 'offset':0},
        lg={'size':10, 'offset':0}, xl={'size':10, 'offset':0}),justify="center"),
    html.Br(),
    dbc.Row(dbc.Col(html.H3(children='Player Analysis'))),
    # Player dropdown menu
    dbc.Row(
        [
            dbc.Row(dbc.Col(html.H4(style={'text-align': 'center'}, children='Select Position:'), xs={'size':'auto', 'offset':0}, sm={'size':'auto', 'offset':0},
                md={'size':'auto', 'offset':0}, lg={'size':'auto', 'offset':0}, xl={'size':'auto', 'offset':0})),
            dbc.Row(dbc.Col(dcc.Dropdown(
                style={'margin-left': '5px','text-align': 'center', 'font-size': '18px', 'width': '100px'},
                id='pos-dropdown',
                clearable=False
                ), xs={'size':'auto', 'offset':0}, sm={'size':'auto', 'offset':0}, md={'size':'auto', 'offset':0}, lg={'size':'auto', 'offset':0},
                xl={'size':'auto', 'offset':0})),
        ],
        class_name='g-0',
    ),
    dbc.Row(dbc.Col(html.H4(children='Pitching Performance'))),
    # Pitching and Fielding graphs, Pitching graphs are set in a subplot dcc.Graph(id='field-graphs', config={'displayModeBar': False})
    dbc.Row(dbc.Col(html.Div(id='pitch-graphs'), xs={'size':12, 'offset':0}, sm={'size':12, 'offset':0},
        md={'size':12, 'offset':0}, lg={'size':12, 'offset':0}, xl={'size':12, 'offset':0})),
    dbc.Row(dbc.Col(dcc.Graph(id='field-graph', config={'displayModeBar': False}), xs={'size':12, 'offset':0}, sm={'size':12, 'offset':0},
        md={'size':12, 'offset':0}, lg={'size':12, 'offset':0}, xl={'size':12, 'offset':0})),
],className = 'app-page')

# Player menu used to select players after era and team are set
projMenu = html.Div([
    # dbc.Row(dbc.Col(html.H3(children='Player Profile and Statistics'))),
    # dbc.Row(dbc.Col(html.P(style={'font-size': '16px', 'opacity': '70%'},
    #     children='Available players are updated based on team selection.'))),
    dbc.Row(
        [
            dbc.Row(dbc.Col(html.H4(style={'text-align': 'center'}, children='Select Year:'), xs={'size':'auto', 'offset':0}, sm={'size':'auto', 'offset':0},
                md={'size':'auto', 'offset':0}, lg={'size':'auto', 'offset':0}, xl={'size':'auto', 'offset':0})),
            dbc.Row(dbc.Col(dcc.Dropdown(
                style={'margin-left': '2%', 'text-align': 'center', 'font-size': '18px', 'width': '100px'},
                id='year-dropdown-select',
                options=[{'label': '2020', 'value': 2020},],
                value=2020,
                clearable=False,
                ), xs={'size':'auto', 'offset':0}, sm={'size':'auto', 'offset':0}, md={'size':'auto', 'offset':0}, lg={'size':'auto', 'offset':0},
                xl={'size':'auto', 'offset':0})),
            dbc.Row(dbc.Col(html.H4(style={'margin-left': '15%', 'text-align': 'center', 'width': '120px'}, children='Select Team:'), xs={'size':'auto', 'offset':0}, sm={'size':'auto', 'offset':0},
                md={'size':'auto', 'offset':0}, lg={'size':'auto', 'offset':0}, xl={'size':'auto', 'offset':0})),
            dbc.Row(dbc.Col(dcc.Dropdown(
                style={'margin-left': '5%', 'text-align': 'center', 'font-size': '18px', 'width': '240px'},
                id='team-dropdown-select',
                clearable=False
                ), xs={'size':'auto', 'offset':0}, sm={'size':'auto', 'offset':0}, md={'size':'auto', 'offset':0}, lg={'size':'auto', 'offset':0},
                xl={'size':'auto', 'offset':0}))
        ],
        class_name='g-0',
    ),
    html.Br(),
    dbc.Row(dbc.Col(html.H3(children='Player Profile and Statistics'))),
    dbc.Row(dbc.Col(html.P(style={'font-size': '16px', 'opacity': '70%'},
        children='Available players are based on 2020 team roster. No rookie players from 2021 are included.'))),
    dbc.Row(
        [
            dbc.Row(dbc.Col(html.H4(style={'text-align': 'center'}, children='Select Player:'), xs={'size':'auto', 'offset':0}, sm={'size':'auto', 'offset':0},
                md={'size':'auto', 'offset':0}, lg={'size':'auto', 'offset':0}, xl={'size':'auto', 'offset':0})),
            dbc.Row(dbc.Col(dcc.Dropdown(
                style={'margin-left': '2%', 'text-align': 'center', 'font-size': '18px', 'width': '218px'},
                id='team-player-dropdown',
                clearable=False
                ), xs={'size':'auto', 'offset':0}, sm={'size':'auto', 'offset':0}, md={'size':'auto', 'offset':0}, lg={'size':'auto', 'offset':0},
                xl={'size':'auto', 'offset':0})),
        ],
        class_name='g-0',
    ),
    html.Br(),
    dbc.Row(dbc.Col(dash_table.DataTable(
            id='select-playerProfile',
            style_as_list_view=True,
            editable=False,
            style_table={
                'overflowY': 'scroll',
                'width': '100%',
                'minWidth': '100%',
            },
            style_header={
                    'backgroundColor': '#f8f5f0',
                    'fontWeight': 'bold'
                },
            style_cell={
                    'textAlign': 'center',
                    'padding': '8px',
                },
        ), xs={'size':'auto', 'offset':0}, sm={'size':'auto', 'offset':0}, md={'size':8, 'offset':0}, lg={'size':'auto', 'offset':0},
                xl={'size':'auto', 'offset':0}),justify="center"),
    html.Br()
],className = 'app-page')

# Batting statistics
projLayout = html.Div([
    # Batting datatable
    dbc.Row(dbc.Col(
        dash_table.DataTable(
            id='select-batterTable',
            style_as_list_view=True,
            editable=False,
            style_table={
                'overflowY': 'scroll',
                'width': '100%',
                'minWidth': '100%',
            },
            style_header={
                    'backgroundColor': '#f8f5f0',
                    'fontWeight': 'bold'
                },
            style_cell={
                    'textAlign': 'center',
                    'padding': '8px',
                }
        ), xs={'size':12, 'offset':0}, sm={'size':12, 'offset':0}, md={'size':10, 'offset':0}, lg={'size':10, 'offset':0},
                xl={'size':10, 'offset':0}),justify="center"),
    
    html.Br(),
    dbc.Row(dbc.Col(html.H3(style={'margin-top': '1%', 'margin-bottom': '1%'},
            children='Player Projection'))),
    dbc.Row(dbc.Col(html.P(style={'font-size': '16px', 'opacity': '70%'},
            children='''Projections are based on the past four seasons (2017-2020). Players with less than four seasons 
                of experience, those projections are considered less reliable.'''))),

    dbc.Row(dbc.Col(
        dash_table.DataTable(
            id='batter-proj-table',
            style_as_list_view=True,
            editable=False,
            style_table={
                'overflowY': 'scroll',
                'width': '100%',
                'minWidth': '100%',
            },
            style_header={
                    'backgroundColor': '#f8f5f0',
                    'fontWeight': 'bold'
                },
            style_cell={
                    'textAlign': 'center',
                    'padding': '8px',
                }
        ), xs={'size':12, 'offset':0}, sm={'size':12, 'offset':0}, md={'size':10, 'offset':0}, lg={'size':10, 'offset':0},
                xl={'size':10, 'offset':0}),justify="center"),
    
    html.Br(),
    dbc.Row(dbc.Col(html.H3(style={'margin-top': '1%', 'margin-bottom': '1%'},
            children='Regression Analysis'))),
    dbc.Row(dbc.Col(html.P(style={'font-size': '16px', 'opacity': '70%'},
            children='''The coefficient indicates the direction of performance. If a player is performing well the 
                coefficient is positive, otherwise the coefficient is negative. Career Coefficient and Recent Coefficient 
                include the player\'s 2021 projection. Career analysis includes entire career, while the Recent analysis only 
                considers the past four seasons plus projection (2017-2020 and 2021 Projection).'''))),
    
    dbc.Row(dbc.Col(dcc.Graph(id='lrce-bar', config={'displayModeBar': False}), xs={'size':12, 'offset':0}, sm={'size':12, 'offset':0}, md={'size': 12, 'offset': 0},lg={'size': 12, 'offset': 0})),

    # dbc.Row(
    #     [
    #         # Line/Bar Chart of On-Base Percentage, features; H BB HBP SF
    #         dbc.Col(dcc.Graph(id='obp-line', config={'displayModeBar': False}), xs={'size':12, 'offset':0}, sm={'size':12, 'offset':0}, md={'size': 12, 'offset': 0},lg={'size': 6, 'offset': 0}),
    #         # Line/Bar Chart of Slugging Average, features; 2B 3B HR
    #         dbc.Col(dcc.Graph(id='slg-line', config={'displayModeBar': False}), xs={'size':12, 'offset':0}, sm={'size':12, 'offset':0}, md={'size': 12, 'offset': 0},lg={'size': 6, 'offset': 0})
    #     ],
    #     class_name='g-0',
    # ),
    # # Line Chart of OPS, Features; OBP SLG
    # dbc.Row(dbc.Col(dcc.Graph(id='ops-line', config={'displayModeBar': False}), xs={'size':12, 'offset':0}, sm={'size':12, 'offset':0},
    #     md={'size': 12, 'offset': 0},lg={'size': 12, 'offset': 0})),
],className = 'app-page')