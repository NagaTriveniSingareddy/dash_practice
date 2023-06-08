import pandas as pd
from dash import Dash, dcc, html, Input, Output,dash_table
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_table_experiments as dt

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
card1=dbc.Card([
        dbc.CardBody([
        html.H4('SuperStore Sales Performance Report')
        ], className='text-center')
                    ])


card2=dbc.Card([
    #dbc.CardHeader("totalsales",className='text-center'),
        dbc.CardBody([
        html.Span("totalsales",style={"margin-top":"-17px",
        "float":"left",
        "margin-left":"-15px",
        "font-size":"15px"}),
        html.H6(id="total_sales", className="card-title"),
        #html.Span("total_sales",className="span-class")
        ], className='text-center')
                    ],color="light",style={"margin-top":"2px",
                      "height":"90px","margin-left":"-10px",
                       })
card3=dbc.Card([
    #dbc.CardHeader("totalprofit",className='text-center'),
        dbc.CardBody([
        html.Span("total_profit",style={"margin-top":"-17px",
        "float":"left",
        "margin-left":"-15px",
        "font-size":"15px"}),
        html.H6(id="total_profit", className="card-title"),
        #html.Span("total_sales",className="span-class")
        ], className='text-center')
                    ],color="light",style={"margin-top":"2px",
                      "height":"90px",
                       })
card4=dbc.Card([
    #dbc.CardHeader("totalsales",className='text-center'),
        dbc.CardBody([
        html.Span("profitmargin",style={"margin-top":"-17px",
        "float":"left",
        "margin-left":"-15px",
        "font-size":"15px"}),
        html.H6(id="profit_margin", className="card-title"),
        #html.Span("total_sales",className="span-class")
        ], className='text-center')
                    ],color="light",style={"margin-top":"2px",
                      "height":"90px",
                       })
card5=dbc.Card([
    #dbc.CardHeader("totalsales",className='text-center'),
        dbc.CardBody([
        html.Span("orders",style={"margin-top":"-17px",
        "float":"left",
        "margin-left":"-15px",
        "font-size":"15px"}),
        html.H6(id="orders", className="card-title"),
        #html.Span("total_sales",className="span-class")
        ], className='text-center')
                    ],color="light",style={"margin-top":"2px",
                      "height":"90px",
                      })
card6=dbc.Card([
    #dbc.CardHeader("totalsales",className='text-center'),
        dbc.CardBody([
        html.Span("products",style={"margin-top":"-17px",
        "float":"left",
        "margin-left":"-15px",
        "font-size":"15px"}),
        html.H6(id="products", className="card-title"),
        #html.Span("total_sales",className="span-class")
        ], className='text-center')
                    ],color="light",style={"margin-top":"2px",
                      "height":"90px",
                      })


app.layout=dbc.Container([dbc.Row([dbc.Col(card1,width=10)]),dbc.Row([dbc.Col(card2),dbc.Col(card3),dbc.Col(card4),dbc.Col(card5),dbc.Col(card6)],classname=style={"display":"flex","margin-top":"2px","padding-right":"0px !important","padding-left":"0px !important","margin-left":"1px"})])

if __name__ == '__main__':
    app.run_server(debug=True)    