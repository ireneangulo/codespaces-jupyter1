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

import networkx as nx
import matplotlib.pyplot as plt
# Se crea un grafo no dirigido
G = nx.Graph()
# Se crean los nodos
G.add_nodes_from(['King\'s Cross', 'Waterloo', 'Victoria Train Station', 'Liverpool Street Station', 'St. Pancras', 'St. Pancras'])
# Se crean las aristas
G.add_edges_from([('King\'s Cross', 'Waterloo'), ('King\'s Cross', 'Victoria Train Station'), ('King\'s Cross', 'Liverpool Street Station'), ('King\'s Cross', 'St. Pancras'), ('Waterloo', 'Victoria Train Station'), ('Waterloo', 'Liverpool Street Station'), ('Waterloo', 'St. Pancras'), ('Victoria Train Station', 'Liverpool Street Station'), ('Victoria Train Station', 'St. Pancras'), ('Liverpool Street Station', 'St. Pancras')])
# Se dibuja el grafo
nx.draw(G, with_labels=True)
plt.show()
# Se obtiene el camino más corto desde la estación King's Cross hasta la estación Waterloo
nx.shortest_path(G, source='King\'s Cross', target='Waterloo')
# Se obtiene el camino más corto desde la estación Victoria Train Station hasta la estación Liverpool Street Station
nx.shortest_path(G, source='Victoria Train Station', target='Liverpool Street Station')
# Se obtiene el camino más corto desde la estación St. Pancras hasta la estación King's Cross
nx.shortest_path(G, source='St. Pancras', target='King\'s Cross')
# Se obtiene la distancia más corta desde la estación King's Cross hasta la estación Waterloo
nx.shortest_path_length(G, source='King\'s Cross', target='Waterloo')
# Se obtiene la distancia más corta desde la estación Victoria Train Station hasta la estación Liverpool Street Station
nx.shortest_path_length(G, source='Victoria Train Station', target='Liverpool Street Station')
# Se obtiene la distancia más corta desde la estación St. Pancras hasta la estación King's Cross
nx.shortest_path_length(G, source='St. Pancras', target='King\'s Cross')



