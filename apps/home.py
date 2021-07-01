#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 18:31:27 2021

@author: thejeswarreddynarravala
"""

import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_daq as daq
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import base64
from app import app


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']




test_png = os.getcwd() +'/assests/DSC_1452.png'
test_base64 = base64.b64encode(open(test_png, 'rb').read()).decode('ascii')
body = dbc.Container([ 
    
dbc.Row([dbc.Col([html.Div( 
    html.Img(src='data:image/png;base64,{}'.format(test_base64),style = {'width':'400px','height':'400px'})
    ),html.Br(),
    html.Div(
    [html.Button("Resume", id="btn_txt"), dcc.Download(id="download-text")]
),
   dbc.Row([
        html.A('GitHub', href='https://github.com/tnarravala',style = {"color":"#E60B1F",'font-size':'20px'})
             ]),]),
         dbc.Col([
             dbc.Row([html.H1("Professional Summary",style = {'font-size':'18px', 'text-decoration': 'underline'})]),
             dbc.Row([html.P("Versatile individual with experience collecting, transforming and organizing data for analysis to make informed decisions. Excellent understanding \
                             and proficiency of platforms for effective data analyis, including SQl, spreadsheets, Tableau, and R. Strong Communication, Organizational, and analytical skills. Recently completed the\
                                 Google Data Analytics Certificate -- a rigorous, hands-on program that covers the entire scope of the data analysis process."),]),
             dbc.Row( [html.H1("Education", style = {'font-size':'18px','text-decoration': 'underline'}) ]),
             dbc.Row(["Masters Degree in Computational Decision Science and Operations Research, Chicago, USA graduated on May 15th, 2021"]),
             dbc.Row([html.Br()]),
             dbc.Row([html.H4("Work Experience", style = {'font-size':'18px','text-decoration': 'underline'})]),
             dbc.Row(['Currently working as Data Engineer at Squaddd, Inc']),
             dbc.Row([html.Br()]),
             dbc.Row([html.H1("Core Skills and Experience",style = {'font-size':'18px','text-decoration': 'underline'})]),
             dbc.Row([html.H5("SQL :"),html.P(" 4 years of Experience as an SQL Developer at Tata Consultancy Services")]),
             dbc.Row([html.H5("Python:"),html.P(" 3 years of Experience as Data Analyst Intern and in the research project")]),
             dbc.Row([html.H5("Tableau:"),html.P("2+ years of experience in generating reports and dashboards")]),
             dbc.Row([html.H5("R programming: "),html.P("2 years of experience and used to scrap the data from web, cleaning and generating reports")]),
             dbc.Row([html.H5("Advanced Excel: "),html.P("Proficent with Pivot tables, optimizers, monte carlo simulations, VLOOKUP,HLOOKUP,Index,match and all other basic excel functionalities ")])
             
             ])]),
            
                             
dbc.Row([html.P("This site is created by myself using Dash Plotly in Python Language")]),




],style={"height": "100vh"}

)

#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])
server = app.server
layout = html.Div([body])


app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

@app.callback(
    Output("download-text", "data"),
    Input("btn_txt", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file(
        "Resume_Thejeswar.pdf"
    )

