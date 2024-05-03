from dash import dcc, html, Output, Input, State
from plotly_dash.dash_app.apps import home, page1


def integrate_callbacks(app, app_pathname):
    """
    CONSOLIDATE ALL CALLBACKS HERE
    """

    # """
    # CALLBACKS FOR
    # index.py
    # """
    @app.callback(
        Output('dash-page-content', 'children'),
        Input('dash-url', 'pathname')
    )
    def render_content(url):
        dash_url = url.replace(app_pathname, "", 1)
        print(dash_url)

        if dash_url == '/':
            return home.create_layout(app_pathname)

        elif dash_url == '/page1':
            return page1.create_layout(app_pathname)

        else:
            return '404'

    # """
    # CALLBACKS FOR
    # apps/page1.py
    # """
    @app.callback(
        Output('dash-output', 'children'),
        Input('dash-input', 'value')
    )
    def render_content(value):
        return [value]
