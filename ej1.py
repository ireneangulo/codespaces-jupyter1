#Desarrollar los algoritmos necesarios para generar un árbol de Huffman a partir de la siguiente tabla –para lo cual deberá calcular primero las frecuencias de cada carácter a partir de la cantidad de apariciones del mismo, para resolver las siguientes actividades:
#la generación del árbol debe hacerse desde los caracteres de menor frecuencia hasta los de mayor, en el caso de que dos caracteres tengan la misma frecuencia, primero se toma el que este primero en el alfabeto, el carácter “espacio” y “coma” se consideraran anteúltimo y último respectivamente en el orden alfabético;
#descomprimir los siguientes mensajes –cuyo árbol ha sido construido de la misma manera que el ejemplo visto anteriormente:
#Mensaje 1:  “10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100”
#Mensaje 2: “0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010”
#finalmente, calcule el espacio de memoria requerido por el mensaje original y el comprimido
import sys
import heapq
import collections
import numpy as np
def huffman( ):
    #frecuencia de cada caracter
    freq = {'a':11, 'b':2, 'c':4, 'd':3, 'e':14, 'g':3, 'i':6, 'l':6, 'm':3, 'n':6, 'o':7, 'p':4, 'q':1, 'r':10, 's':4, 't':3, 'u':4, 'v':2, ' ':17, ',':2}
    #ordenar de menor a mayor
    sorted_freq = sorted(freq.items(), key=lambda x: x[1])

    #crear arbol
    heap = [[wt, [sym, ""]] for sym, wt in sorted_freq]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    #imprimir arbol
    print("Arbol de Huffman:")
    for p in sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p)):
        print("%s\t%s" % (p[0], p[1]))
    #descodificar mensaje
    mensaje1 = "10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100"
    mensaje2 = "0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010"
    print("Mensaje 1: ", mensaje1)
    print("Mensaje 2: ", mensaje2)
    print("Mensaje 1 descodificado: ", descodificar(mensaje1))
    print("Mensaje 2 descodificado: ", descodificar(mensaje2))
    #calcular espacio de memoria
    print("Espacio de memoria original: ", sys.getsizeof("La vida es una sucesion de momentos, algunos son felices, otros no tanto, pero todos son unicos."))
    print("Espacio de memoria comprimido: ", sys.getsizeof(mensaje1+mensaje2))
def descodificar(mensaje):
    #frecuencia de cada caracter
    freq = {'a':11, 'b':2, 'c':4, 'd':3, 'e':14, 'g':3, 'i':6, 'l':6, 'm':3, 'n':6, 'o':7, 'p':4, 'q':1, 'r':10, 's':4, 't':3, 'u':4, 'v':2, ' ':17, ',':2}
    #ordenar de menor a mayor
    sorted_freq = sorted(freq.items(), key=lambda x: x[1])
    #crear arbol
    heap = [[wt, [sym, ""]] for sym, wt in sorted_freq]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    #descodificar mensaje
    code = dict(heapq.heappop(heap)[1:])
    decoded = ""
    temp = ""
    for bit in mensaje:
        temp += bit
        for dec in code:
            if (temp == code[dec]):
                decoded += dec
                temp = ""
    return decoded 
   
huffman()































