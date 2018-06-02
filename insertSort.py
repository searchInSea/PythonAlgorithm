# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class SortNum(object):
    def __init__(self, A=None):
        self.A=A
        
    def insertSort(self):
        for i in range(1,len(self.A)):
            key=self.A[i]
            
            for j in range(i-1,-1,-1):
                if self.A[j]>key: #1,2,3,4...
                    self.A[j+1]=self.A[j]
                    if j == 0:
                        j -= 1
                else:
                    break
                
            self.A[j+1]=key
        return A
    
    def selctSort(self):
        for i in range(1,len(self.A)-1):
            minIdx = i-1
            for j in range(i,len(self.A)):
                if self.A[minIdx] > self.A[j]:
                    minIdx = j
            tem=self.A[minIdx]
            self.A[minIdx]=self.A[i-1]
            self.A[i-1]=tem
        return self.A
    
    def __insertSortDiGuiIner(self, n):
        #print '__insertSortDiGuiIner',n
        key=self.A[n]
        for i in range(n-1, -1, -1):
            if self.A[i] > key:
                self.A[i+1] = self.A[i]
                if i == 0:
                    i -= 1
            else:
                break
            
        self.A[i+1] = key
        
    def __insertSortDiGui(self, n):
        if n > 0:
            #print n
            self.__insertSortDiGui(n-1)
            self.__insertSortDiGuiIner(n)
            
    def insertSortDiGui(self):
        self.__insertSortDiGui(len(self.A)-1)
        return self.A
        
    def __mergeSort(self, A):
        if len(A)>1:
            MidIdx = len(A)/2
            B1 = self.__mergeSort(A[:MidIdx])
            B2 = self.__mergeSort(A[MidIdx:])
            IdxB1 = 0
            IdxB2 = 0
            B=[]
            for i in range(len(B1)+len(B2)):
                if IdxB1 >= len(B1):
                    B += B2[IdxB2:]
                    break
                if IdxB2 >= len(B2):
                    B += B1[IdxB1:]
                    break
                
                if B1[IdxB1] > B2[IdxB2]:
                    B.append(B2[IdxB2])
                    IdxB2 += 1
                else:
                    B.append(B1[IdxB1])
                    IdxB1 += 1
            return B
        else:
            return A
        
    def mergeSort(self):
        self.A = self.__mergeSort(self.A)
        return self.A
    
    def findValHalf(self, value):
        beginIdx = 0
        endIdx = len(self.A)-1
        halfIdx = (len(self.A) - 1)/2
        while endIdx - beginIdx > 1 and self.A[halfIdx] != value:
            if self.A[halfIdx] > value:
                endIdx = halfIdx
                halfIdx = (halfIdx + beginIdx)/2
            elif self.A[halfIdx] < value:
                beginIdx = halfIdx
                halfIdx = (halfIdx + endIdx)/2
                
        if self.A[halfIdx] == value:
            return halfIdx
        elif self.A[beginIdx] == value:
            return beginIdx
        elif self.A[endIdx] == value:
            return endIdx
        return None
        

if __name__ == '__main__':
    A=[8,3,100.1,10,6,7]
    objSort=SortNum(A)
    #print objSort.insertSort()
    #print objSort.selctSort()
    #print objSort.insertSortDiGui()
    print objSort.mergeSort()
    print objSort.findValHalf(100.1)