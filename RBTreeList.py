# -*- coding: utf-8 -*-

from CONSTVAL import *
from Queue import *

class RBNode(object):
    def __init__(self, key = NULL,color = RED_COLOR, value = NULL, p = NULL, L = NULL, R = NULL):
        self.p = p   #指向父节点
        self.L = L   #指向左子树
        self.R = R   #指向右子树
        self.color = color  #红黑
        self.key = key      #用于排序的key
        self.value = value  #卫星数据

    def __str__(self):
        #print self.__class__
        retStr = 'key='+str(self.key)+ \
                 ('\ncolor='+'Red' if self.color == RED_COLOR else '\nBlack')+ \
                '\nValue='+str(self.value)+ \
                 '\np='+str(hex(id(self.p)))+' key:'+ ('None' if (self.p == NULL) else str(self.p.key))+ \
                 '\nL='+ str(hex(id(self.L)))+' key:'+('None' if (self.L == NULL) else str(self.L.key))+ \
                 '\nR='+str(hex(id(self.R)))+ ' key:'+('None' if (self.R == NULL) else str(self.R.key))+'\n'
        #print(retStr)
        return retStr

class RBTree(object):
    InvalidNode = RBNode(color = BLACK_COLOR)
    walkQueue = Queue(2048)
    def __init__(self, root = NULL):
        self.root = root
        if root:
            root.p = RBTree.InvalidNode
            root.color = BLACK_COLOR
            root.L = RBTree.InvalidNode
            root.R = RBTree.InvalidNode

    def __RotLeft(self, RotNode):
        """左旋"""
        rightNode = RotNode.R
        rightNode.p = RotNode.p
        if RotNode.p.L == RotNode:
            RotNode.p.L = rightNode
        elif RotNode.p.R == RotNode:
            RotNode.p.R = rightNode

        RotNode.R = rightNode.L
        rightNode.L.p = RotNode

        rightNode.L = RotNode
        RotNode.p = rightNode

        if RotNode == self.root:
            self.root = rightNode

    def __RotRight(self, RotNode):
        """右旋"""
        leftNode = RotNode.L
        leftNode.p = RotNode.p
        if RotNode.p.L == RotNode:
            RotNode.p.L = leftNode
        else:
            RotNode.p.R = leftNode

        RotNode.L = leftNode.R
        leftNode.R.p = RotNode

        leftNode.R = RotNode
        RotNode.p = leftNode
        if RotNode == self.root:
            self.root = leftNode

    def insertFixUp(self, Node):
        """插入修正"""
        while Node.p.color == RED_COLOR:
            if Node.p.p.L == Node.p:
                uncleNode = Node.p.p.R

                if uncleNode.color == RED_COLOR:  #case1:叔父节点颜色为红色
                    Node.p.color = BLACK_COLOR
                    uncleNode.color = BLACK_COLOR
                    Node.p.p.color = RED_COLOR
                    Node = Node.p.p               #case1:问题从node提升到了node.p.p
                elif Node.p.R == Node:
                    self.__RotLeft(Node.p)   #case2: 将case2转化成case3
                    Node = Node.L
                else:
                    Node.p.color = BLACK_COLOR    #case3:右旋解决
                    Node.p.p.color = RED_COLOR
                    self.__RotRight(Node.p.p)

            elif Node.p.p.R == Node.p:
                uncleNode = Node.p.p.L

                if uncleNode.color == RED_COLOR:  #case1:叔父节点颜色为红色
                    uncleNode.color = BLACK_COLOR
                    Node.p.color = BLACK_COLOR
                    Node.p.p.color = RED_COLOR
                    Node = Node.p.p              #case1:问题从node提升到了node.p.p
                elif Node.p.L == Node:
                    self.__RotRight(Node.p)      #case2: 将case2转化成case3
                    Node = Node.R
                else:
                    Node.p.color = BLACK_COLOR   #case3:左旋解决
                    Node.p.p.color = RED_COLOR
                    self.__RotLeft(Node.p.p)
        self.root.color = BLACK_COLOR

    def inserNode(self, Node):
        """插入修正"""
        Node.color = RED_COLOR
        Node.L = RBTree.InvalidNode
        Node.R = RBTree.InvalidNode
        pNode = self.root
        if pNode == NULL:
            self.root = Node

        while pNode != RBTree.InvalidNode:
            pNodeTmp = pNode
            if Node.key < pNode.key:
                pNode = pNode.L
            else:
                pNode = pNode.R

        if Node.key < pNodeTmp.key:
            pNodeTmp.L = Node
        else:
            pNodeTmp.R = Node
        Node.p = pNodeTmp

        self.insertFixUp(Node)

    def __FirstWalk(self, Node):
        if Node == NULL or Node == RBTree.InvalidNode:
            return

        if Node.L != RBTree.InvalidNode and Node.L != NULL:
            self.__FirstWalk(Node.L)
        print(Node.key)
        if Node.R != RBTree.InvalidNode and Node.R != NULL:
            self.__FirstWalk(Node.R)

    def floorWalk(self):
        if self.root == NULL:
            return
        RBTree.walkQueue.put(self.root)
        while False == RBTree.walkQueue.empty():
            RBNodeTmp = RBTree.walkQueue.get()
            print(RBNodeTmp)
            if RBNodeTmp.L != NULL and RBNodeTmp.L != RBTree.InvalidNode:
                RBTree.walkQueue.put(RBNodeTmp.L)
            if RBNodeTmp.R != NULL and RBNodeTmp.R != RBTree.InvalidNode:
                RBTree.walkQueue.put(RBNodeTmp.R)

    def __TransPlant(self, delNode, newNode):  #只处理父节点
        newNode.p = delNode.p
        if delNode.p.L == delNode:
            delNode.p.L = newNode
        elif delNode.p.R == delNode:
            delNode.p.R = newNode
        if self.root == delNode:
            self.root = newNode

    def searchNode(self, key):
        nodeTmp = self.root
        while nodeTmp != NULL and nodeTmp.key != key and nodeTmp != RBTree.InvalidNode:
            if key < nodeTmp.key:
                nodeTmp = nodeTmp.L
            else:
                nodeTmp = nodeTmp.R
        if key == nodeTmp.key:
            return nodeTmp
        else:
            return NULL

    def __findMinNode(self, TreeRoot):
        NodeTmp = TreeRoot
        while NodeTmp.L != NULL and NodeTmp.L != RBTree.InvalidNode:
            NodeTmp = NodeTmp.L
        return NodeTmp

    def __findMaxNode(self, TreeRoot):
        NodeTmp = TreeRoot
        while NodeTmp.R != NULL and NodeTmp.R != RBTree.InvalidNode:
            NodeTmp = NodeTmp.R
        return NodeTmp

    def findMinNode(self):
        return self.__findMinNode(self.root)

    def findMaxNode(self):
        return self.__findMaxNode(self.root)

    def delFixUp(self, fixNodex):
        """需要增加一个黑色节点"""
        while fixNodex.color == BLACK_COLOR and fixNodex != self.root:
            if fixNodex.p.L == fixNodex:
                brothNode = fixNodex.p.R
                if brothNode.color == RED_COLOR:    #case1 兄弟节点为红色,修正兄弟节点为黑色
                    fixNodex.p.color = RED_COLOR
                    brothNode.color = BLACK_COLOR
                    self.__RotLeft(fixNodex.p)
                    brothNode = fixNodex.p.R

                if brothNode.L == BLACK_COLOR and brothNode.R == BLACK_COLOR:
                    brothNode.color = RED_COLOR    #case2 兄弟节点为黑色，兄弟子节点为黑色
                    fixNodex = fixNodex.p
                elif brothNode.R == BLACK_COLOR:    #case3 兄弟节点的右节点为黑色,左节点为红色,将右节点转化为红色
                    brothNode.L = BLACK_COLOR
                    brothNode.color = RED_COLOR
                    self.__RotRight(brothNode)
                    brothNode = fixNodex.p.R
                else:
                    #case4 兄弟节点为黑色,其右节点为红色
                    brothNode.color = fixNodex.p.color
                    fixNodex.p.color = BLACK_COLOR
                    self.__RotLeft(fixNodex.p)
                    brothNode.R.color = BLACK_COLOR
                    fixNodex = self.root

            else:
                brothNode = fixNodex.p.L
                if brothNode.color == RED_COLOR:  # case1 兄弟节点为红色,修正兄弟节点为黑色
                    fixNodex.p.color = RED_COLOR
                    brothNode.color = BLACK_COLOR
                    self.__RotRight(fixNodex.p)
                    brothNode = fixNodex.p.L

                if brothNode.L == BLACK_COLOR and brothNode.R == BLACK_COLOR:
                    brothNode.color = RED_COLOR  # case2 兄弟节点为黑色，兄弟子节点为黑色
                    fixNodex = fixNodex.p
                elif brothNode.L == BLACK_COLOR:  # case3 兄弟节点的左节点为黑色,右节点为红色,将左节点转化为红色
                    brothNode.R = BLACK_COLOR
                    brothNode.color = RED_COLOR
                    self.__RotLeft(brothNode)
                    brothNode = fixNodex.p.L
                else:
                    # case4 兄弟节点为黑色,其左节点为红色
                    brothNode.color = fixNodex.p.color
                    fixNodex.p.color = BLACK_COLOR
                    self.__RotRight(fixNodex.p)
                    brothNode.L.color = BLACK_COLOR
        fixNodex.color = BLACK_COLOR

    def delNode(self, delNode):
        delOriginColory = delNode.color

        if delNode.L == RBTree.InvalidNode or delNode.L == NULL:
            self.__TransPlant(delNode,delNode.R)
            newNodex = delNode.R
        elif delNode.R == RBTree.InvalidNode or delNode.R == NULL:
            self.__TransPlant(delNode, delNode.L)
            newNodex = delNode.L
        else:
            newNodeTmp = self.__findMinNode(delNode.R)
            delOriginColory = newNodeTmp.color
            newNodex = newNodeTmp.R
            newNodex.p = newNodeTmp  #当newNodex为无效节点时newNodex.p是无效值,导致216行case4左旋失败
            if delNode.R != newNodeTmp and newNodeTmp.R != NULL:
                self.__TransPlant(newNodeTmp, newNodeTmp.R)
                newNodeTmp.R = delNode.R
                delNode.R.p = newNodeTmp

            self.__TransPlant(delNode, newNodeTmp)
            newNodeTmp.L = delNode.L
            delNode.L.p = newNodeTmp
            newNodeTmp.color = delNode.color

        if delOriginColory == BLACK_COLOR:
            self.delFixUp(newNodex)
    def delNodeByKey(self, key):
        delNodeTmp = self.searchNode(key)

        if delNodeTmp != NULL and delNodeTmp != RBTree.InvalidNode:
            self.delNode(delNodeTmp)

    def __str__(self):
        self.__FirstWalk(self.root)
        return '\n'

if __name__ == '__main__':
    pass