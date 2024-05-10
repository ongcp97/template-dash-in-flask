import dash


def create_dash_app(server, app_pathname):
    external_stylesheets = [
    ]
    dash._dash_renderer._set_react_version('18.2.0')
    dash_app = dash.Dash(__name__,
                         server=server,
                         title='Dash in Flask',
                         url_base_pathname=app_pathname + '/',
                         external_stylesheets=external_stylesheets)

    return dash_app
