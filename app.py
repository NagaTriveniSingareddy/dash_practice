import pandas as pd
from dash import Dash, dcc, html, Input, Output,dash_table
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_table_experiments as dt
from datetime import date
from dash.dependencies import Input, Output, State
import dash
import plotly.graph_objects as go
from plotly.graph_objects import *
import time
from plotly.subplots import make_subplots

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
data=pd.read_csv("SuperStoreOrders.csv")
data['sales']=data['sales'].str.replace(',','')
data['sales']=data['sales'].astype(int)
#print(len(data))
#print(data['order_date'])
#data['order_date'] = data['order_date'].apply(lambda x: pd.to_datetime(x).strftime('%d/%m/%Y'))
data['order_date'] = pd.to_datetime(data['order_date'], infer_datetime_format=True,format='mixed')
#print(data['order_date'])

#data['order_date'] = pd.to_datetime(data['order_date'],dayfirst=True).strftime('%d/%m/%Y')
#print(type(min(data['order_date'])))
card1=dbc.Card([
        dbc.CardBody([
        html.H4('SuperStore Sales Performance Report')
        ], className='text-center')
                    ],color="#f3f5fb",style={"margin-right":"12px"})


card2=dbc.Card([
    #dbc.CardHeader("totalsales",className='text-center'),
        dbc.CardBody([
        html.Span("Total Sales",style={"margin-top":"-17px",
        "float":"left",
        "margin-left":"-15px",

        "font-size":"15px"}),
        html.Div([
        html.H6(id="total_sales",style={'font-size':'22px'}),
        html.H6("M",style={'font-size':'22px'})],style={"display":"flex",
    "justify-content":"flex-start",
    "align-content":"center",
    "margin-top":"16px",
    "margin-left":"39px"})
        ], className='text-center card-color')
                    ],color="#f3f5fb",style={
                      "height":"120px","font-weight": "600"
                       })
card3=dbc.Card([
    #dbc.CardHeader("totalprofit",className='text-center'),
        dbc.CardBody([
        html.Span("Total Profit",style={"margin-top":"-17px",
        "float":"left",
        "margin-left":"-15px",
        "font-size":"15px"}),
        html.Div([
        html.H6(id="total_profit",style={'font-size':'22px'}),
        html.H6("K",style={'font-size':'22px'})],style={"display":"flex",
    "justify-content":"flex-start",
    "align-content":"center",
    "margin-top":"16px",
    "margin-left":"39px"}),
        #html.Span("total_sales",className="span-class")
        ], className='text-center card-color')
                    ],color="#f3f5fb",style={
                      "height":"120px","font-weight": "600"
                       })
card4=dbc.Card([
    #dbc.CardHeader("totalsales",className='text-center'),
        dbc.CardBody([
        html.Span("Profit Margin",style={"margin-top":"-17px",
        "float":"left",
        "margin-left":"-15px",
        "font-size":"15px"}),
        html.Div([
        html.H6(id="profit_margin",style={'font-size':'22px'}),
        html.H6("%",style={'font-size':'22px'})],style={"display":"flex",
    "justify-content":"flex-start",
    "align-content":"center",
    "margin-top":"16px",
    "margin-left":"39px"}),
        #html.Span("total_sales",className="span-class")
        ], className='text-center card-color')
                    ],color="#f3f5fb",style={
                      "height":"120px","font-weight": "600"
                       })
card5=dbc.Card([
    #dbc.CardHeader("totalsales",className='text-center'),
        dbc.CardBody([
        html.Span("Orders",style={"margin-top":"-17px",
        "float":"left",
        "margin-left":"-15px",
        "font-size":"15px"}),
        html.Br(),
        html.H6(id="orders",style={'font-size':"32px"},className='margin_alignment'),
        #html.Span("total_sales",className="span-class")
        ], className='text-center card-color')
                    ],color="#f3f5fb",style={
                      "height":"120px","font-weight": "600"
                      })
card6=dbc.Card([
    #dbc.CardHeader("totalsales",className='text-center'),
        dbc.CardBody([
        html.Span("Products",style={"margin-top":"-17px",
        "float":"left",
        "margin-left":"-15px",
        "font-size":"15px"}),
        html.Br(),
        html.H6(id="products",style={'font-size':"32px"},className='margin_alignment'),
        #html.Span("M")
        #html.Span("total_sales",className="span-class")
        ], className='text-center card-color')
                    ],color="#f3f5fb",
                     style={ "height":"120px","font-weight": "600"
                      })

