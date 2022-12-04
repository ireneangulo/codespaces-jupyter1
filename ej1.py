#Desarrollar los algoritmos necesarios para generar un árbol de Huffman a partir de la siguiente tabla –para lo cual deberá calcular primero las frecuencias de cada carácter a partir de la cantidad de apariciones del mismo, para resolver las siguientes actividades:
#la generación del árbol debe hacerse desde los caracteres de menor frecuencia hasta los de mayor, en el caso de que dos caracteres tengan la misma frecuencia, primero se toma el que este primero en el alfabeto, el carácter “espacio” y “coma” se consideraran anteúltimo y último respectivamente en el orden alfabético;
#descomprimir los siguientes mensajes –cuyo árbol ha sido construido de la misma manera que el ejemplo visto anteriormente:
#Mensaje 1:  “10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100”
#Mensaje 2: “0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010”
#finalmente, calcule el espacio de memoria requerido por el mensaje original y el comprimido
import numpy as np
import heapq
import collections
def huffman( ) :
    #frecuencia de cada caracter
    freq = {'a':11, 'b':2, 'c':4, 'd':3, 'e':14, 'g':3, 'i':6, 'l':6, 'm':3, 'n':6, 'o':7, 'p':4, 'q':1, 'r':10, 's':4, 't':3, 'u':4, 'v':2, ' ':17, ',':2}
    #ordenar de menor a mayor
    sorted_freq = sorted(freq.items(), key=lambda x: x[1])
    #construir arbol
    nodes = sorted_freq
    while len(nodes) > 1:
        key1, c1 = nodes[0]
        key2, c2 = nodes[1]
        nodes = nodes[2:]
        node = (key1, key2)
        heapq.heappush(nodes, (node, c1 + c2))
    #asignar codigo
    huff = {}
    def assign_code(node, pat=''):
        if type(node) is str:
            huff[node] = pat
        else:
            l, r = node
            assign_code(l, pat + "0")
            assign_code(r, pat + "1")
    assign_code(nodes[0][0])
    #imprimir
    print('Caracteres y sus codigos:')
    for p in sorted(huff):
        print(p + ' : ' + huff[p])
    
    #mensaje 1
    mensaje1 = "10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100"
    #mensaje 2
    mensaje2 = "0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010"
    #descomprimir
    def decode( mensaje, huff):
        ans = ''
        node = nodes[0][0]
        for bit in mensaje:
            if bit == '0':
                node = node[0]
            else:
                node = node[1]
            if type(node) is str:
                ans += node
                node = nodes[0][0]
        return ans
    print('Mensaje 1: ' + decode(mensaje1, huff))
    print('Mensaje 2: ' + decode(mensaje2, huff))
    #calcular espacio de memoria
    print('Espacio de memoria original: ' + str(8*len(mensaje1)))
    print('Espacio de memoria comprimido: ' + str(len(mensaje1)))
huffman()



