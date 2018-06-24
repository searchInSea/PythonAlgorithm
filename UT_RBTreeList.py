# -*- coding: utf-8 -*-

from RBTreeList import *

def testRBNodeFun1():
    AA = RBNode(1,BLACK_COLOR,4)
    BB = RBNode(2,RED_COLOR,3)
    AA.L = BB
    BB.p = AA
    print(AA)
    print(BB)
def testRBTreeList():
    List1 = RBTree(RBNode(1, value = 3))
    List1.inserNode(RBNode(2, value = 4))
    List1.inserNode(RBNode(5, value=4))
    List1.inserNode(RBNode(4, value=4))
    List1.inserNode(RBNode(7, value=4))
    List1.inserNode(RBNode(8, value=4))
    List1.inserNode(RBNode(9, value=4))
    List1.inserNode(RBNode(10, value=4))
    List1.delNodeByKey(8)
    List1.inserNode(RBNode(8, value=4))
    List1.inserNode(RBNode(11, value=4))
    List1.inserNode(RBNode(12, value=4))
    List1.inserNode(RBNode(13, value=4))
    List1.inserNode(RBNode(14, value=4))
    List1.inserNode(RBNode(15, value=4))
    List1.delNodeByKey(5)
    List1.delNodeByKey(7)
    #print(List1)
    List1.floorWalk()

#testRBNodeFun1()
testRBTreeList()