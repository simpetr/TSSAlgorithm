import snap
import random
import copy
import gc
import sys

####LOAD UNDIRECTED GRAPH FROM TXT####
name = "CA-GrQc"
Graph = snap.LoadEdgeList(snap.PNEANet, name+".txt" ,0,1,'\t')
print "Loaded graph"

####ADD THRESHOLD ON EVERY NODE####
for n in Graph.Nodes():
	degree = n.GetOutDeg()
	thr= 2.0
	if (thr<= degree):
		threshold = thr
	else:
		threshold = degree
	Graph.AddFltAttrDatN(n.GetId(),threshold,"Threshold")

print Graph.GetNodes()
print Graph.GetEdges()

####SAVE THE NEW GRAPH IN SNAP-FRIENDLY FORMAT####
FOut = snap.TFOut(name+".graph")
Graph.Save(FOut)
FOut.Flush()
print "End"


