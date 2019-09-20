import snap
import random
import copy
import gc
import sys
#####
## Load an undirected graph from a .txt file, add a threshold attribute to each node, and turn the customized graph into a .graph file.


#################
####FUNCTIONS####
#####	IsEdge(SrcNId, DstNId) tests whether an edge from node SrcNId to DstNId exists in the graph.
#####	GetNodes() returns the number of nodes in the graph.
#####	Nodes() returns a generator for the nodes in the graph.
#####   GetId() returns node ID of the current node.
#####	GetOutEdges() returns a generator for the caller's neighbors.
#####   GetNI(NId) returns a node iterator referring to the node of ID NId in the graph.
#####	AddFltAttrDatN(NId, Value, Attr) sets the value of the attribute named Attr for the node with node id NId to Value. Value is an integer, a float, or a string, respectively.

name = raw_input("Please enter the dataset name: ")
print "You entered", name

Graph = snap.LoadEdgeList(snap.PNEANet, name+".txt" ,0,1,'\t')
print "Loaded graph"

####ADD THRESHOLD ON EACH NODE####
for n in Graph.Nodes():
	#An example of threhsold value
	#change on need
	degree = n.GetOutDeg()
	threshold = random.randint(1,degree)
	#
	Graph.AddFltAttrDatN(n.GetId(),threshold,"Threshold")

# print Graph.GetNodes()
# print Graph.GetEdges()

####SAVE THE NEW GRAPH IN A SNAP-FRIENDLY FORMAT####
FOut = snap.TFOut(name+".graph")
Graph.Save(FOut)
FOut.Flush()
print "End"


