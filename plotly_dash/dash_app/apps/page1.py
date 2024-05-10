from dash import dcc, html, Output, Input, State
import dash_mantine_components as dmc


def create_layout(app_pathname):
    layout = html.Div([
        html.Div(id='dash-output'),
        dcc.Input(id='dash-input'),
        dmc.Drawer(
            title="Drawer Example",
            id="drawer-simple",
            padding="md",
            zIndex=10000,
        ),
        html.Div([html.A(href=app_pathname + "/", children='Go back to the Dash app.'),
                  html.Br(),
                  html.A(href="/api", children='Go to the Flask app.'),
                  ],
                 ),
        dmc.Button("Open Drawer", id="drawer-demo-button"),
    ])

    return layout
