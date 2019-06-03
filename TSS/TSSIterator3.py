import snap
import random
import copy
import gc
import sys
import array

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

####INFLUENCE FUNCTION####
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

FIn = snap.TFIn(name +".graph")
Graph = snap.TNEANet.Load(FIn)
print "Loaded graph"
#####################################
########START SIMPLE TSS#############
#####################################

S = snap.TIntV()
T = snap.TIntFltH()
nodesList = snap.TIntV()
j = 0
sum = 0
for node in Graph.Nodes():
	id = node.GetId()
	T[id] =Graph.GetFltAttrDatN(node,"Threshold")
	#T.append(Graph.GetFltAttrDatN(node,"Threshold"))
	#T.Add(Graph.GetFltAttrDatN(node,"Threshold"))
	
print "Finished"
print len(T)
gc.collect()
nodesList = snap.TIntV()
while not Graph.Empty():
	Graph.GetNIdV(nodesList)
	length = len(nodesList)
	j+=1
	if (j%1000 ==0):
		print "."
	moveOn = True
	for i in nodesList:
		# print "Node %d" % (node)
		thrVal = T[i]
		if thrVal == 0.0:
			influence(Graph,Graph.GetNI(i))
			Graph.DelNode(i)
			moveOn = False
			break
	if not moveOn:
		continue
	
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
	# #print "Third phase"
	maxV = -100
	maxN = -1
	for i in nodesList:
		thrVal = T[i]
		degree = Graph.GetNI(i).GetOutDeg()
		if degree!=0:
			value = (thrVal/(degree * (degree+1.0)))
			if value > maxV:
				maxV = value
				maxN = i
	# #print "Node %d influence value %f" % (maxN,maxV)
	Graph.DelNode(maxN)
	
# print "Final set: "
# for i in S:
	# print "Node %d" % (i)
	
f = open('result.txt', 'a')
f.write(name+"\n")
# f.write("nodes size"+str(Graph.GetNodes())+"\n")
# f.write("edges size"+str(Graph.GetEdges())+"\n")
f.write("Target set size"+str(S.Len())+"\n")
for i in S:
	f.write(str(i))
	f.write("\n")
f.close()
			
			
	
		

		
	
		


