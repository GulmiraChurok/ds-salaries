from dash import Dash, html             
import dash_bootstrap_components as dbc
from util import get_data
from layout import create_layout
import os

PATH = os.path.join(os.getcwd(), "salaries.csv")

data = get_data(PATH)

app = Dash(external_stylesheets=[dbc.themes.CYBORG])
server = app.server
app.title = "Data Science Salary"

app.layout = create_layout(app,data)


app.run_server(debug=True)
