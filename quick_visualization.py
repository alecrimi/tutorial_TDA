!pip import nilearn


import pandas as pd
from nilearn import plotting

# Brain atlas centroids
coords = pd.read_csv("coords.txt", header=None)
# Adjacency matrix (brain connectivity)
connectome = pd.read_csv("Conn_mat.txt", header=None)
plotting.view_connectome(connectome.values, coords.values, linewidth=5.0, node_size=5.0)