card7=dbc.Card([
    #dbc.CardHeader("totalsales",className='text-center'),
        dbc.CardBody([
        html.H6("Date"),
        html.Div([
    dcc.DatePickerRange(
        id='my-date-picker-range',
       min_date_allowed=min(data['order_date']),
       max_date_allowed=max(data['order_date']),
       # initial_visible_month=date(2017, 8, 5),
        start_date=min(data['order_date']),
        end_date=(max(data['order_date']))
    )],style={"margin-left":"8px"}),
        html.H6("Sub-Category"),
        dcc.Dropdown(list(data['category'].unique()),list(data['category'].unique())[0] ,id='sub-category-dropdown',clearable=False,style={"height":"10px","width":"170px","border":"none","margin-left":"4px","border-radius":"0px"}),
        html.Br(),
        html.H6("Regional Manager"),
        dcc.Dropdown(options=[],value=None,id='regional-dropdown',clearable=False,style={"height":"10px","width":"170px","border":"none","margin-left":"4px","border-radius":"0px"})
       
        ], className='app-12 text-left')
                    ],color="#f3f5fb",style={"width":"88%","margin-top":"3px","height":"191px"})
text1=dbc.Card([dbc.CardBody([dbc.Row([dbc.Col(dbc.Button('YOY', id='text-1',color="grey",n_clicks=0,
                                                          style={"font-weight":"bold","font-size":"22px"}),width=4, className="triveni"),
                                       dbc.Col(dbc.Button('QOQ', id='text-2',color="grey",n_clicks=0,
                                                          style={"font-weight":"bold","font-size":"22px"}),width=4),
                                       dbc.Col(dbc.Button('MOM', id='text-3',color="grey",n_clicks=0,
                                                          style={"font-weight":"bold","font-size":"22px"}),width=3)])],style={"padding":0})
    ],color="#d7def4",className='text-center',style={"margin-top":"-10px","font-size":"22px","font-weight":700})
# text1= button_group = dbc.ButtonGroup(
#     [
#         dbc.Button("Left",color="grey"),
#         dbc.Button("Middle",color="grey"),
#         dbc.Button("Right",color="grey"),
#     ],className="value1"
# )
text2=html.Span("YoY Sales Performance",style={"margin-top":"-17px",
        "float":"left",
        "margin-left":"-15px",
        "font-size":"15px",
        "font-weight": "600"})
text3=dcc.Graph(id="graph1",className="h-100",config= {'displayModeBar': False},figure={
            'layout': {
                'plot_bgcolor':"#f3f5fb",
                'paper_bgcolor':"#f3f5fb",
                
                 'height':400
            }
            })
text4=html.Span("Sales by Segment",style={"margin-top":"-17px",
        "float":"left",
        "margin-left":"-15px",
        "font-size":"15px",
        "font-weight": "600"})


 
text5= html.Div([
    dcc.Graph(id="graph2",className="h-100",config= {'displayModeBar': False},figure={
            'layout': {
                'plot_bgcolor':"#f3f5fb",
                'paper_bgcolor':"#f3f5fb",

                 'height':400
            }
            }),
    dcc.Interval(id='interval', interval=1000, n_intervals=0)
])
text6=html.Span("Top 20 Customers by Sales",style={"margin-top":"-17px",
        "float":"left",
        "margin-left":"-15px",
        "font-size":"15px",
        "font-weight": "600"})

text7=html.Div([dcc.Graph(id="graph3",config= {'displayModeBar': False},figure={
            'layout': {
                'plot_bgcolor':"#f3f5fb",
                'paper_bgcolor':"#f3f5fb",
                'height':400
                
            }
            }
            )],style={"max-height":"500px","overflow-x":"scroll", "position": "relative"})

card8=dbc.Card([
    #dbc.CardHeader("totalsales",className='text-center'),
        dbc.CardBody([dbc.Row([dbc.Col(text2,width=4),dbc.Col([text1],width=5)]),dbc.Row(text3)]
    )],color="#f3f5fb",style={'height':531,'margin-left':'3px'})
