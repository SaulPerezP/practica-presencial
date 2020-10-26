from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/suma', methods=['POST'])
def suma():

	if request.method == 'POST':

		response = {}

		a = request.form.get('a')
		b = request.form.get('b')

		resultado = float(a) + float(b)

		response["fecha"] = datetime.now()
		response["a"] = a
		response["b"] = b
		response["tipoOperación"] = "suma"
		response["respuesta"] = str(resultado)

		return response

	

@app.route('/resta', methods=['POST'])
def resta():

	if request.method == 'POST':

		response = {}

		a = request.form.get('a')
		b = request.form.get('b')

		resultado = float(a) - float(b)

		response["fecha"] = datetime.now()
		response["a"] = a
		response["b"] = b
		response["tipoOperación"] = "resta"
		response["respuesta"] = str(resultado)

		return response



@app.route('/multiplicacion', methods=['POST'])
def multiplicacion():	

	if request.method == 'POST':

		response = {}

		a = request.form.get('a')
		b = request.form.get('b')

		resultado = float(a) * float(b)

		response["fecha"] = datetime.now()
		response["a"] = a
		response["b"] = b
		response["tipoOperación"] = "multiplicación"
		response["respuesta"] = str(resultado)

		return response




@app.route('/division', methods=['POST'])
def division():	
	
	if request.method == 'POST':

		response = {}

		a = request.form.get('a')
		b = request.form.get('b')

		resultado = float(a) / float(b)

		response["fecha"] = datetime.now()
		response["a"] = a
		response["b"] = b
		response["tipoOperación"] = "división"
		response["respuesta"] = str(resultado)

		return response


@app.route('/potencia', methods=['POST'])
def potencia():	

	if request.method == 'POST':

		response = {}

		a = request.form.get('a')
		b = request.form.get('b')

		var_a = float(a)
		var_b = float(b)

		resultado = pow(var_a,var_b)

		response["fecha"] = datetime.now()
		response["a"] = a
		response["b"] = b
		response["tipoOperación"] = "potencia"
		response["respuesta"] = str(resultado)

		return str(resultado)


@app.route('/raiz', methods=['POST'])
def raiz():	
	
	if request.method == 'POST':

		response = {}

		a = request.form.get('a')
		b = request.form.get('b')

		var_a = float(a)
		var_b = float(b)

		resultado = float(var_b)**(1/float(var_a))

		response["fecha"] = datetime.now()
		response["a"] = a
		response["b"] = b
		response["tipoOperación"] = "raíz"
		response["respuesta"] = str(resultado)

		return str(resultado)

@app.route('/historial', methods=['GET'])
def historial():

	if request.method == 'GET':

		fecha = datetime.now()

		return fecha


if __name__ == "__main__":
	app.run(threaded=True, port=5000,debug=True)		