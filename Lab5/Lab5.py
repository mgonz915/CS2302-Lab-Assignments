#Author: Michael Gonzalez
#Course: CS 2302 Data Structures
#Lab 5
#TA: Anindita Nath
#Purpose:the purpose of this lab is to modify the code given in class and implement various methods.

# Last modifiedmarch 31, 2019


import matplotlib.pyplot as plt
import numpy as np
import math
import time 

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right    
        
        
class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size,num_items=0):  
        self.item = []
        self.num_items = num_items
        if num_items//size==1:
            size = (size*2)+1
        for i in range(size):
            self.item.append([])
            
def BSTChoice():
    T = None
    
    f = open('glove.6B.50d.txt',encoding='utf-8')    
    for line in f:
        lines = line.split()
        name  = [lines[0]]
        nums = []
        for i in range(len(lines)-1):
            nums.append(float(lines[i+1]))
        p = [name,nums]
    
        T = Insert(T,p)
    print()
    print("Binary Search Tree stats:")
    print("Number of nodes: ",CountNodes(T))
    print("Height: ",maxDepth(T))
    elapsed_time = time.time()-start
    print("Running time for binary search tree construction:", round(elapsed_time),"seconds")
    print()
    print("Reading word file to determine similarities")
    print()
    print("Word similarities found:")
    print("Similarity [bear,bear] = ",round(simT('bear','bear',T),4))
    print("Similarity [barley,shrimp] = ",round(simT('barley','shrimp',T),4))
    print("Similarity [barley,oat] = ",round(simT('barley','oat',T),4))
    print("Similarity [federer,baseball] = ",round(simT('federer','baseball',T),4))
    print("Similarity [federer,tennis] = ",round(simT('federer','tennis',T),4))
    print("Similarity [harvard,stanford] = ",round(simT('harvard','stanford',T),4))
    print("Similarity [harvard,utep] = ",round(simT('harvard','utep',T),4))
    print("Similarity [harvard,ant] = ",round(simT('harvard','ant',T),4))
    print("Similarity [raven,crow] = ",round(simT('raven','crow',T),4))
    print("Similarity [raven,whale] = ",round(simT('raven','whale',T),4))
    print("Similarity [spain,france] = ",round(simT('spain','france',T),4))
    print("Similarity [spain,mexico] = ",round(simT('spain','mexico',T),4))
    print("Similarity [mexico,france] = ",round(simT('mexico','france',T),4))
    print("Similarity [mexico,guatemala] = ",round(simT('mexico','guatemala',T),4))
    print("Similarity [computer,platypus] = ",round(simT('computer','platypus',T),4))
    print()
    elapsed_time2 = time.time()-start
    print("Running time for binary search tree query processing:", round(elapsed_time2),"seconds")

#    data = np.array[file.readline().split()]
#    for temp in data:
#        print(temp)
#    
#    return
#    
    
def HashChoice():
    H = HashTableC(11)
    f = open('glove.6B.50d.txt',encoding='utf-8')    
    for line in f:
        lines = line.split()
        name  = [lines[0]]
        nums = []
        for i in range(len(lines)-1):
            nums.append(float(lines[i+1]))
        p = [name,nums]
        InsertC(H,p,p[1])
        
    print()
    print("Hash table stats:")
    print("Initial table size:")
    print("Final table size:")
    print("Load factor:",LoadFactor(H))
    print("Percentage of empty lists:")
    print("Standard deviation of the lengths of the lists:")
    elapsed_time = time.time()-start
    print("Running time for Hash Table construction:", round(elapsed_time),"seconds")
    print()
    print("Reading word file to determine similarities")
    print()
    print("Word similarities found:")
    print("Similarity [bear,bear] = ",round(simH('bear','bear',H),4))
    print("Similarity [barley,shrimp] = ",round(simH('barley','shrimp',H),4))
    print("Similarity [barley,oat] = ",round(simH('barley','oat',H),4))
    print("Similarity [federer,baseball] = ",round(simH('federer','baseball',H),4))
    print("Similarity [federer,tennis] = ",round(simH('federer','tennis',H),4))
    print("Similarity [harvard,stanford] = ",round(simH('harvard','stanford',H),4))
    print("Similarity [harvard,utep] = ",round(simH('harvard','utep',H),4))
    print("Similarity [harvard,ant] = ",round(simH('harvard','ant',H),4))
    print("Similarity [raven,crow] = ",round(simH('raven','crow',H),4))
    print("Similarity [raven,whale] = ",round(simH('raven','whale',H),4))
    print("Similarity [spain,france] = ",round(simH('spain','france',H),4))
    print("Similarity [spain,mexico] = ",round(simH('spain','mexico',H),4))
    print("Similarity [mexico,france] = ",round(simH('mexico','france',H),4))
    print("Similarity [mexico,guatemala] = ",round(simH('mexico','guatemala',H),4))
    print("Similarity [computer,platypus] = ",round(simH('computer','platypus',H),4))
    print()
    elapsed_time2 = time.time()-start
    print("Running time for hash table query processing:", round(elapsed_time2),"seconds")


