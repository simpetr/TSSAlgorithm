import snap
import random
import copy
import gc
import sys

name = "CA-GrQc"

if not gc.isenabled():
	gc.enable()

def printGraphDetails(Graph):
	#print
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


def influence(graph,node):
	#print "Start influencing.."
	for neighbor in node.GetOutEdges():
		###check if the neighbor is still active
		#print "Influencing node %d" % (neighbor)
		# if IsActive(graph,node):
			##it's active, reduce threshold##
			## can be improved => if threshold == 0 direclty deactive neighbor##
		# thrVal = graph.GetIntAttrDatN(neighbor,"Threshold")
		thrVal = T[neighbor]
		if(thrVal<=1):
			# graph.AddIntAttrDatN(neighbor,0,"Threshold")
			T[neighbor] = 0
		else:
			thrVal-=1
			# graph.AddIntAttrDatN(neighbor,thrVal,"Threshold")
			T[neighbor] = thrVal
	return

FIn = snap.TFIn(name+".graph")
Graph = snap.TNEANet.Load(FIn)
print "Loaded graph"
#####################################
########START SIMPLE TSS#############
#####################################

S = snap.TIntV()
T = snap.TIntV()
nodesList = snap.TIntV()
j = 0
sum = 0
for node in Graph.Nodes():
	T.Add(Graph.GetFltAttrDatN(node,"Threshold"))
print "Finished"
print len(T)
gc.collect()

while not Graph.Empty():
	j+=1
	if (j%1000 ==0):
		nodesNumber = Graph.GetNodes()
		print ". elaborated nodes %d left nodes %d target size %d" %(j,nodesNumber,S.Len())
	moveOn = True
	n = Graph.BegNI()
	while n < Graph.EndNI():
		node = n.GetId()
		# print "Node %d" % (node)
		thrVal = T[node]
		if thrVal == 0.0:
			influence(Graph,n)
			Graph.DelNode(node)
			moveOn = False
			break
		n.Next()
	if not moveOn:
		continue
	n = Graph.BegNI()
	while n < Graph.EndNI():
		node = n.GetId()
		thrVal = T[node]
		if n.GetOutDeg() < thrVal:
			influence(Graph,n)
			S.Add(node)
			Graph.DelNode(node)
			moveOn = False
			break
		n.Next()
	if not moveOn:
		continue
	# #print "Third phase"
	maxV = -100
	maxN = -1

	n = Graph.BegNI()
	while n < Graph.EndNI():
		node = n.GetId()
		thrVal = T[node]
		degree = n.GetOutDeg()
		if degree!=0:
			value = (thrVal/(degree * (degree+1.0)))
			if value > maxV:
				maxV = value
				maxN = node
		n.Next()
	# #print "Node %d influence value %f" % (maxN,maxV)
	Graph.DelNode(maxN)
	
print "Final set: "
for i in S:
	print "Node %d" % (i)
			
			
	
		

		
	
		


