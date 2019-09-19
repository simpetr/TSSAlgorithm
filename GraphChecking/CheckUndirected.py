import snap
import random
import copy
import gc
import sys
#################
## Check if a given graph is directed or not

#################
####FUNCTIONS####
#####	IsEdge(SrcNId, DstNId) tests whether an edge from node SrcNId to DstNId exists in the graph.
#####	GetNodes() returns the number of nodes in the graph.
#####	Nodes() returns a generator for the nodes in the graph.
#####   GetId() returns node ID of the current node.
#####	GetOutEdges() returns a generator for the caller's neighbors.
#####   GetNI(NId) returns a node iterator referring to the node of ID NId in the graph.
 
 
name = raw_input("Please enter dataset name: ")
print "You entered", name

if not gc.isenabled():
	gc.enable()

Graph = snap.LoadEdgeList(snap.PNEANet, name+".txt" ,0,1,'\t')
print "Loaded graph from txt file"
print "Nodes number: " + str(Graph.GetNodes())
print "Checking the graph"

directed = False
for n in Graph.Nodes():
	node = n.GetId()
	for x in n.GetOutEdges():
		if Graph.IsEdge(node,x):
			if not Graph.IsEdge(x,node):
					directed = True
					break

if directed:
	print "The graph is directed"
else:
	print "The graph is undirected"

			
	
		

		
	
		


