import requests
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def readEdgeList(filename):
	dataFrame = pd.read_csv(filename) #method of pandas finds the filename
	if len(dataFrame.columns) > 2:
		print "Error"
		dataFrame = pd.read_csv(filename, usecols = [0,1])
		data = pd.DataFrame(dataFrame)
	else:
		data=pd.DataFrame(dataFrame)
	#pd.read_csv takes a string (URL) and returns a DataFrame
	return data #dataframe

filename = 'edgeList.csv' #string
# print readEdgeList(filename)

#turning the csv file into a DataFrame
#  artistID           next_artistID
# 0   2mAFHYBasVVtMekMUkRO9g  6M0icmVnLz7AcdSfpQ1L78

def degree(edgeList, in_or_out):
	#series.value_counts()  takes a parameter and returns object of counts of values
	# DataFrame + string --> in degree or out degree for all nodes on list
	dataFrame = readEdgeList(edgeList)
	if in_or_out == "in":
		degree = dataFrame['artistID'].value_counts()
	if in_or_out == "out":
		degree = dataFrame['next_artistID'].value_counts()
	return degree

#print degree('edgeList.csv', 'in')

def combineEdgelists(edgeList1, edgeList2):
	#combining dataframes
	# dataframe1 = edgeList1
	# dataframe2 = edgeList2
	concatenated = pd.concat([edgeList1], [edgeList2])
	return concatenated.drop_duplicates()
edgeList1 = readEdgeList('edgeList.csv')
edgeList2 = readEdgeList('edgeList.csv')
#print combineEdgelists(edgeList1, edgeList2)

def pandasToNetworkX(edgeList):
	g = nx.DiGraph() #empty graph 
	for artist, related_artist in edgeList.to_records(index=False): #adds an edge
		g.add_edge(artist, related_artist)
	#print g.number_of_edges()
	return(g)

d=readEdgeList('edgeList.csv')
# g = pandasToNetworkX(d)
# print g.nodes()

def randomCentralNode(inputDiGraph):
	#takes graph --> single node from that network
	nodes_dict = nx.eigenvector_centrality(inputDiGraph) #network method assigns centrality value to each node
	#keys are artist ids, value is centrality(weights)
	total = sum(nodes_dict.values()) #total is 0
	#nx.eigenvector_centrality() takes graph as parameter and returns nodes in a dict.
	for variable in nodes_dict:
		if total == 0:
			nodes_dict[variable]=1.0/len(inputDiGraph)
		else:
			nodes_dict[variable]=nodes_dict[variable]/float(total)

	random_node = np.random.choice(nodes_dict.keys(), p = nodes_dict.values()) #need to sum to 1 because of probability rules
	return random_node

edgeList = readEdgeList('edgeList.csv')
print randomCentralNode(pandasToNetworkX(edgeList))






