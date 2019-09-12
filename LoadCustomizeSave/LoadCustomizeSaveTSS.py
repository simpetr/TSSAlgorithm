import snap
import random
import copy
import gc
import sys
#####
## Load undirected graph from txt, add attribute on nodes, and turn the .txt into a .graph


#################
####FUNCTIONS####
#####	IsEdge(SrcNId, DstNId) Tests whether an edge from node SrcNId to DstNId exists in the graph.
#####	GetNodes() Returns the number of nodes in the graph.
#####	Nodes() Returns a generator for the nodes in the graph.
#####   GetId() Returns node ID of the current node.
#####	GetOutEdges() Returns a generator for the caller's neighbors.
#####   GetNI(NId) Returns a node iterator referring to the node of ID NId in the graph.
#####	AddFltAttrDatN(NId, Value, Attr) Sets the value of attribute named Attr for the node with node id NId to Value. Value is an integer, a float, or a string, respectively.

name = raw_input("Please enter something: ")
print "You entered", name

Graph = snap.LoadEdgeList(snap.PNEANet, name+".txt" ,0,1,'\t')
print "Loaded graph"
####ADD THRESHOLD ON EVERY NODE####
for n in Graph.Nodes():
	#An example of threhsold value
	#change on need
	degree = n.GetOutDeg()
	threshold = random.randint(1,degree)
	Graph.AddFltAttrDatN(n.GetId(),threshold,"Threshold")

# print Graph.GetNodes()
# print Graph.GetEdges()

####SAVE THE NEW GRAPH IN SNAP-FRIENDLY FORMAT####
FOut = snap.TFOut(name+".graph")
Graph.Save(FOut)
FOut.Flush()
print "End"


