# import sys

# print("Python version")

# print (sys.version)

# print("Version info.")

# print (sys.version_info)
import numpy as np
import pandas as pd
# arr=np.zeros((2,3))
# print(arr)
# print(arr.reshape(3,2))

# arr1=np.array([[1,2,3],[4,5,6]])
# print(arr1.T)
# data = {
#     'sales': [100, 150, 120, 200, 180, 220, 250, 300, 280, 320, 350, 400],
#     'month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
#     'year': [2019, 2019, 2019, 2019, 2020, 2020, 2020, 2020, 2021, 2021, 2021, 2021]
# }

# df = pd.DataFrame(data)
# df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'].astype(str), format='%Y-%m')
# df = df.sort_values('date')
# df = df.sort_values('date')
# print(df)
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots

# # Sample data
# categories = ['A', 'B', 'C', 'D']
# values = [100, 200, 300, 400]
# percentages = [10, 20, 30, 40]

# # Create subplots with two y-axes
# fig = make_subplots(specs=[[{"secondary_y": True}]])

# # Add bar trace for values on the left side
# fig.add_trace(
#     go.Bar(x=categories, y=values, name='Values'),
#     secondary_y=False
# )

# # Add scatter trace for percentages on the right side
# fig.add_trace(
#     go.Scatter(x=categories, y=percentages, name='Percentages',yaxis='y2', mode='markers+lines'),
#     secondary_y=True
# )
# fig.update_layout(
#         yaxis2=dict(
#             ticksuffix="%"))
# # Set y-axis labels
# fig.update_yaxes(title_text="Values", secondary_y=False)
# fig.update_yaxes(title_text="Percentages (%)", secondary_y=True)

# # Set layout title
# fig.update_layout(title='Values and Percentages')

# # Show the plot
# fig.show()
import pandas as pd

# Sample data
# data = {
#     'date': ['2019-01-01', '2019-02-01', '2019-03-01', '2019-04-01', '2019-05-01', '2019-06-01',
#              '2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01',
#              '2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01', '2021-06-01',
#              '2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01', '2022-06-01'],
#     'sales': [1000, 1500, 2000, 1800, 2500, 3000,
#               1200, 1800, 2200, 1900, 2600, 3200,
#               1100, 1600, 1900, 1700, 2300, 2700,
#               1300, 1700, 2100, 2000, 2800, 3400]
# }

# # Create a DataFrame
# df = pd.DataFrame(data)

# # Convert date column to datetime format
# df['date'] = pd.to_datetime(df['date'])

# # Set date column as the index
# df.set_index('date', inplace=True)

# # Group by month and year, and calculate the sum of sales
# monthly_sales = df.resample('M').sum().reset_index()
# #print(monthly_sales)
# # Calculate the month-over-month sales percentage change
# monthly_sales['sales_mom'] = monthly_sales['sales'].pct_change()

# # Print the result
# print(monthly_sales)
import pandas as pd

# Sample data
# data = {
#     'float_column': [0.123, 0.456, 0.789]
# }

# # Create a DataFrame
# df = pd.DataFrame(data)

# # Add percentage symbol to float values in column
# df['percentage_column'] = df['float_column'].apply(lambda x: '{:.0%}'.format(x))

# # Print the DataFrame
# print(df)
# value = 85.09
# string_value = str(value)

# print(string_value)
# nums=[1,2,3,4,5,6]
# l1=[]
# l1+=[5]*3
# nums=l1
# print(nums)
# print(type(l1))
# a=["this","is","triveni"]
# a=[i[::-1] for i in a]
# print(a)
# import plotly.express as px
# import pandas as pd

# # Create some example data
# import dash
# import plotly.graph_objects as go
# from dash import html, dcc
# import numpy as np

# df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
# fig = px.bar(df, x='pop', y='country', text_auto='.2s',orientation='h', height=2000)
# fig.update_traces(width=1)
# fig.update_xaxes(range=[0, 90000000],title=None)

# df2=df[df['country']=='Bosnia and Herzegovina']
# fig2 = px.bar(df2,x='pop',y='country',orientation='h', height=35, text_auto='.2s')
# fig2.update_layout(yaxis = dict(color = 'white'))
# fig2.update_xaxes(range=[0, 90000000])
# fig2.update_yaxes(title=None)

