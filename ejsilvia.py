def f(x):
    return x**3 + x + 16

def biseccion(a,b):
    if f(a)*f(b) >= 0:
        print("No hay raiz en el intervalo")
        return
    c = a
    while (b-a) >= 0.01:
        c = (a+b)/2
        if f(c) == 0.0:
            break
        if f(c)*f(a) < 0:
            b = c
        else:
            a = c
    print("La raiz es: ",c)

a = -200
b = 300
biseccion(a,b)

#Desarrollar un algoritmo numérico iterativo que permita calcular el método de la secante de una función f(x).
def f(x):
    return x**3 + x + 16

def secante(x0,x1):
    for i in range(1,100):
        x2 =  x1 - (f(x1)*(x1-x0))/(f(x1)-f(x0))
        x0 = x1
        x1 = x2
    print("La raiz es: ",x2)

x0 = float(input("Ingrese el valor inicial: "))
x1 = float(input("Ingrese el valor inicial: "))
secante(x0,x1)

#Desarrollar un algoritmo numérico iterativo que permita calcular el método de Newton-Raphson de una función f(x).

def df(x):
    return x**3 + x + 16

def newton_raphson(x):
    for i in range(0,100):
        x = x - f(x)/df(x)
    print("La raiz es: ",x)

x = 0
newton_raphson(x)