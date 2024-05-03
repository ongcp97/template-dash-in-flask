# Reusable Dash in Flask Template
1. This is a template for a Flask app that allows routing to an embedded Dash app.
2. Run app.py to initialize the app. This both initiates the Dash app, its required callbacks, and the Flask server.
3. The logic of the Dash app is contained within the dash_app folder.
4. All Dash callbacks have to be contained within the function integrate_callbacks() in plotly_dash/dash_app/index.py.
