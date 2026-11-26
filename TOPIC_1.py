from dash import Dash, dcc, html, Output, Input
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

server = app.server

my_text = dcc.Input(value='Type Text new now')
my_layout = dcc.Markdown(children='')

app.layout = dbc.Container([
    my_text,
    my_layout
])

@app.callback(
    Output(my_layout, 'children'),
    Input(my_text, 'value')
)
def update_text(el_texto):
    return el_texto

if __name__ == '__main__':
    app.run(debug=True)