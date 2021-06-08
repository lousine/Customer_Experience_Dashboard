# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 10:02:09 2021

@author: Lusine
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import base64
import pandas as pd

data = pd.read_excel('.\\customer_experience.xlsx')
lik = pd.read_excel('.\\Likelihood.xlsx')
detr = pd.read_excel('.\\detractors.xlsx')
image_filename = 'img1.png'

encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode('ascii')
data['Resp_date'] = pd.to_datetime(data['Resp_date'])

colors = {
        'full-background':  'white',
        'block-borders':    '#00000000',
        'text': 'Garamond'
}

margins = {
        'block-margins': '10px 10px 10px 10px',
        'block-margins': '4px 4px 4px 4px'
}
 
sizes = {
        'subblock-heights': '4px 4px 4px 4px'
}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
server=app.server

R= data.loc[data['Q3T'] == 'I Join/Solve: Retail. Active Sales']
fig3 = px.pie(R, names=R['Q3A'],color_discrete_sequence=px.colors.sequential.Plasma_r)

F= data.loc[data['Q3T'] == 'I Join/Solve: Retail. Waiting time']
fig5 = px.pie(F, names=F['Q3A'],color_discrete_sequence=px.colors.sequential.Plasma_r)

controls = dbc.FormGroup([
    html.P('Pie Chart: Categorical Variables:', style={'textAlign': 'center'}),
        dcc.Dropdown(
                    id='names', 
                    value='Survey', 
                    options=[{'value': x, 'label': x} 
                             for x in ['Survey', 'Age Group of customer', 'Group ARPU segment']],
                    clearable=False
                    ),
    html.P('Likelihood to Recommend: Survey Type:', style={'textAlign': 'center'}),
        dcc.Dropdown(
                    id='surveys', 
                    value='I Solve: Contact Center', 
                    options=[{'value': x, 'label': x} 
                             for x in ['I Solve: Contact Center', 'I Use: Product', 'I Join/Solve: Retail']],
                    clearable=False
                    ),
        html.Br(),
        html.P('Agent types', style={
            'textAlign': 'center'
        }),
        dbc.Card([dbc.Checklist(
            id='check_list',
            options=[{
                'label': 'CC Agent',
                'value': 'value1'
            },
                {
                    'label': 'Technician',
                    'value': 'value2'
                },
                {
                    'label': 'Retail Agent',
                    'value': 'value3'
                }
            ],
            value=['value1', 'value2'],
            inline=True
        )]),
        html.Br(),
        html.P('Heatmap: Consider:', style={
            'textAlign': 'center'
        }),
        dbc.Card([dbc.RadioItems(
            id='radio_items',
            options=[{
                'label': 'Age group',
                'value': 'value1'
            },
                {
                    'label': 'Years with us',
                    'value': 'value2'
                }
            ],
            value='value1',
            style={
                'margin': 'auto'
            }
        )]),
    ]
)
sidebar = html.Div(
    [
        html.H2('Parameters'),
        html.Hr(),
        controls,
    ],style={'backgroundColor': '#FFF44F',
             'block-borders': '#FFF44F' }
)

div_image = html.Div([html.Img(src='data:image/png;base64,{}'.format(encoded_image))],
                     style={'color':'white',
                            'margins':margins,
                            'sizes':sizes
                            })

div_title = html.Div(children =	[html.H1('Customer Feedback Analysis'), 
                                 html.H5('This dashboard is created to provide Customer Feedback visualization.'),
                                 html.H6('To be updated weekly for CEO, CEO-1, CEO-2 level users and for the marketing department.')
                                 ],
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'text-align': 'left',
                            'color': 'black',
                            'font_style':'Garamond',
							}
					)
div_1 = html.Div(children = [html.H5('Likelihood to recommend'),
                                  dcc.Graph(
                                      id='likelihood'),
                                      ],
                 style ={'text-align': 'center',
                            'border': '1px {} solid'.format(colors['block-borders']),
                            'margin': margins['block-margins'], 'width': '49%', 'height': sizes['subblock-heights'],'color': 'black'
                            }
                )

div_2 = html.Div(children = [html.H5('Agent KPI Dynamics'),
                                  dcc.Graph(
                                      id='figure2')
                                      ],
					style ={'text-align': 'center',
                            'border': '1px {} solid'.format(colors['block-borders']),
                            'margin': margins['block-margins'], 'width': '49%', 'height': sizes['subblock-heights'],'color': 'black'
                            }
                )

div_3 = html.Div(children = [html.H5('I Join/Solve: Retail: Did you like active sales?'),
                             dcc.Graph(
                                      id='figure3',
                                      figure=fig3)
                                      ],
					style ={'text-align': 'center',
                            'border': '1px {} solid'.format(colors['block-borders']),
                            'margin': margins['block-margins'], 'width': '49%', 'height': sizes['subblock-heights'],'color': 'black'
                            }
                )

div_4 = html.Div(children = [html.H5('Proportions: Categorical Variables'),
                             dcc.Graph(
                                      id='figure4')
                                      ],
					style ={'text-align': 'center',
                            'border': '1px {} solid'.format(colors['block-borders']),
                            'margin': margins['block-margins'], 'width': '49%', 'height': sizes['subblock-heights'],'color': 'black'
                            }
                )

