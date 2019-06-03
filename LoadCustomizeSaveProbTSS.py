import snap
import random
import copy
import gc
import sys

def prob_succes(prob):
	return random.random() <= prob
####LOAD UNDIRECTED GRAPH FROM TXT####
name = "CA-CondMat"
Graph = snap.LoadEdgeList(snap.PNEANet, name+".txt" ,0,1,'\t')
print "Loaded graph"

####ADD THRESHOLD ON EVERY NODE####
for n in Graph.Nodes():
	threshold = 2.0
	Graph.AddFltAttrDatN(n.GetId(),threshold,"Threshold")

print "Added threshold"

####ADD PROB ON EVERY EDGES####
for edge in Graph.Edges():
	value = 0.5
	Graph.AddFltAttrDatE(edge, value, "EdgeProb")

print "Added probability on edge"

##########################
#######CHECK PROB#########
##########################

firstNode = snap.TIntV()
secondNode = snap.TIntV()

####ITERATE THROUGH THE GRAPH CHECKING####
####IF NODES CAN APPLY INFLUECE THROUGH THE VARIOUS EDGES####
for n in Graph.Nodes():
	node = n.GetId()
	for nid in n.GetOutEdges():
		edge = Graph.GetEId(node,nid)
		prob = Graph.GetFltAttrDatE(edge,"EdgeProb")
		if not prob_succes(prob):
			Graph.DelEdge(nid,node)
			firstNode.Add(node)
			secondNode.Add(nid)
			
for idx, val in enumerate(firstNode):
	Graph.DelEdge(val,secondNode[idx])


print Graph.GetNodes()
print Graph.GetEdges()

####SAVE THE NEW GRAPH IN SNAP-FRIENDLY FORMAT####
FOut = snap.TFOut(name+".graph")
Graph.Save(FOut)
FOut.Flush()
print "End"


