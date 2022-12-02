#Se requiere implementar una red de ferrocarriles compuesta de estaciones de trenes y cambios de agujas (o desvíos). Contemplar las siguientes consideraciones:
#cada vértice del grafo no dirigido tendrá un tipo (estación o desvió) y su nombre, en el caso de los desvíos el nombre es un número –estos estarán numerados de manera consecutiva–;
#cada desvío puede tener múltiples puntos de entrada y salida;
#se deben cargar seis estaciones de trenes y doce cambios de agujas;
#cada cambio de aguja debe tener al menos cuatro salida o vértices adyacentes;
#y cada estación como máximo dos salidas o llegadas y no puede haber dos estaciones co- nectadas directamente
# encontrar el camino más corto desde:
#la estación King's Cross hasta la estación Waterloo,
#la estación Victoria Train Station hasta la estación Liverpool Street Station,
#la estación St. Pancras hasta la estación King's Cross;
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
#creamos el grafo
G=nx.Graph()
#agregamos los vertices
G.add_node("King's Cross",tipo="estacion")
G.add_node("Waterloo",tipo="estacion")
G.add_node("Victoria Train Station",tipo="estacion")
G.add_node("Liverpool Street Station",tipo="estacion")
G.add_node("St. Pancras",tipo="estacion")
G.add_node("1",tipo="desvio")
G.add_node("2",tipo="desvio")
G.add_node("3",tipo="desvio")
G.add_node("4",tipo="desvio")
G.add_node("5",tipo="desvio")
G.add_node("6",tipo="desvio")
#agregamos las aristas
G.add_edge("King's Cross","Waterloo",peso=1)
G.add_edge("King's Cross","Victoria Train Station",peso=1)
G.add_edge("King's Cross","St. Pancras",peso=1)
G.add_edge("Waterloo","1",peso=1)
G.add_edge("Victoria Train Station","2",peso=1)
G.add_edge("Liverpool Street Station","3",peso=1)
G.add_edge("St. Pancras","4",peso=1)
G.add_edge("1","5",peso=1)
G.add_edge("2","5",peso=1)
G.add_edge("3","5",peso=1)
G.add_edge("4","5",peso=1)
G.add_edge("5","6",peso=1)
G.add_edge("6","Liverpool Street Station",peso=1)
#dibujamos el grafo
nx.draw(G,with_labels=True)
plt.show()
#camino mas corto desde King's Cross a Waterloo
print("Camino mas corto desde King's Cross a Waterloo")
print(nx.shortest_path(G,source="King's Cross",target="Waterloo"))
#camino mas corto desde Victoria Train Station a Liverpool Street Station
print("Camino mas corto desde Victoria Train Station a Liverpool Street Station")
print(nx.shortest_path(G,source="Victoria Train Station",target="Liverpool Street Station"))
#camino mas corto desde St. Pancras a King's Cross
print("Camino mas corto desde St. Pancras a King's Cross")
print(nx.shortest_path(G,source="St. Pancras",target="King's Cross"))