card9=dbc.Card([
    #dbc.CardHeader("totalsales",className='text-center'),
        dbc.CardBody([dbc.Row([dbc.Col(text4)]),dbc.Row(text5)]
    )],color="#f3f5fb",style={'height':531,'width':396})
card10=dbc.Card([
        dbc.CardBody([dbc.Row([dbc.Col(text6)]),dbc.Row(text7)]
    )],color="#f3f5fb",style={'height':300,'width':396})


#app.layout=dbc.Container([dbc.Row([dbc.Col(card1,width=10),dbc.Col(card7)]),dbc.Row([dbc.Col(card2,width=2),dbc.Col(card3,width=2),dbc.Col(card4,width=2),dbc.Col(card5,width=2),dbc.Col(card6,width=2)],className="app-header")])
app.layout=html.Div([dbc.Row([dbc.Col([dbc.Row([dbc.Col(card1)]),dbc.Row([dbc.Col(card2),dbc.Col(card3),dbc.Col(card4),dbc.Col(card5),dbc.Col(card6)],className="app-header")],width=10),dbc.Col([card7])]),dbc.Row([dbc.Col(card8,width=8),dbc.Col(card9)]),dbc.Row([dbc.Col(card10)])])
    
@app.callback(
    Output('regional-dropdown', 'options'),
    Input('sub-category-dropdown', 'value'))
def update_output(value):
    data1=data.loc[data['category']==value]
    return data1['region'].unique()
@app.callback(
    Output('regional-dropdown','value'),
    Input('regional-dropdown', 'options'))
def district_value(available_options):
    #print(available_options)
    return available_options[0]
# @app.callback(
#     Output('total_sales', 'children'),
#     Output('total_profit', 'children'),
#     Output('profit_margin', 'children'),
#     Output('orders', 'children'),
#     Output('products', 'children'),
#     Output('graph3', 'figure'),
#     Input('my-date-picker-range', 'start_date'),
#     Input('my-date-picker-range', 'end_date'),
#     Input('sub-category-dropdown','value'),
#     Input('regional-dropdown','value'))
# def result_data(start_date,end_date,sub_category,region):
#     data1=data.loc[((data['order_date']>=start_date)&(data['order_date']<=end_date))&(data['category']==sub_category)&(data['region']==region)]
#     #print(len(data1))
#     orders=data1['order_id'].count()
#     products=data1['product_name'].nunique()
    
#    # print(data1['sales'].dtypes)
#    #total sales
#     totalsales1=(data1['sales'] * data1['quantity']).sum()
#    # print(totalsales1)
#     totalsales = round(((data1['sales'] * data1['quantity']).sum())/1000000,2)
#     #totalprofit
#     data1['total_cost'] = (data1['profit'] + data1['shipping_cost']) * data1['quantity']
#     data1['total_sales_after_discount'] = ((1 - data1['discount']) * data1['sales']) * data1['quantity']
#     totalprofit = round(((data1['total_sales_after_discount'] - data1['total_cost']).sum())/1000,2)
#     # calculate marginal profit
#     data1['profit_per_unit'] = (data1['sales'] - data1['profit'] - data1['shipping_cost']) / data1['quantity']
#     data1['marginal_profit'] = (1 - data1['discount']) * data1['profit_per_unit']
#     marginalprofit = data1['marginal_profit'].sum()
#     marginalprofit =round((marginalprofit/totalsales1)*100,2)
#     customer=data1.groupby(data1['customer_name'])['sales'].sum().reset_index()
#     customer.sort_values(by='sales',inplace=True,ascending=False)
#     customer=customer.head(20)
#     figure=px.bar(customer,y=customer['customer_name'],x=customer['sales'],orientation='h')
#     return totalsales,totalprofit,marginalprofit,orders,products,figure

