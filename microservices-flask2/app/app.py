# compose_flask/app.py
# https://runnable.com/docker/python/docker-compose-with-flask-apps
# https://stackoverflow.com/questions/42316511/communication-between-two-flask-services-in-docker
# https://github.com/eelkevdbos/microservices-flask/blob/master/concat/concat.py
from flask import Flask
from flask import render_template,request,make_response
import requests

app = Flask(__name__)

@app.route('/send', methods=['POST', 'GET'])
def send():
	if request.form['action'] == '+':
	    #COMUNICARSE CON SUMA.PY
	    #num1 = int(request.form["num1"])
		#num2 = int(request.form["num2"])
		suma=requests.get('http://suma:5000/').text;
		return render_template('/show_all.html', string_variable=suma)
	elif request.form['action'] == '-':
		return render_template('/show_all.html', string_variable=suma)
	    #COMUNICARSE CON RESTA.PY
	elif request.form['action'] == '*':
		return render_template('/show_all.html', string_variable=suma)
	    #COMUNICARSE CON MULTIPLICACION.PY
	elif request.form['action'] == '/':
	    #COMUNICARSE CON DIVISION.PY
		return render_template('/show_all.html', string_variable=suma)


@app.route('/show_all')
def show_all():
    	return render_template('show_all.html')

if __name__ == "__main__":
    	app.run(host="0.0.0.0", debug=True)


