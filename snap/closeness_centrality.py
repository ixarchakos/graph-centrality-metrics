import snap

fw = open('results.txt', 'w')

# load the edge list using snap library
Graph = snap.LoadEdgeList(snap.PUNGraph, "data/edges.txt", 0, 1)

for NI in Graph.Nodes():
    # calculate the closeness centrality value
    closeness_value = snap.GetClosenessCentr(Graph, NI.GetId())
    # write the results into a txt file
    fw.write("Node:{0}, Value: {1} \n".format(NI.GetId(), closeness_value))
    fw.flush()
fw.close()
