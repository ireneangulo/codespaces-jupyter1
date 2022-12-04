#Se requiere implementar una red de ferrocarriles compuesta de estaciones de trenes y cambios de agujas (o desvíos). Contemplar las siguientes consideraciones:
#cada vértice del grafo no dirigido tendrá un tipo (estación o desvió) y su nombre, en el caso de los desvíos el nombre es un número –estos estarán numerados de manera consecutiva–;
#cada desvío puede tener múltiples puntos de entrada y salida;
#se deben cargar seis estaciones de trenes y doce cambios de agujas;
#cada cambio de aguja debe tener al menos cuatro salida o vértices adyacentes;
#y cada estación como máximo dos salidas o llegadas y no puede haber dos estaciones co- nectadas directamente
# encontrar el camino más corto desde:
#la estación King's Cross hasta la estación Waterloo,
#la estación Victoria Train Station hasta la estación Liverpool Street Station,
#la estación St. Pancras hasta la estación King's Cross.
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(['King\'s Cross', 'Waterloo', 'Victoria Train Station', 'Liverpool Street Station', 'St. Pancras', 'Euston', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], type='station')
G.add_nodes_from(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], type='desvio')

G.add_edges_from([('King\'s Cross', '1'), ('Waterloo', '1'), ('Waterloo', '2'), ('Victoria Train Station', '2'), ('Liverpool Street Station', '2'), ('Liverpool Street Station', '3'), ('St. Pancras', '3'), ('St. Pancras', '4'), ('Euston', '4'), ('1', '5'), ('1', '6'), ('2', '5'), ('2', '6'), ('2', '7'), ('2', '8'), ('3', '7'), ('3', '8'), ('3', '9'), ('3', '10'), ('4', '9'), ('4', '10'), ('4', '11'), ('4', '12'), ('5', '6'), ('5', '7'), ('6', '7'), ('7', '8'), ('8', '9'), ('9', '10'), ('10', '11'), ('11', '12')])

print("Camino más corto entre King's Cross y Waterloo:")
print(nx.shortest_path(G, source="King\'s Cross", target='Waterloo'))
print("Camino más corto entre Victoria Train Station y Liverpool Street Station:")
print(nx.shortest_path(G, source='Victoria Train Station', target='Liverpool Street Station'))
print("Camino más corto entre St. Pancras y King's Cross:")
print(nx.shortest_path(G, source='St. Pancras', target="King\'s Cross"))

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, nodelist=['King\'s Cross', 'Waterloo', 'Victoria Train Station', 'Liverpool Street Station', 'St. Pancras', 'Euston'], node_color='b', node_size=500, alpha=0.8)










 











