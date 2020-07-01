# import sys
# class Graph():
#     def __int__(self,vertices):
#         self.V=vertices
#         self.graph=[[0 for column in range(vertices)] for row in range(vertices)]
#
#     def printMST(self,parent):
#         for i in range(1,self.V):
#             print("{}-{}\t={}".format(parent[i],i,self.graph[i][parent[i]]))
#     def minKey(self,key,mstSet):
#         min=sys.maxint
#         for v in range(s)