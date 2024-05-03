from dash import dcc, html, Output, Input, State


def create_layout(app_pathname):
    layout = html.Div([
        html.Div(id='dash-output'),
        dcc.Input(id='dash-input'),
        html.Div([html.A(href=app_pathname + "/", children='Go back to the Dash app.'),
                  html.Br(),
                  html.A(href="/api", children='Go to the Flask app.'),
                  ],
                 ),
    ])

    return layout
