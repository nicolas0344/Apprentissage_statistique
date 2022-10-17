# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 17:34:20 2022

@author: olivi
"""


import igraph as ig
import matplotlib.pyplot as plt

# On charge le celebre graphe du club de karate de Zachary
G_karateClub = ig.Graph.Famous("Zachary")

# On utilise la centralite d'intermediarite
# pour la detection de communaute
communities = G_karateClub.community_edge_betweenness()
# On convertit l'objet communities en un objet VertexClustering
# pour la representation graphique
communities = communities.as_clustering()
# On va colorier chaque sommet et arete en fonction de leur appartenance
# a une communaute
numberOfCommunities = len(communities)
ColorPalette = ig.RainbowPalette(n=numberOfCommunities)
for i, c in enumerate(communities):
    G_karateClub.vs[c]["color"] = i
    community_edges = G_karateClub.es.select(_within=c)
    community_edges["color"] = i
    print((i,c))
# On affiche le graphe avec les sommets et les aretes colorees en fonction
# de leur appartenance a une communaute
fig, ax = plt.subplots()
ig.plot(
    communities,
    palette=ColorPalette,
    edge_width=1,
    target=ax,
    vertex_size=0.3,
)

# On cree la legende qui indiquera les couleurs associees a chaque communautes
G_legend = []
for i in range(numberOfCommunities):
    handle = ax.scatter(
        [], [],
        s=100,
        facecolor=ColorPalette.get(i),
        edgecolor="k",
        label=i+1,
    )
    G_legend.append(handle)

ax.legend(
    handles=G_legend,
    title='communautes:',
    bbox_to_anchor=(0, 1.0),
    bbox_transform=ax.transAxes,
)

# On sauvegarde le trace du graphe au format png
#plt.savefig('G_zachary.png')