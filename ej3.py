#desarrollar un algoritmo numerico iterativo que permita calcular el metodo de la biseccion f(x)
import numpy as np
def f(x):
    return x**2-2
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


