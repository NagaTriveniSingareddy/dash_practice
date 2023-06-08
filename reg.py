# # import re
# # a="triVe123@#.srt456"
# # b=re.split("[^a-z0-9]",a,0,re.IGNORECASE)
# # #print(b)
# # normal_string=''.join(filter(str.isalnum, a))
# # print(normal_string)
# class person:
#     def __init__(self) -> None:
#         pass
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.graph_objects as go

# app = dash.Dash(__name__)

# app.layout = html.Div([
#     dcc.Graph(
#         id='bar-graph',
#         figure={
#             'data': [
#                 {'x': ['Category 1', 'Category 2', 'Category 3'],
#                  'y': [1000, 2000, 3000],
#                  'type': 'bar'}
#             ],
#             'layout': go.Layout(
#                 yaxis={
#                     'ticktext': ['1K', '2K', '3K'],
#                     'tickvals': [1000, 2000, 3000]
#                 }
#             )
#         }
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.graph_objects as go
# import plotly.express as px

# app = dash.Dash(__name__)

# # Sample data
# data = {'Category': ['Category 1', 'Category 2', 'Category 3'],
#         'Value': [20, 35, 25]}

# # Create a bar graph
# fig = px.bar(data, x='Category', y='Value')

# fig.update_layout(
#     title='Bar Graph with Line',
#     xaxis_title='Categories',
#     yaxis_title='Values'
# )

# # Get maximum value for line position
# max_value = data['Value'].max()

# Add a line shape above the graph based on the maximum value
# fig.add_shape(
#     type='line',
#     x0=0,
#     y0=max_value + 5,  # Position the line slightly above the highest bar
#     x1=len(data['Category']),
#     y1=max_value + 5,
#     line=dict(
#         color='red',
#         width=2,
#         dash='dash'
#     )
# )

# app.layout = html.Div([
#     dcc.Graph(
#         id='bar-graph',
#         figure=fig
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

app = dash.Dash(__name__)

# Sample data
x = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']
y = [20, 35, 25, 40, 30]

# Create a bar trace
bar_trace = go.Bar(
    x=x,
    y=y,
    name='Bar Graph'
)

# Create a line trace for the trendline
trend_trace = go.Scatter(
    x=x,
    y=[sum(y) / len(y)] * len(y),  # Trendline value is the average of all bar values
    mode='lines',
    name='Trendline'
)

data = [bar_trace, trend_trace]

layout = go.Layout(
    title='Bar Graph with Trendline',
    xaxis={'title': 'Categories'},
    yaxis={'title': 'Values'}
)

fig = go.Figure(data=data, layout=layout)

app.layout = html.Div([
    dcc.Graph(
        id='bar-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
