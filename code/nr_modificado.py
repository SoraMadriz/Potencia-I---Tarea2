import sympy as sp
import pandas as pd
import pdb

def run():
#DECLARACIONES DE LAS VARIABLES
    x,y = sp.symbols('x y')

#DECLARACIONES DE FUNCIONES
    f1 = sp.sympify(x**2-10*x+y**2+8)
    f2 = sp.sympify(x*y**2 + x - 10*y+8)

#CONDICIONES INICIALES
    i = 0; x_i = sp.Matrix([0, 0]); error_x=100; error_f=100

#LISTA DE SALIDAS
    iteraciones=[]; x_values=[]; y_values=[]; f1_values=[]; f2_values=[];
    error_x_values = []; error_f_values = []

#ELEMENTOS DEL METODO NEWTON-RAPHSON
    X = sp.Matrix([0,0])
    F = sp.Matrix([f1, f2])
    X=sp.Matrix(list(map(float,X)))
    x_salida = x_i
#ITERACIONES DEL MÉTODO NR
    while True:
    #CALCULO REQUERIDO {X = X0 -(JB^-1)*F}
        F_output = F.subs({x:x_salida[0],y:x_salida[1]})                        
        F_output=sp.Matrix(list(map(float,F_output)))
        df1dx = F[0].diff(x)
        df2dy = F[1].diff(y)
        X[0] = x_salida[0] - ((F_output[0])/(df1dx.subs({x:x_salida[0],y:x_salida[1]})))
        G_output = F[1].subs({x:X[0],y:x_salida[1]})                            
        X[1] = x_salida[1] - ((G_output)/(df2dy.subs({x:X[0],y:x_salida[1]})))
        X = X.evalf()                                                 
        G_output = F.subs({x:X[0],y:X[1]})                            
        error_X = float(max(abs(X[0]-x_salida[0]),abs(X[1]-x_salida[1])))       
        error_F = float(max(abs(G_output[0]-F_output[0]),abs(G_output[1]-F_output[1])))
        print(f'El valor de la matrix X: {X}')
        print(f'El valor de la matrix x_i: {x_salida}')


    #AÑADIR VALORES A LISTA DE SALIDA
        iteraciones.append(i)
        x_values.append("{:.4f}".format(x_salida[0]))
        y_values.append('{:.4f}'.format(x_salida[1]))
        f1_values.append('{:-4f}'.format(float(F_output[0])))
        f2_values.append('{:-4f}'.format(float(F_output[1])))
        error_x_values.append('{:-4f}'.format(error_X))
        error_f_values.append('{:-4f}'.format(error_F))


    #CONDICIONES DE REITERACION
        if ((error_X < 10e-4) and (error_F < 10e-4)) or (i>10):
            iteraciones.append(i+1)
            x_values.append("{:.4f}".format(X[0]))
            y_values.append('{:.4f}'.format(X[1])); #pdb.set_trace()
            f1_values.append('{:-4f}'.format(float(G_output[0])))
            f2_values.append('{:-4f}'.format(float(G_output[1])))
            break
        else:
        #ACTUALIZACION DE VARIABLES
            #pdb.set_trace()
            x_salida[0] = X[0]
            x_salida[1] = X[1]
            i += 1;
            continue

    #ESCRITURA DE LOS VALORES
    error_x_values.insert(0,"")
    error_f_values.insert(0,"")
    df = pd.DataFrame({
        'ITERACIONES': iteraciones,
        'x': x_values,
        'y': y_values,
        'f(x,y)': f1_values,
        'g(x,y)': f2_values,
        'Max error (x,y)': error_x_values,
        'Max error (f(x,y),g(x,y))': error_f_values
    })

    df_latex = df.to_latex(index=False, caption="Método de NR",label="NR Table")
    print(df_latex)



if __name__ == "__main__":
    run()
