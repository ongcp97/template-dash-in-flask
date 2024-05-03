from dash import Dash

def create_dash_app(server, app_pathname):
    external_stylesheets = [
    ]

    dash_app = Dash(__name__,
                    server=server,
                    title='Dash in Flask',
                    url_base_pathname=app_pathname + '/',
                    external_stylesheets=external_stylesheets)

    return dash_app
