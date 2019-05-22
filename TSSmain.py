import snap
import random
import copy


# def IsActive(graph,node):
	# if graph.GetIntAttrDatN(node,"IsActive"):
		# return True
	# else:
		# return False

# def SetToFalse(graph,node):
	# graph.AddIntAttrDatN(node,False,"IsActive")
	# return


def influence(graph,node):
	print "Start influencing.."
	for neighbor in node.GetOutEdges():
		###check if the neighbor is still active
		print "Influencing node %d" % (neighbor)
		# if IsActive(graph,node):
			##it's active, reduce threshold##
			## can be improved => if threshold == 0 direclty deactive neighbor##
		thrVal = Graph.GetIntAttrDatN(neighbor,"Threshold")
		if(thrVal<=1):
			graph.AddIntAttrDatN(neighbor,0,"Threshold")
		else:
			thrVal-=1
			graph.AddIntAttrDatN(neighbor,thrVal,"Threshold")
	return



#######################
###change to dataset###
nodes = 10
edges = 16
Graph = snap.TNEANet.New()
#######################

threshold = 2
Graph.AddIntAttrN("Threshold", threshold)
####IsActive#####
####True = active#####
####False = noActive####
#Graph.AddIntAttrN("IsActive",True)

#U = snap.TIntV()
S = snap.TIntV()


##Remove when dataset is used##
###############################
#Create nodes
for i in range(0,nodes):
	Graph.AddNode(i)
	#U.Add(i)

#Create random edges
while edges>0:
	x = int(random.random() *nodes)
	y = int(random.random() *nodes)
	if x!=y and not Graph.IsEdge(x,y):
		Graph.AddEdge(x,y)
		Graph.AddEdge(y,x)
		edges-=1
		
#print
for NI in Graph.Nodes():
	nid = NI.GetId()
	thrVal = Graph.GetIntAttrDatN(nid,"Threshold")
	Oedges = NI.GetOutEdges()
	Iedges = NI.GetInEdges()
	print "node %d, threshold %d" % (nid,thrVal)
	print "node %d, OutDegree %d InDegree %d" % (nid, NI.GetOutDeg(),NI.GetInDeg())
	
	print "My neighbors "
	for nid2 in NI.GetOutEdges():
		edge = Graph.GetEId(nid,nid2)
		print "%d " % (nid2)
		
while not Graph.Empty():
	moveOn = True
	print "First phase"
	for n in Graph.Nodes():
		node = n.GetId()
		print "Node %d" % (node)
		thrVal = Graph.GetIntAttrDatN(node,"Threshold")
		if thrVal == 0:
			influence(Graph,n)
			if Graph.IsNode(node):
				Graph.DelNode(node)
				moveOn = False
				break
	if not moveOn:
		continue
	print "Second phase"
	for n in Graph.Nodes():
		node = n.GetId()
		print "Node %d" % (node)
		thrVal = Graph.GetIntAttrDatN(node,"Threshold")
		if n.GetOutDeg() < thrVal:
			influence(Graph,n)
			if Graph.IsNode(node):
				S.Add(node)
				print "Added %d into the Set" % (node)
				Graph.DelNode(node)
				moveOn = False
				break
	if not moveOn:
		continue
	print "Third phase"
	maxV = -100
	maxN = -1
	for n in Graph.Nodes():
		node = n.GetId()
		print "Node %d" % (node)
		thrVal = Graph.GetIntAttrDatN(node,"Threshold")
		degree = n.GetOutDeg()
		value = (thrVal/(degree * (degree+1.0)))
		print "Node influence value %f" % (value)
		if value > maxV:
			maxV = value
			maxN = node
	print "Node %d influence value %f" % (maxN,maxV)
	Graph.DelNode(maxN)
	
print "Final set: "
for i in S:
	print "Node %d" % (i)
			
			
	
		

		
	
		


