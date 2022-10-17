# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 20:49:27 2022

@author: olivi
"""

import random as rd
import matplotlib.pyplot as plt
import igraph as ig

rd.seed(123)

myGraphe = ig.Graph.Erdos_Renyi(34, m=78, directed=False, loops=False)

# On utilise la centralite d'intermediarite
# pour la detection de communaute
communitiesOfmyGraphe = myGraphe.community_edge_betweenness()
# On convertit l'objet communities en un objet VertexClustering
# pour la representation graphique
communitiesOfmyGraphe = communitiesOfmyGraphe.as_clustering()
# On va colorier chaque sommet et arete en fonction de leur appartenance
# a une communaute
numberOfCommunities = len(communitiesOfmyGraphe)
ColorPalette = ig.RainbowPalette(n=numberOfCommunities)
for i, c in enumerate(communitiesOfmyGraphe):
    myGraphe.vs[c]["color"] = i
    community_edges = myGraphe.es.select(_within=c)
    community_edges["color"] = i
    print((i,c))
# On affiche le graphe avec les sommets et les aretes colorees en fonction
# de leur appartenance a une communaute
fig, ax = plt.subplots()
ig.plot(
    communitiesOfmyGraphe,
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

#plt.savefig('random_network2.png')