# Networkx para grafos
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

tren = input("Seleccione un TREN: Rojo (r), Verde(g): ")
origen = input("Seleccione un origen: ")
destino = input("Seleccione un destino: ")

# CARGA ARCHIVO DE ESTACIONES
station = pd.read_csv('stations.csv')
color_list = station['color'].tolist()

#print(station.head())

# CARGA DE RUTAS O COMBINACIONES DE LAS ESTACIONES
combinaciones = pd.read_csv('routes.csv')

#print(combinaciones.head())

DG = nx.DiGraph()
for row in station.iterrows():
    DG.add_node(row[1]["name"], color = row[1]["color"])
    
for row in combinaciones.iterrows():
    DG.add_edge(row[1]["origen"], row[1]["destino"])

def heuristica(u,v,d):
    colorA = node_u_wt = DG.nodes[u].get("color")
    colorB = node_u_wt = DG.nodes[v].get("color")

    if tren == "r":
        if colorA == "white" and colorB == "white": ponderado = 1
        if colorA == "white" and colorB == "green": ponderado = 0
        if colorA == "white" and colorB == "red": ponderado = 1
        if colorA == "red" and colorB == "white": ponderado = 1
        if colorA == "red" and colorB == "green": ponderado = 0
        if colorA == "red" and colorB == "red": ponderado = 1
        if colorA == "green" and colorB == "white": ponderado = 1
        if colorA == "green" and colorB == "green": ponderado = 0
        if colorA == "green" and colorB == "red": ponderado = 1

    elif tren == "g":
        if colorA == "white" and colorB == "white": ponderado = 1
        if colorA == "white" and colorB == "green": ponderado = 1
        if colorA == "white" and colorB == "red": ponderado = 0
        if colorA == "red" and colorB == "white": ponderado = 1
        if colorA == "red" and colorB == "green": ponderado = 1
        if colorA == "red" and colorB == "red": ponderado = 0
        if colorA == "green" and colorB == "white": ponderado = 1
        if colorA == "green" and colorB == "green": ponderado = 1
        if colorA == "green" and colorB == "red": ponderado = 0

    return ponderado


rutas = list(nx.all_shortest_paths(DG, source=origen, target=destino, weight = lambda u, v, d: heuristica(u,v,d)))

for i, ruta in enumerate(rutas):
    if tren == "r": print("Ruta #:", i+1,  [d for d in ruta if DG.nodes[d].get("color") != "green"])
    if tren == "g": print("Ruta #:", i+1,  [d for d in ruta if DG.nodes[d].get("color") != "red"])

# GRAFICO
nx.draw_networkx(DG, node_color=color_list, edge_color="indigo", font_size=14, width=2, with_labels=True, node_size=350, font_weight='bold' )
plt.show()