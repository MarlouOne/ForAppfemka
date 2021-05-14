# -*- coding: utf-8 -*-
"""
Created on Thu May  6 17:00:33 2021

@author: Marlou
"""
class node:
    intIndex : int
    listConnection = []
    listRoadlen    = []
    
    def __init__(self,listConnection,listRoadlen,intIndex):
        self.intIndex       = intIndex
        self.listConnection = listConnection
        self.listRoadlen    = listRoadlen
        
    def makeGraph(listConnection, listRoadlen):
        listGraph = []
        for i in range(len(listConnection)):
            listGraph.append(node(listConnection[i],listRoadlen[i],i+1))
        return listGraph
    
    def printNode(self):
        print('Node number', self.intIndex, 'Node connections', self.listConnection, 'Connections lenght', self.listRoadlen)
    
    def printGraph(listGraph):
        for i in range(len(listGraph)):
            print(listGraph[i].intIndex, ' ', listGraph[i].listConnection, ' ', listGraph[i].listRoadlen)
            
class pointer:
    StaticListGraph    = []
    listUsedNode       = []
    listAllWays        = []
    listCorrectWays    = []
    bFlagEnd = False
    
    def setStaticVar(listGraph):
        pointer.StaticListGraph = listGraph
        pointer.listCorrectWays = [] 
        pointer.listAllWays     = []
        pointer.listUsedNode    = []

    def printCorrectWays(self,StaticIntFinalNode):
        for i in range(len(self.listAllWays)):
            if self.listAllWays[i][-1] == StaticIntFinalNode: print(self.listAllWays[i])
        
    def stepBack(self,StaticIntFinalNode):
        if self.bFlagEnd == False:            
            try:
                a = self.listUsedNode[-2]
                self.listUsedNode = self.listUsedNode[:-2]
                self.findAllWays(a,StaticIntFinalNode)
            except IndexError:
                self.bFlagEnd = True
        
    def findAllWays(self,intNode,StaticIntFinalNode):  
        self.listUsedNode.append(intNode)
        
        if intNode == StaticIntFinalNode:
            self.listCorrectWays.append(self.listUsedNode)
            self.listAllWays.append(self.listUsedNode)
            self.stepBack(StaticIntFinalNode)
            
        for i in range(len(pointer.StaticListGraph[intNode-1].listConnection)):
            intNextNode = pointer.StaticListGraph[intNode-1].listConnection[i]
            if self.isItUsedWay(intNextNode) and self.isItUsedNode(intNextNode) :              
                self.findAllWays(intNextNode, StaticIntFinalNode)
             
        self.listAllWays.append(self.listUsedNode)
        self.stepBack(StaticIntFinalNode)
        return self.listCorrectWays[:-1]
            
    def isItUsedNode(self,intNode):
        if intNode not in self.listUsedNode:
             return True
        return False   
    
    def isItUsedWay(self,intNode):
        listWay = self.listUsedNode.copy()
        listWay.append(intNode)
        if listWay not in self.listAllWays:
            return True
        return False
    
def main():
    listConnection = [[2,8,9],[1,4],[4,6],[2,3,8],[6,7,8],[3,5,7],[5,6,9],[1,4,5],[1,7]]
    listRoadlen    = [[10,8,31],[10,7],[27,10],[7,27,9],[17,15,15],[10,17,21],[15,21,12],[8,9,15],[31,12]]
    listGraph = node.makeGraph(listConnection,listRoadlen)
    node.printGraph(listGraph)
    
    intStartNode, intFinalNode = 6, 2
    pointer.setStaticVar(listGraph)
    pObj = pointer.findAllWays(pointer(),intStartNode,intFinalNode)
    print(f' Final ways {pObj} \n Count of ways {len(pObj)}')
    
    intStartNode, intFinalNode = 3, 6
    pointer.setStaticVar(listGraph)
    pObj = pointer.findAllWays(pointer(),intStartNode,intFinalNode)
    print(f' Final ways {pObj} \n Count of ways {len(pObj)}')
    
    
main()



# def __init__(self,intNode):
#         intIndex = intNode
#         boolWrongWayFlag = False
#         while intIndex != self.StaticIntFinalNode:
#             self.listUsedNode.append(intIndex)
#             for i in range(len(pointer.StaticListGraph[intIndex-1].listConnection)):
#                 if self.isItUsedNode(pointer.StaticListGraph[intIndex-1].listConnection[i]) == False:   
#                     # print(self.listUsedNode)
#                     pointer(pointer.StaticListGraph[intIndex-1].listConnection[i])
#                 elif len(self.listUsedNode) == len(pointer.StaticListGraph):
#                     boolWrongWayFlag = True
#                     break
#         # self.listUsedNode.append(intIndex)
#         if boolWrongWayFlag == True:
#             print('Way',self.listUsedNode,'is bloked')
#         else:
#             print('Final way',self.listUsedNode)
    

    # def __init__(self,intNodeNumber):
    #     while intNodeNumber != pointer.StaticIntFinalNode:
    #         self.listUsedNode.append(intNodeNumber)
    #         for i in range(len(pointer.StaticListGraph[intNodeNumber-1].listConnection)):
    #             if self.isItUsedNode(pointer.StaticListGraph[intNodeNumber-1].listConnection[i]) == False:
    #                 pointer(pointer.StaticListGraph[intNodeNumber-1].listConnection[i])
    #             if self.isAllNodeUsed == True:
                    