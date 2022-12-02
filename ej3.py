#desarrollar un algoritmo numerico iterativo que permita calcular el metodo de la biseccion f(x)
import numpy as np
def f(x):
    return x**3 + x +16
def biseccion(a,b):     
    if f(a)*f(b)>0:
        print("no hay raiz en el intervalo")
    else:
        while abs(b-a)>0.0001:
            c=(a+b)/2
            if f(a)*f(c)<0:
                b=c
            else:
                a=c
        print("la raiz es",c)
a= float(input("ingrese el valor de a "))
b= float(input("ingrese el valor de b "))
biseccion(a,b)

#desarrollar un algoritmo numerico iterativo que permita calcular el metodo de la secante f(x)
import numpy as np      
def f(x):
    return  x**3 + x +16
def secante(x0,x1):
    if f(x0)*f(x1)>0:
        print("no hay raiz en el intervalo")
    else:
        while abs(x1-x0)>0.0001:
            x2=x1-f(x1)*(x1-x0)/(f(x1)-f(x0))
            x0=x1
            x1=x2
        print("la raiz es",x2)
x0= float(input("ingrese el valor de x0 "))
x1= float(input("ingrese el valor de x1 "))
secante(x0,x1)

#desarrollar un algoritmo numerico iterativo que permita calcular el metodo de newton raphson f(x)
import numpy as np
def f(x):
    return  x**3 + x + 16
def df(x):
    return 2*x
def newton_raphson(x0):
    if f(x0)*df(x0)>0:
        print("no hay raiz en el intervalo")
    else:
        while abs(f(x0))>0.0001:
            x1=x0-f(x0)/df(x0)
            x0=x1
        print("la raiz es",x1)
x0= float(input("ingrese el valor de x0 "))
newton_raphson(x0)



 
