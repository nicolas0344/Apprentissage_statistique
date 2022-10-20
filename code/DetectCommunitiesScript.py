# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 01:41:17 2022

@author: olivi
"""

import igraph as ig
import matplotlib.pyplot as plt

def DetectCommunities(G):
    # On utilise la centralite d'intermediarite
    # pour la detection de communaute
    communitiesOfGraphe = G.community_edge_betweenness()
    # On convertit l'objet communities en un objet VertexClustering
    # pour la representation graphique
    communitiesOfGraphe = communitiesOfGraphe.as_clustering()
    # On va colorier chaque sommet et arete en fonction de leur appartenance
    # a une communaute
    numberOfCommunities = len(communitiesOfGraphe)
    ColorPalette = ig.RainbowPalette(n=numberOfCommunities)
    for i, c in enumerate(communitiesOfGraphe):
        G.vs[c]["color"] = i
        community_edges = G.es.select(_within=c)
        community_edges["color"] = i
    # On affiche le graphe avec les sommets et les aretes colorees en fonction
    # de leur appartenance a une communaute
    fig, ax = plt.subplots()
    ig.plot(
        communitiesOfGraphe,
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
    
