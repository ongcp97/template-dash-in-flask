from dash import dcc, html, Output, Input, State


def create_layout(app_pathname):
    layout = html.Div([
        html.H1('Dash Application'),
        html.Div('This is a Dash app running inside of Flask.'),
        html.A(href=app_pathname + '/page1', children='Go to Page1 of the Dash app.'),
        html.Br(),
        html.A(href="/api", children='Go to the Flask app.'),

    ])
    return layout
