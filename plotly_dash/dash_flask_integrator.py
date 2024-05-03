from flask import Flask

from plotly_dash.dash_app.app import create_dash_app
from plotly_dash.dash_app.index import create_layout
from plotly_dash.dash_app.callbacks import integrate_callbacks

def init_dash(server: Flask, app_pathname):
    dash_app = create_dash_app(server, app_pathname)
    dash_app.layout = create_layout()
    integrate_callbacks(dash_app, app_pathname)
    return dash_app