# # app and layout
# app = dash.Dash(__name__)
# app.layout = html.Div([
#     html.Div([
#     dcc.Graph(
#         figure=fig),
# ],style={'overflow-y':'auto', 'height':500}),
# # dcc.Graph(
# #         figure=fig2),
# ])
# if __name__ == '__main__':
# #     app.run(debug=False)
# import dash
# import plotly.graph_objects as go
# from dash import html, dcc
# import numpy as np

# # create data, lots of bars
# data = np.arange(200)

# # app and layout
# app = dash.Dash(__name__)
# app.layout = html.Div(
#     [
#         html.Div(
#             dcc.Graph(
#                 figure=go.Figure(
#                     data=go.Bar(
#                         y=data,
#                         orientation='h'
#                     ),
#                     layout={'height': 10000}
#                     # ^^ adapt the height to your needs so that the bars
#                     #    show the desired thickness
#                 )
#             ),
#             className='scroll'
#             # ^^ custom css in the assets folder
#         )
#     ],
# )

# if __name__ == '__main__':
#     app.run(debug=True)
# import plotly.graph_objects as go

# # Create some example data
# x = [1, 2, 3, 4, 5]
# y = [1, 2, 3, 4, 5]

# # Create a scatter trace
# trace = go.Scatter(x=x, y=y)

# # Create layout with fixed range on y-axis
# layout = go.Layout(
#     yaxis=dict(
#         range=[0, 10],  # Set the desired range on the y-axis
#         fixedrange=True  # To disable zooming vertically
#     )
# )

# # Create figure and add the trace and layout
# fig = go.Figure(data=[trace], layout=layout)

# # Show the plot
# fig.show()
# import plotly.graph_objects as go

# # Create some example data
# x = [1, 2, 3, 4, 5]
# y = [1, 2, 3, 4, 5]

# # Create a scatter trace
# trace = go.Scatter(x=x, y=y)

# # Create layout with fixed range on y-axis
# layout = go.Layout(
#     yaxis=dict(
#         range=[0, 10],  # Set the desired range on the y-axis
#         fixedrange=True  # To disable zooming vertically
#     )
# )

# # Create figure and add the trace and layout
# fig = go.Figure(data=[trace], layout=layout)

# # Show the plot
# fig.show()

# import re
# a=int(input())
# try:
#     if re.compile(r"\d{3}",a):
#        print('yes')
# except:
#       print('no')      
#print(list(range(10,20)))
#print(list(range(["01:00","02:00"])))
# event1 = ["01:15","02:00"]
# event2 = ["02:00","03:00"]
# event1=[((int(i.split(":")[0])*60)+(int(i.split(":")[1])//60)) for i in event1]
# event2=[((int(i.split(":")[0])*60)+(int(i.split(":")[1])//60)) for i in event2]
# print(event1)
# print(event2)
# print(list(range(event1[0],event1[1]+1)))
# a=[[1,2],[1,2,3,4,5],[1,2,3],[1]]
# b={len(i):i for i in a} 
# print(b)
# print(dict(sorted(b.items())).getvalues())
#a=[10,20,30,5,15]
#b=[11,15,35,6,17]
#n=4
# n = 5
# x = 3 
# y = 3
# a = [1, 2, 3, 4, 5]
# b = [5, 4, 3, 2, 1]
# n = 8
# a= [1, 4, 3, 2, 7, 5, 9, 6]
# b= [1, 2, 3, 6, 5, 4, 9, 8]
# l1=[]
# # for i in range(len(a)):
# #     if(a[i]>b[i]):
# #         l1.append(a[i])
# #     else:
# #         l1.append(b[i])    
# # print(l1)
# # l1.sort(reverse=True)
# # print(sum(l1[:n+1]))
# l1=[[1],[1,3,4],[2,3,4,5,6],[1,2],[2]]
# print(sorted(l1,key=lambda x :len(x)))
# print(l1.sort(key=lambda x :len(x))) 
# data={'a':'abc',
#       'b':'def',
#       'c':{'test':1}}
# value='test'
# #print(data.keys())
# for i in data:
#     if(i==value):
#         print(data[i])
#     elif:
nums = [0,1,2,2,4,4,1]
nums = [n for n in nums if n % 2 == 0]
nums.sort()
print(nums)
print(max(nums,key=nums.count) )
#max(nums,key=nums.count) if len(nums) > 0 else -1
    
    