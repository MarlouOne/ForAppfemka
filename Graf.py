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
            
    def getRootLenToNode(self,intNodeIndex):
        return self.listRoadlen[self.listConnection.index(intNodeIndex)]
            
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
    
    def stepBack(self,StaticIntFinalNode):
        if self.bFlagEnd == False:            
            try:
                intNode = self.listUsedNode[-2]
                self.listUsedNode = self.listUsedNode[:-2]
                self.getAllWays(intNode,StaticIntFinalNode)
            except IndexError:
                self.bFlagEnd = True
    
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
        
    def getAllWays(self,intNode,StaticIntFinalNode):  
        self.listUsedNode.append(intNode)
        
        if intNode == StaticIntFinalNode:
            self.listCorrectWays.append(self.listUsedNode)
            self.listAllWays.append(self.listUsedNode)
            self.stepBack(StaticIntFinalNode)
            
        for i in range(len(pointer.StaticListGraph[intNode-1].listConnection)):
            intNextNode = pointer.StaticListGraph[intNode-1].listConnection[i]
            if self.isItUsedWay(intNextNode) and self.isItUsedNode(intNextNode) :              
                self.getAllWays(intNextNode, StaticIntFinalNode)
             
        self.listAllWays.append(self.listUsedNode)
        self.stepBack(StaticIntFinalNode)
        return self.listCorrectWays[:-1]
    
    def findWays(intStartNode,intFinalNode, listGraph):
        pointer.setStaticVar(listGraph)
        pObj = pointer.getAllWays(pointer(),intStartNode,intFinalNode)
        print(f' Final ways {pObj} \n Count of ways {len(pObj)}')
        pointer.getMinWay(pObj)
        pointer.getMaxWay(pObj)
    
    def getMinWay(listWays):
        listMinWay = []
        intMinWay  = 1000000
        intWayLen  = 0
        for intWay in range(len(listWays)):
            intWayLen = 0
            for index in range(len(listWays[intWay])-1):
                nodeObj = pointer.StaticListGraph[listWays[intWay][index]-1]
                intWayLen += nodeObj.getRootLenToNode(listWays[intWay][index+1])
            if intWayLen < intMinWay :
                intMinWay = intWayLen
                listMinWay = listWays[intWay]
        print(f'Min way is {intMinWay} on {listMinWay}')
                
    def getMaxWay(listWays):
        listMaxWay = []
        intMaxWay  = 0
        intWayLen  = 0
        for intWay in range(len(listWays)):
            intWayLen = 0
            for index in range(len(listWays[intWay])-1):
                nodeObj = pointer.StaticListGraph[listWays[intWay][index]-1]
                intWayLen += nodeObj.getRootLenToNode(listWays[intWay][index+1])
            if intWayLen > intMaxWay :
                intMaxWay = intWayLen
                listMaxWay = listWays[intWay]
        print(f'Max way is {intMaxWay} on {listMaxWay}')                
                
def main():
    listConnection = [[2,8,9],[1,4],[4,6],[2,3,8],[6,7,8],[3,5,7],[5,6,9],[1,4,5],[1,7]]
    listRoadlen    = [[10,8,31],[10,7],[27,10],[7,27,9],[17,15,15],[10,17,21],[15,21,12],[8,9,15],[31,12]]
    listGraph = node.makeGraph(listConnection,listRoadlen)
    node.printGraph(listGraph)
    
    pointer.findWays(6,2,listGraph)
    
main()
