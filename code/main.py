# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 01:55:24 2022

@author: olivi
"""

import igraph as ig
import random as rd
from DetectCommunitiesScript import DetectCommunities

G_zachary = ig.Graph.Famous("Zachary")
DetectCommunities(G_zachary)

rd.seed(123)
rd_G = ig.Graph.Erdos_Renyi(34, m=78, directed=False, loops=False)
DetectCommunities(rd_G)
