import networkx as nx

MG = nx.MultiGraph()
#MG.add_weighted_edges_from([(1, 2, 0.5), (1, 2, 0.75), (2, 3, 0.5)])

MG.add_edge(1, 2, key='lambda_0', weight=4)
MG.add_edge(1, 2, key='lambda_1', weight=9)
MG.add_edge(1, 2, key='lambda_2', weight=7)

MG.add_edge(2, 3, key='lambda_0', weight=4)
MG.add_edge(2, 3, key='lambda_1', weight=3)
MG.add_edge(2, 3, key='lambda_2', weight=4)


print(nx.dijkstra_path(MG, 1, 3))

print(nx.dijkstra_path_length(MG, 1, 3))

MG.remove_edge(1, 2, key='lambda_0')

print(nx.dijkstra_path(MG, 1, 3))

print(nx.dijkstra_path_length(MG, 1, 3))
