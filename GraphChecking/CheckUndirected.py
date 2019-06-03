import snap
import random
import copy
import gc
import sys

name = "CA-GrQc"

if not gc.isenabled():
	gc.enable()

threshold = 2.0
Graph = snap.LoadEdgeList(snap.PNEANet, name+".txt" ,0,1,'\t')
print "Loaded graph"

print "Added probability on edge"
#####################################
########START SIMPLE TSS#############
#####################################
print Graph.GetNodes()
for n in Graph.Nodes():
	node = n.GetId()
	for x in n.GetOutEdges():
		if Graph.IsEdge(node,x):
			ixnode =Graph.GetNI(x)
			ixnodeId = ixnode.GetId()
			if not Graph.IsEdge(ixnodeId,node):
					print False
					break
print "Finished"

			
	
		

		
	
		