def dotProduct(e0,e1):
    tot = 0
    for i in range(len(e0)):
        tot += e0[i]*e1[i]
    return tot

def Magnitude(ex):
    return math.sqrt(dotProduct(ex,ex))


def simH(w0,w1,H):
    e0 = FindC(H,w0)
    e1 = FindC(H,w1)
    e0ne1 = dotProduct(e0,e1)
    Me0 = Magnitude(e0)
    Me1 = Magnitude(e1)
    
    result = (e0ne1)/(Me0*Me1)
    return result

def simT(w0,w1,T):
    e0 = Find(T,w0)
    e1 = Find(T,w1)
    e0ne1 = dotProduct(e0,e1)
    Me0 = Magnitude(e0)
    Me1 = Magnitude(e1)
    
    result = (e0ne1)/(Me0*Me1)
    return result
#########################################################    
        #               BST Code
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item[0][0] > newItem[0][0]:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T

def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item[0][0],end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item[0][0])
        InOrderD(T.left,space+'   ')
  

def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

  
def CountNodes(T):
    Count = 0
    if T is not None:
        Count += 1
    else:
        return 0
    return Count + CountNodes(T.right) + CountNodes(T.left)

def maxDepth(T): 
    if T is None: 
        return 0 ;  
  
    else : 
  
        # Compute the depth of each subtree 
        lDepth = maxDepth(T.left) 
        rDepth = maxDepth(T.right) 
  
        # Use the larger one 
        if (lDepth > rDepth): 
            return lDepth+1
        else: 
            return rDepth+1   
        
def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item[0][0] == k:
        return T.item[1]
    if T.item[0][0]<k:
        return Find(T.right,k)
    return Find(T.left,k)

#########################################################
    #````````HASH Code
def InsertC(H,k,l):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    b = h(k[0][0],len(H.item))
    H.item[b].append([k[0][0],l]) 
    H.num_items += 1
    
   
def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    b = h(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0] == k:
            return  H.item[b][i][1]
    return b, -1, -1

def h(s,n):
    r = 0
    for c in s:
        r = (r*n + ord(c))% n
    return r

def LoadFactor(H):
    count = 0.0
    for i in H.item:
       count +=len(i)
    return count/len(H.item)
  
#########################################################
#
#H = HashTableC(11)
#A = ['data','structures','computer','science','university','of','texas','at','el','paso']
#for a in A:
#    InsertC(H,a,len(a))
#    print(H.item)
#
#for a in A: # Prints bucket, position in bucket, and word length
#    print(a,FindC(H,a))

#########################################
#           User Interface              #
#########################################
start = time.time()
print("Choose table implementation")
print("Type 1 for binary search tree or 2 for hash table with chaining")
x =input("Choice: ")
print()

if int(x) == 1:
    print("Building binary search tree")
    BSTChoice()
    
elif int (x) == 2:
    print("Building hash table with chaining Hash table")
    HashChoice()
    
else:
    print("Wrong input Try Again")
    
    
