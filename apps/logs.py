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
    
   dbc.Row
   ([
     html.H5("June 30th, 2021", style = {'font-size':'18px'}), 
   ]),
    
    
   dbc.Row
   ([
     html.H5("June 29th, 2021", style = {'font-size':'18px'}), 
   ]),
    dbc.Row
   ([
     html.P("Interview Preparations and Attended Interviews", style = {'font-size':'14px','margin-left':'20px'}), 
   ]),
   
   dbc.Row
   ([
     html.H5("June 28th, 2021", style = {'font-size':'18px'}), 
   ]),
    dbc.Row
   ([
     html.P("Squaddd", style = {'font-size':'14px'}), 
   ]),
    dbc.Row
   ([
     html.P("Created Mongo DB connection in the Node Js Application for providing input \
                    to the python script", style = {'font-size':'14px','margin-left':'20px'}), 
   ]),
    dbc.Row
   ([
     html.P("Created and executed pycode.js file in Node Js application to run python code of Squaddd matching algorithm", style = {'font-size':'14px','margin-left':'20px'}), 
   ]),
    dbc.Row
   ([
     html.P("Google CapStone Project", style = {'font-size':'14px'}), 
   ]),
    dbc.Row
   ([
     html.P("Read through problem statement", style = {'font-size':'14px','margin-left':'20px'}), 
   ]),

],style={"height": "100vh"})

#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])
server = app.server
layout = html.Div([body])



app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})
