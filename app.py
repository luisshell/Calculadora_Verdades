import itertools
from flask import Flask, render_template, request
from sympy import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])

# # Función que evalúa una expresión lógica
# def evaluar_expresion(expresion, variables):
#     # Crea un diccionario para asignar valores a las variables
#     asignaciones = dict(zip(variables, range(len(variables))))

# def generar_tabla_verdad(expresion, variables):
#     # Crea una lista con todas las posibles asignaciones de valores a las variables
#     valores = list(itertools.product([0, 1], repeat=len(variables)))
    
# #     # Crea una lista para almacenar los resultados de la evaluación de la expresión para cada asignación de valores
# #     resultados = []
# #     for valor in valores:
# #         resultado = evaluar_expresion(expresion, dict(zip(variables, valor)))
# #         resultados.append(resultado)
       
#     Tabla=generar_tabla_verdad(expresion, variables)

def calcular():
    proposicion = request.form['proposicion']
    valor_verdad = evaluar_proposicion(proposicion)
    return render_template('resultado.html', proposicion=proposicion, valor_verdad=valor_verdad)

def evaluar_proposicion(proposicion):
    # Convertir la proposición a una expresión booleana
    expr = sympify(proposicion)
    # Evaluar la expresión
    valor_verdad = bool(expr)
    return valor_verdad

if __name__ == '__main__':
    app.run(debug=True)
    