from dash import dcc, html, Output, Input, State
import dash_mantine_components as dmc


def create_layout():
    layout = dmc.MantineProvider(
        forceColorScheme="light",
        theme={
            "primaryColor": "indigo",
            "fontFamily": "'Inter', sans-serif",
            "components": {
                "Button": {"defaultProps": {"fw": 400}},
                "Alert": {"styles": {"title": {"fontWeight": 500}}},
                "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
                "Badge": {"styles": {"root": {"fontWeight": 500}}},
                "Progress": {"styles": {"label": {"fontWeight": 500}}},
                "RingProgress": {"styles": {"label": {"fontWeight": 500}}},
                "CodeHighlightTabs": {"styles": {"file": {"padding": 12}}},
                "Table": {
                    "defaultProps": {
                        "highlightOnHover": True,
                        "withTableBorder": True,
                        "verticalSpacing": "sm",
                        "horizontalSpacing": "md",
                    }
                },
            },
        },
        children=[
            html.Div(id='dash-page-content'),
            dcc.Location(id='dash-url'),
        ],
    )

    return layout
