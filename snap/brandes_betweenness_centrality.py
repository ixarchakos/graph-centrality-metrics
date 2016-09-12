from collections import deque
import snap

fw = open('results.txt', 'w')

# load the edge list using snap library
G1 = snap.LoadEdgeList(snap.PUNGraph, "edges.txt", 0, 1)
V = snap.TIntV()
for NI in G1.Nodes():
    V.Add(NI.GetId())

A = dict((w, []) for w in V)
for NI in G1.Nodes():
    for Id in NI.GetOutEdges():
        A[NI.GetId()].append(Id)
C = dict((v, 0) for v in V)

for s in V:
    # stack - initially empty
    S = []
    # list of predecessors on shortest paths from source
    P = dict((w, []) for w in V)
    # number of shortest paths from source to v which belongs in V
    g = dict((t, 0) for t in V)
    g[s] = 1
    # distance from source
    d = dict((t, -1) for t in V)
    d[s] = 0
    # queue - initially empty
    Q = deque([])
    Q.append(s)
    while Q:
        v = Q.popleft()
        S.append(v)
        for w in A[v]:
            if d[w] < 0:
                Q.append(w)
                d[w] = d[v] + 1
            if d[w] == d[v] + 1:
                g[w] += g[v]
                P[w].append(v)
    # dependency of source on v which belongs in V
    e = dict((v, 0) for v in V)
    while S:
        w = S.pop()
        for v in P[w]:
            e[v] += (g[v]/g[w]) * (1 + e[w])
            if w != s:
                C[w] += e[w]
    # write the results into a txt file
    fw.write("Node:{0}, Value: {1} \n".format(s, C[s]))
    fw.flush()
fw.close()

