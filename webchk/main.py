from flask import Flask, request, render_template, make_response
from api.api4 import api_bp4
import random

app = Flask(__name__)

@app.route('/')
def index():
    resp =  make_response(render_template('index.html'))
    resp.set_cookie('availiblity', 'gstatics_'+str(random.randint(1000000000000000, 9999999999999999)))
    return resp


app.register_blueprint(api_bp4)
app.run(debug=False,host='0.0.0.0', port=8080)
