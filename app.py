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

		response["1.fecha"] = datetime.now()
		response["2.a"] = a
		response["3.b"] = b
		response["4.tipoOperación"] = "suma"
		response["5.respuesta"] = str(resultado)

		return response


@app.route('/resta', methods=['POST'])
def resta():

	if request.method == 'POST':

		response = {}

		a = request.form.get('a')
		b = request.form.get('b')

		resultado = float(a) - float(b)

		response["1.fecha"] = datetime.now()
		response["2.a"] = a
		response["3.b"] = b
		response["4.tipoOperación"] = "resta"
		response["5.respuesta"] = str(resultado)

		return response



@app.route('/multiplicacion', methods=['POST'])
def multiplicacion():	

	if request.method == 'POST':

		response = {}

		a = request.form.get('a')
		b = request.form.get('b')

		resultado = float(a) * float(b)

		response["1.fecha"] = datetime.now()
		response["2.a"] = a
		response["3.b"] = b
		response["4.tipoOperación"] = "multiplicación"
		response["5.respuesta"] = str(resultado)

		return response


@app.route('/division', methods=['POST'])
def division():	
	
	if request.method == 'POST':

		response = {}

		a = request.form.get('a')
		b = request.form.get('b')

		resultado = float(a) / float(b)

		response["1.fecha"] = datetime.now()
		response["2.a"] = a
		response["3.b"] = b
		response["4.tipoOperación"] = "división"
		response["5.respuesta"] = str(resultado)

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

		response["1.fecha"] = datetime.now()
		response["2.a"] = a
		response["3.b"] = b
		response["4.tipoOperación"] = "potencia"
		response["5.respuesta"] = str(resultado)

		return response


@app.route('/raiz', methods=['POST'])
def raiz():	
	
	if request.method == 'POST':

		response = {}

		a = request.form.get('a')
		b = request.form.get('b')

		var_a = float(a)
		var_b = float(b)

		resultado = float(var_b)**(1/float(var_a))

		response["1.fecha"] = datetime.now()
		response["2.a"] = a
		response["3.b"] = b
		response["4.tipoOperación"] = "raíz"
		response["5.respuesta"] = str(resultado)

		return response

@app.route('/historial', methods=['GET'])
def historial():

	if request.method == 'GET':

		fecha = datetime.now()

		return fecha


if __name__ == "__main__":
	app.run(threaded=True, port=5000,debug=True)		