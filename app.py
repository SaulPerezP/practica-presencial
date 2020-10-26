from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/suma', methods=['POST'])
def suma():

	if request.method == 'POST':

		a = request.form.get('a')
		b = request.form.get('b')

		resultado = float(a) + float(b)

		return str(resultado)

	

@app.route('/resta', methods=['POST'])
def resta():

	if request.method == 'POST':

		a = request.form.get('a')
		b = request.form.get('b')

		resultado = float(a) - float(b)

		return str(resultado)



@app.route('/multiplicacion', methods=['POST', 'GET'])
def multiplicacion():	

	if request.method == 'POST':

		return "TRue"




@app.route('/division', methods=['POST', 'GET'])
def division():	
	
	if request.method == 'POST':

		return "TRue"	


@app.route('/potencia', methods=['POST', 'GET'])
def potencia():	

	if request.method == 'POST':

		return "TRue"


@app.route('/raiz', methods=['POST', 'GET'])
def raiz():	
	
	if request.method == 'POST':

		return "TRue"	


if __name__ == "__main__":
	app.run(threaded=True, port=5000,debug=True)		