div_5 = html.Div(children = [html.H5('Retail: Waiting time'),
                             dcc.Graph(
                                      id='figure5',
                                      figure=fig5),
                                      ],
					style ={'text-align': 'center',
                            'border': '1px {} solid'.format(colors['block-borders']),
                            'margin': margins['block-margins'], 'width': '49%', 'height': sizes['subblock-heights'],'color': 'black'
                            }
                )
div_6 = html.Div(children = [html.H5('Product satisfaction considering age and ARPU segment'),
                             dcc.Graph(
                                      id='figure8'),
                                      ],
					style ={'text-align': 'center',
                            'border': '1px {} solid'.format(colors['block-borders']),
                            'margin': margins['block-margins'], 'width': '49%', 'height': sizes['subblock-heights'],'color': 'black'
                            }
                )

div_7 = html.Div(children = [html.H5('Proportions: Categorical Variables Detractors'),
                             dcc.Graph(
                                      id='figure7'),
                                      ],
					style ={'text-align': 'center',
                            'border': '1px {} solid'.format(colors['block-borders']),
                            'margin': margins['block-margins'], 'width': '49%', 'height': sizes['subblock-heights'],'color': 'black'
                            }
                )

div_head = html.Div(children =    [div_image,
                                div_title,
                                ],                    
                    style ={
                            'border': '3px {} solid'.format(colors['block-borders']),
                            'margin': margins['block-margins'], 'display': 'flex', 'flex-flaw': 'row-wrap'
                            })

div_row1 = html.Div(children =[sidebar,
                               div_1,
                               div_2
                               ],                    
                    style ={
                            'border': '3px {} solid'.format(colors['block-borders']),
                            'margin': margins['block-margins'], 'display': 'flex', 'flex-flaw': 'row-wrap'
                            })
div_row2 = html.Div(children =[div_4,
                               div_3,
                               div_5
                               ],                    
                    style ={
                            'border': '3px {} solid'.format(colors['block-borders']),
                            'margin': margins['block-margins'], 'display': 'flex', 'flex-flaw': 'row-wrap'
                            })
div_row3 = html.Div(children =[div_6,
                               div_7
                               ],                    
                    style ={
                            'border': '3px {} solid'.format(colors['block-borders']),
                            'margin': margins['block-margins'], 'display': 'flex', 'flex-flaw': 'row-wrap'
                            })

app.layout = html.Div(  [
                         div_head,
                         div_row1,
                         div_row2,
                         div_row3
                        ],
                        style = {
                            'backgroundColor': colors['full-background']
                        }
                    )


@app.callback(
    Output("figure4", "figure"), 
    [Input("names", "value")])

def generate_chart(names):
    fig = px.pie(data,names=names,color_discrete_sequence=px.colors.sequential.Plasma_r)
    return fig

@app.callback(
    Output("figure2", "figure"), 
    [Input("surveys", "value")])

def generate_chartZ(surveys):
    data1 = data[['Survey','Resp_date','Q2A']]
    a = pd.DataFrame(data1.groupby('Resp_date').mean())
    a = a.reset_index()
    fig1 = px.line(a.loc[a['Survey'] == surveys], x="Resp_date", y="Q2A",
                   template="plotly_white",labels=dict(Resp_date= "Response Date",Q2A="Agent KPI"))
    fig1.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label="1m",
                         step="month",
                         stepmode="backward"),
                    dict(count=3,
                         label="3m",
                         step="month",
                         stepmode="backward"),
                    dict(count=1,
                         label="MTD",
                         step="month",
                         stepmode="todate")
                    ])
                ),
            rangeslider=dict(
                visible=True
                ),
            type="date"
            )
        )
    return fig1
    
@app.callback(
    Output("figure7", "figure"), 
    [Input("names", "value")])

def generate_chart0(names):
    fig6 = px.pie(detr,names=names,color_discrete_sequence=px.colors.sequential.Plasma_r)
    return fig6

@app.callback(
    Output("likelihood", "figure"), 
    [Input("surveys", "value")])

def generate_chart1(surveys):
    fig1 = px.bar(lik.loc[lik['Survey'] == surveys], x="Date", y=["Detractors", "Neutrals", "Promoters"])
    fig1.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label="1m",
                         step="month",
                         stepmode="backward"),
                    dict(count=3,
                         label="3m",
                         step="month",
                         stepmode="backward"),
                    dict(count=1,
                         label="MTD",
                         step="month",
                         stepmode="todate")
                    ])
                ),
            rangeslider=dict(
                visible=True
                ),
            type="date"
            )
        )
    return fig1

@app.callback(
    Output("figure8", "figure"), 
    [Input("radio_items", "value")])

def generate_chartY(radio_items):
    fig8 = go.Figure(data=go.Heatmap(
                   z=[[7,9,8,4,9], [6,8,7,6,8], [8,9,8,8,7], [7,8,5,6,8],[8,9,8,6,7]],
                   x=['Very High', 'High', 'Medium', 'Low', 'Very Low'],
                   y=['18-25','26-35', '36-45', '46-55','56-65'],
                   hoverongaps = False))
    return fig8

if __name__=='__main__':
    app.run_server(debug=True, port = 8080)