def update_graph(data2,sales_col,date_col,percentage_col):
    data2['sales_col1']=round((data2[sales_col]/1000000),2)
    data2['sales_col1']=data2['sales_col1'].astype('str')+'M'
    #data2[percentage_col]= data2[percentage_col].map('{:,.2f}%'.format)
    print(data2[percentage_col])
    figure = make_subplots(specs=[[{"secondary_y": True}]])
    figure.update_layout(paper_bgcolor="#f3f5fb")
    figure.update_layout(
    #        autosize=False,
    #        width=400,
            height=470)
    figure.add_trace(
       go.Scatter(name=percentage_col+'%',mode='lines+markers+text', line=dict(dash='dot'),
        marker=dict(color='black'),
        x=data2[date_col],
        y=data2[percentage_col],
        
       text=data2[percentage_col].map('{:,.2f}%'.format),
       
       textposition='bottom right',
       
       ),secondary_y=True)
       


    figure.add_trace(
           
       go.Bar(
        x=data2[date_col],
        y=data2[sales_col],
        name="Sales",
        text=data2['sales_col1'],
        textposition='outside',
        marker=dict(color="#7DC8EA",
                    ),
        

    ),secondary_y=False)
    
    figure.update_layout(
        yaxis2=dict(
            ticksuffix="%"
            #tickformat=".0%"
        )
    )
    figure.update_layout(
    legend=dict(
        orientation='h',
        x=0,
        y=1.3,
        traceorder='normal',
        font=dict(
            size=12
        )
    )
)
    return figure
# @app.callback(
#     Output('graph1', 'figure'),
#     Input('text-1', 'n_clicks'), 
#     Input('text-2', 'n_clicks'),
#     Input('text-3', 'n_clicks'),
#     State('graph1', 'figure'))
def resultant_graph(data2,n,n1,n2,current_figure):
    data1=data2.copy()
   # data1['sales']=data1['sales'].str.replace(',','')
    #data1['sales']=data1['sales'].astype(int)
   # print(text_1)
    #print(text_2)
    #print(dash.callback_context.triggered[0]['prop_id'].split('.')[0])
   # print(dash.callback_context.triggered)
    a=dash.callback_context.triggered[0]['prop_id'].split('.')[0]
    #data1['MoM Sales'] = data1['sales'].diff()
    #print(data1)
    print(a)
    #if(a=='text-1'):
    data2=data1.groupby(pd.to_datetime(data1['order_date']).dt.year)['sales'].sum().reset_index()
    data2['year']=data2['order_date'].astype('str')
    data2['yoy sales'] = data2['sales'].pct_change().mul(100).round(2)
       #data2['yoy sales'] = data2['sales'].pct_change()
      # print(data2)
       #data2['yoy sales'] = data2['yoy sales'].shift(0)
      # print(data2)
    figure=update_graph(data2,'sales','year','yoy sales')
       
    #    figure=px.bar(data2,x=data2['year'],y=data2['sales'],text=data2['yoy sales'])
    #    figure.update_traces(textposition='auto')
    #    figure.add_Scatter(x=data2['year'],y=data2['yoy sales'])
      # figure=go.Figure()
       #return figure
    if(a=='text-2'):
        #print(a)
       # data2=data1.groupby([pd.to_datetime(data1['order_date']).dt.to_period('m')])['sales'].sum().reset_index()
        data2=data1[['order_date','sales']]
       # data2['order_date']=data2['order_date'].dt.to_period('m')
        data2.set_index('order_date', inplace=True)
        data2=data2.resample('Q').sum()
        data2['quatar_sales'] = data2['sales'].pct_change().mul(100).round(2)
        data2=data2.reset_index()
        #data2['month']=pd.to_datetime(data2['order_date']).dt.month_name()
        #data2['month'] = data2.index.strftime('%B')
        #print(data2.dtypes)
        quarter_names = {1: 'Q1', 2: 'Q2', 3: 'Q3', 4: 'Q4'}
        data2['quatar']=data2['order_date'].dt.quarter.map(quarter_names)
        #print(data2)
        data2=data2.groupby(data2['quatar']).agg({'sales':'sum','quatar_sales':'sum'}).reset_index()
        #print(len(data2))
        #month_name = pd.to_datetime(month_number, format='%m').strftime('%B')
        #print(data2)
       # data2['sales_mom'] = data2['sales_mom'].map('{:.2%}'.format)

        figure=update_graph(data2,'sales','quatar','quatar_sales')
        return figure
    elif(a=='text-3'):
        data2=data1[['order_date','sales']]
       # data2['order_date']=data2['order_date'].dt.to_period('m')
        data2.set_index('order_date', inplace=True)
        data2=data2.resample('M').sum()
        data2['sales_mom'] = data2['sales'].pct_change().mul(100).round(2)
        data2=data2.reset_index()
        #data2['month']=pd.to_datetime(data2['order_date']).dt.month_name()
        #data2['month'] = data2.index.strftime('%B')
        data2=data2.groupby(data2['order_date'].dt.month).agg({'sales':'sum','sales_mom':'sum'}).reset_index()
        #print(len(data2))
        #month_name = pd.to_datetime(month_number, format='%m').strftime('%B')
        data2['month']=pd.to_datetime(data2['order_date'], format='%m').dt.month_name()
        #print(data2)
       # data2['sales_mom'] = data2['sales_mom'].map('{:.2%}'.format)

        figure=update_graph(data2,'sales','month','sales_mom')
        return figure
    #else:
    return figure   
