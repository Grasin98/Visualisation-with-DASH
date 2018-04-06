# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 09:09:29 2018

@author: NISARG
"""

import dash
import dash_core_components as dcc
import dash_html_components as html

app=dash.Dash()
app.layout=html.Div(children=[html.H1("Dash Tuts"),dcc.Graph(id="example",
                                                             figure={"data":[{'x':[1,2,3,4,5],'y':[5,6,7,8,9],'type':"line","name":"boats"},
                                                                             {'x':[1,2,3,4,5],'y':[8,10,7,18,9],'type':"bar","name":"cars"}],
                                                                     "layout":{
                                                                         "title":"Basic Dash Example"   
                                                                     }
                                                                     })
                                                                    ])

if __name__=="__main__":
    app.run_server(debug=True)
    
