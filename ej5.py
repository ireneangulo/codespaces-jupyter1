import heapq
import collections 

def huffman(frecuencias):
    heap = [[frecuencia, [caracter, ""]] for caracter, frecuencia in frecuencias.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        frecuencia1 = heapq.heappop(heap)
        frecuencia2 = heapq.heappop(heap)
        for par in frecuencia1[1:]:
            par[1] = '0' + par[1]
        for par in frecuencia2[1:]:
            par[1] = '1' + par[1]
        heapq.heappush(heap, [frecuencia1[0] + frecuencia2[0]] + frecuencia1[1:] + frecuencia2[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


def main():
    texto = "Este es un texto de prueba para el algoritmo de Huffman"
    frecuencias = collections.Counter(texto)
    huff = huffman(frecuencias)
    print("Caracteres y su frecuencia:")
    print(frecuencias)
    print("Caracteres y su codificación:")
    for p in huff:
        print(p[0], ":", p[1])

if __name__ == "__main__":
    main()




 