import dash
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash()

app.layout = html.Div([
    html.A('Text 1', id='text-1', n_clicks=0),
    html.A('Text 2', id='text-2', n_clicks=0),
    html.Div(id='output')
])

@app.callback(
    Output('output', 'children'),
    Input('text-1', 'n_clicks'),
    Input('text-2', 'n_clicks'),
    State('text-1', 'children'),
    State('text-2', 'children')
)
def update_output(text1_clicks, text2_clicks, text1_value, text2_value):
    print(text1_value)
    # if text1_clicks is None:
    #     text1_clicks = 0
    # if text2_clicks is None:
    #     text2_clicks = 0
    # if text1_clicks > 0:
    #     return f'You clicked "{text1_value}"'
    # elif text2_clicks > 0:
    #     return f'You clicked "{text2_value}"'
    # else:
    #     return 'Click a text'
    return text1_clicks,text2_clicks

if __name__ == '__main__':
    app.run_server(debug=True)
