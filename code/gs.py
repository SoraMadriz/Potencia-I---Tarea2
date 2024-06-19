import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd
import pdb

def run():
#Declaracidon de variables
    x,y,z = sp.symbols('x y z')
#Declaracion de funciones (x=g1);(y=g2)
    g1 = sp.sympify((x**2+y**2+8)/10)
    g2 = sp.sympify((x*y**2+x+8)/10)
#Algoritmo de Jacobi
    #Condiciones iniciales
    i = 0
    x0 = 0
    y0 = 0
    error = 1000
    #Lista de la salida
    iteraciones = []
    x_values = []
    y_values = []
    error_values = []
    #Parte iterativa
    while True:
        #Calculo de los nuevos valores
        x_iter = g1.subs({x: x0, y: y0})
        y_iter = g2.subs({x: x_iter, y: y0})
        error = max(abs(x_iter - x0),abs(y_iter - y0))
        #Agregar valores a los arrays de salida
        iteraciones.append(i)
        x_values.append("{:.4f}".format(x0))
        y_values.append("{:.4f}".format(y0))
        error_values.append("{:.4f}".format(float(error)))
        #Condicion para reiterar
        if (error < 10e-4) or (i >50):
            break
        else:
           #Actualizacion de variables
           i += 1
           x0 = x_iter
           y0 = y_iter

#Guardado de los valores en latex
    error_values.pop()
    error_values.insert(0,"")
    df = pd.DataFrame({
        'ITERACIONES': iteraciones,
        'X' : x_values,
        'Y' : y_values,
        'ERROR': error_values
    })

    latex_table = df.to_latex(index=False, caption="Método de Jacobi", label="Jacobi Table")
    print(latex_table)

    

if __name__ == "__main__":
    run()
