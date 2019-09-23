import snap
import random
import copy
import gc
import sys
import array
#################
## Simple TSS algorithm

#################
####METHODS####
#####	IsEdge(SrcNId, DstNId) tests whether an edge from node SrcNId to DstNId exists in the graph.
#####	GetNodes() returns the number of nodes in the graph.
#####	Nodes() returns a generator for the nodes in the graph.
#####   GetId() returns node ID of the current node.
#####	GetOutEdges() returns a generator for the caller's neighbors.
#####   GetNI(NId) returns a node iterator referring to the node of ID NId in the graph.



name = raw_input("Please enter something: ")
print "You entered", name

if not gc.isenabled():
	gc.enable()
	
####PRINT FUNCTION
def printGraphDetails(Graph):
	for NI in Graph.Nodes():
		node = NI.GetId()
		thrVal = Graph.GetIntAttrDatN(node,"Threshold")
		print "node %d, threshold %d" % (node,thrVal)
		
		print "My neighbors are"
		for nid in NI.GetOutEdges():
			edge = Graph.GetEId(node,nid)
			value = Graph.GetFltAttrDatE(edge,"EdgeProb")
			print "edge between %d and %d" % (node,nid)
			print "%d value on the edge %f" % (nid,value)
####END



####INFLUENCE FUNCTION####
def influence(graph,node):
	##Check all nodes' neighbors
	for neighbor in node.GetOutEdges():
		thrVal = T[neighbor]
		if(thrVal<=1):
			T[neighbor] = 0
		else:
			thrVal-=1
			T[neighbor] = thrVal
	return
#END

FIn = snap.TFIn(name +".graph")
Graph = snap.TNEANet.Load(FIn)
print "Loaded graph"

#####################################
########START SIMPLE TSS#############
#####################################

S = snap.TIntV()
T = snap.TIntFltH()
nodesList = snap.TIntV()
# j = 0

for node in Graph.Nodes():
	id = node.GetId()
	T[id] =Graph.GetFltAttrDatN(node,"Threshold")
	
print "Finished"

gc.collect()


while not Graph.Empty():
	Graph.GetNIdV(nodesList)
	#Enable if you want a feedback on the execution
	# j+=1
	# if (j%1000 ==0):
		# print "."
	##FIRST PHASE	
	moveOn = True
	for i in nodesList:
		thrVal = T[i]
		if thrVal == 0.0:
			influence(Graph,Graph.GetNI(i))
			Graph.DelNode(i)
			moveOn = False
			break
	if not moveOn:
		continue
	##SECOND PHASE
	for i in nodesList:
		thrVal = T[i]
		if Graph.GetNI(i).GetOutDeg() < thrVal:
			influence(Graph,Graph.GetNI(i))
			S.Add(i)
			Graph.DelNode(i)
			moveOn = False
			break
	if not moveOn:
		continue
	##THIRD PHASE
	maxV = -1000
	maxN = -1
	for i in nodesList:
		thrVal = T[i]
		degree = Graph.GetNI(i).GetOutDeg()
		if degree!=0:
			value = (thrVal/(degree * (degree+1.0)))
			if value > maxV:
				maxV = value
				maxN = i
	Graph.DelNode(maxN)
	
# print "Final set: "
# for i in S:
	# print "Node %d" % (i)
	
f = open("result"+name+".txt", 'a')
f.write(name+"\n")
f.write("Target set size"+str(S.Len())+"\n")
f.close()
			
			
	
		

		
	
		


