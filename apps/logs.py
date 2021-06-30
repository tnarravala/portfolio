#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 00:52:00 2021

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


body = dbc.Container([
    
    dbc.Row([html.H4("June 28th, 2021")]),
    dbc.Row(html.H5("Squaddd :")),
    dbc.Row([html.P("Created Mongo DB connection in the Node Js Application for providing input \
                    to the python script"),
              html.P("Created and executed pycode.js file in Node Js application to run python code of Squaddd matching algorithm")])      
                    ,
    dbc.Row([html.H5("Google Capstone: ")]),
    dbc.Row([
        html.P("Read the Cyclistics use case")
        ])                       ,  
                             
    dbc.Row([html.H4("June 28th, 2021")]),
    dbc.Row(html.P("Interview Preparations and Attended Interviews")),
    
    ],style={"height": "100vh"})

#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])
server = app.server
layout = html.Div([body])



app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})
