import pandas as pd
from dash import Dash, dcc, html, Input, Output,dash_table
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_table_experiments as dt

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
server=app.server
data=pd.read_csv("APY.csv")
#print(len(data))
card2=dbc.Card([
    dbc.CardBody([dbc.Row([dbc.Col(dcc.Dropdown(data['State'].unique(),'Andhra Pradesh',
                                id='dropdown_id1'),width=5)]),
                                dbc.Row(dcc.Graph(id="graph_id1"))
                
   
    ])],style={'margin-top':'10px'})
card3=dbc.Card([
    dbc.CardBody([dbc.Row([dbc.Col(dcc.Dropdown(
                                id='dropdown_id2',options=[], value=None),width=4)]),
                                dbc.Row(dcc.Graph(id="graph_id2"))
                
   
    ])],style={'margin-top':'10px'})
#card3=dbc.Card([dbc.CardBody([html.H4("result table",style={'text-align':"center"}),html.Div([html.Div(id='tb1')])])])
#card2=dbc.Card([dbc.Row([dbc.Col(dcc.Dropdown(data['State'].unique(),'Andhra Pradesh',id='dropdown_id1'))])])
app.layout=dbc.Container(
    [dbc.Row([html.H4("sample demo app")],style={'text-align':'center'}),
        dbc.Row([dbc.Col([card2],width=6),dbc.Col([card3],width=6)])])
            
@app.callback(
    Output('dropdown_id2','options'),
    #Output('dropdown_id2','options'),
    Input('dropdown_id1', 'value'))

def callback_func(dropdown_value):
    data1=data.loc[data['State']==dropdown_value]
    #print(data1)
    data1=data1.reset_index()
   # print(data1.columns)
    #print(data1['District '])
    result=[i for i in data1['District '].unique()]
   # print(result)
    return result
@app.callback(
    Output('dropdown_id2', 'value'),
    Input('dropdown_id2', 'options'))
def district_value(available_options):
    #print(available_options)
    return available_options[0]
@app.callback(
    Output('graph_id1','figure'),
    Input('dropdown_id1', 'value'),
    )
    
def callback_func(x1):
    #print(x1,x2)
    data1=data.loc[data['State']==x1]
    data1=data1.groupby('District ')['Yield'].sum().reset_index(name='total_yield')
    fig=px.bar(data1,y='total_yield',x='District ')
    #fig = px.bar(dff, x='country', y='count',color='country')
    # else:
    #      data1=data.loc[((data['State'])==x1)&(data['District ']==x2)]
    #      data1=data1.groupby('Crop')['Yield'].sum().reset_index(name='total_yield')
    #      fig=px.bar(data1,x='total_yield',y='Crop')

    return fig
@app.callback(
    Output('graph_id2','figure'),
    Input('dropdown_id1', 'value'),
    Input('dropdown_id2', 'value') )
    
def callback_func1(x1,x2):

    data1=data.loc[((data['State'])==x1)&(data['District ']==x2)]
    data1=data1.groupby('Crop')['Yield'].sum().reset_index(name='total_yield')
    fig=px.bar(data1,x='total_yield',y='Crop')
    #fig = px.pie(data1, values='total_yield', names='Crop', title='Population of European continent')
    return fig
# @app.callback(
#     Output('tb1','children'),
#     Input('dropdown_id1','value'))
# def district_value(table_value):
#     data1=data.loc[data['State']==table_value]
#     data1=data1.head(10)
#     data2= data1.to_dict('rows')
#     columns =  [{"name": i, "id": i,} for i in (data1.columns)]
#     val=dash_table.DataTable(data=data2, columns=columns,
#                              css=[{'selector': 'table', 'rule': 'table-layout: fixed'}],
#                              style_header={
#         'overflow': 'hidden',
#         'textOverflow': 'ellipsis',
#         'maxWidth': 0},
#                              style_cell={
#           'overflow': 'hidden',
#         'textOverflow': 'ellipsis'}
#         )
#     return val
    

if __name__ == '__main__':
    app.run_server(debug=True)    
        
