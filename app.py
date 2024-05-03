from flask import Flask, render_template
from plotly_dash.dash_flask_integrator import init_dash

app = Flask(__name__)
DASH_APP_BASE_PATHNAME = ''

@app.route('/api')
def flask_home():
    return render_template('api.html', DASH_APP_BASE_PATHNAME = DASH_APP_BASE_PATHNAME+'/')

if __name__ == '__main__':
    dash_app = init_dash(app, DASH_APP_BASE_PATHNAME)
    app.run(debug=False)
