# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
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