# @app.callback(
#     Output('graph2', 'figure'),
#     Input('interval', 'n_intervals'))
def update_segment(data2):
      #data2=data.copy()
      data2['sales']=(data2['sales'] * data2['quantity'])
      data2=data2.groupby(data2['segment'])['sales'].sum().reset_index()
      #print(data2)
      figure=px.pie(data2,values=data2['sales'],names=data2['segment'].unique(),hole=.6,)
      figure.update_traces(textposition='outside', textinfo='label')
      figure.update_layout(paper_bgcolor="#f3f5fb")
      figure.update_layout(showlegend=False)
      return figure
def update_top_customers(data2):
    customer=data2.groupby(data2['customer_name'])['sales'].sum().reset_index()
    customer.sort_values(by='sales',inplace=True,ascending=False)
    customer=customer.head(20)
    figure=px.bar(customer,y=customer['customer_name'],x=customer['sales'],orientation='h',color=customer['customer_name'])
    figure.update_layout(
    margin=dict(l=10, r=20, t=0, b=0),showlegend=False
)
    return figure

@app.callback(
    Output('total_sales', 'children'),
    Output('total_profit', 'children'),
    Output('profit_margin', 'children'),
    Output('orders', 'children'),
    Output('products', 'children'),
    Output('graph1', 'figure'),
    Output('graph2', 'figure'),
    Output('graph3','figure'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),
    Input('sub-category-dropdown','value'),
    Input('regional-dropdown','value'),
    Input('text-1', 'n_clicks'), 
    Input('text-2', 'n_clicks'),
    Input('text-3', 'n_clicks'),
    State('graph1', 'figure'))
def result_data(start_date,end_date,sub_category,region,n,n1,n2,current_figure):
    data1=data.loc[((data['order_date']>=start_date)&(data['order_date']<=end_date))&(data['category']==sub_category)&(data['region']==region)]
    #print(len(data1))
    data2=data1.copy()
    orders=data1['order_id'].count()
    products=data1['product_name'].nunique()
    
   # print(data1['sales'].dtypes)
   #total sales
    totalsales1=(data1['sales'] * data1['quantity']).sum()
   # print(totalsales1)
    totalsales = round(((data1['sales'] * data1['quantity']).sum())/1000000,2)
    #totalprofit
    data1['total_cost'] = (data1['profit'] + data1['shipping_cost']) * data1['quantity']
    data1['total_sales_after_discount'] = ((1 - data1['discount']) * data1['sales']) * data1['quantity']
    totalprofit = round(((data1['total_sales_after_discount'] - data1['total_cost']).sum())/1000,2)
    # calculate marginal profit
    data1['profit_per_unit'] = (data1['sales'] - data1['profit'] - data1['shipping_cost']) / data1['quantity']
    data1['marginal_profit'] = (1 - data1['discount']) * data1['profit_per_unit']
    marginalprofit = data1['marginal_profit'].sum()
    marginalprofit =round((marginalprofit/totalsales1)*100,2)
    customer=data1.groupby(data1['customer_name'])['sales'].sum().reset_index()
    customer.sort_values(by='sales',inplace=True,ascending=False)
    customer=customer.head(20)
    figure1=resultant_graph(data2,n,n1,n2,current_figure)
    figure2=update_segment(data2)
    figure3=update_top_customers(data2)
    
    
    
    return totalsales,totalprofit,marginalprofit,orders,products,figure1,figure2,figure3

 
if __name__ == '__main__':
    app.run_server(debug=True)    