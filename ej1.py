#Desarrollar los algoritmos necesarios para generar un árbol de Huffman a partir de la siguiente tabla –para lo cual deberá calcular primero las frecuencias de cada carácter a partir de la cantidad de apariciones del mismo, para resolver las siguientes actividades:
#la generación del árbol debe hacerse desde los caracteres de menor frecuencia hasta los de mayor, en el caso de que dos caracteres tengan la misma frecuencia, primero se toma el que este primero en el alfabeto, el carácter “espacio” y “coma” se consideraran anteúltimo y último respectivamente en el orden alfabético;
#descomprimir los siguientes mensajes –cuyo árbol ha sido construido de la misma manera que el ejemplo visto anteriormente:
#Mensaje 1:  “10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100”
#Mensaje 2: “0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010”
#finalmente, calcule el espacio de memoria requerido por el mensaje original y el comprimido
import numpy as np
import heapq
import collections


class Nodo:
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der

    def __lt__(self, other):
        return self.valor < other.valor

    def __repr__(self):
        return str(self.valor)


def huffman(codigos):
    heap = [Nodo(frecuencia, caracter) for caracter, frecuencia in codigos.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        izq = heapq.heappop(heap)
        der = heapq.heappop(heap)
        padre = Nodo(izq.valor + der.valor, izq, der)
        heapq.heappush(heap, padre)
    return heap[0]


def codificar(nodo, codigo, codigos):
    if nodo.izq is None and nodo.der is None:
        codigos[nodo] = codigo
    else:
        codificar(nodo.izq, codigo + '0', codigos)
        codificar(nodo.der, codigo + '1', codigos)


def descodificar(nodo, codigo, mensaje):
    if nodo.izq is None and nodo.der is None:
        return nodo, codigo
    else:
        if codigo[0] == '0':
            return descodificar(nodo.izq, codigo[1:], mensaje)
        else:
            return descodificar(nodo.der, codigo[1:], mensaje)


def main():
    mensaje = "hola como estas, como estas"
    frecuencias = collections.Counter(mensaje)
    codigos = {}
    raiz = huffman(frecuencias)
    codificar(raiz, '', codigos)
    print(codigos)
    mensaje_codificado = ''.join([codigos[caracter] for caracter in mensaje])
    print(mensaje_codificado)
    mensaje_descodificado = ''
    nodo = raiz
    for codigo in mensaje_codificado:
        nodo, codigo = descodificar(nodo, codigo, mensaje_descodificado)
        if nodo.izq is None and nodo.der is None:
            mensaje_descodificado += nodo.valor
            nodo = raiz
    print(mensaje_descodificado)


if __name__ == '__main__':
    main()


