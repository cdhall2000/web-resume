from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__, static_folder="public_html/static", template_folder="public_html")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<variable>")
def index_variable(variable):
    if variable == None: print('variable is none!')
    if variable == 'testing' : return 'Hello World!'
    else: 
        return render_template('index.html', var1 = escape(variable))
