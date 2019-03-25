#Author: Michael Gonzalez
#Course: CS 2302 Data Structures
#Lab 4 B-Trees
#TA: Anindita Nath & Eduardo Lara
#Purpose:the purpose of this lab is to modify the code given in class and implement various methods.
#1. Compute the height of the tree
#2. Extract the items in the B-tree into a sorted list.
#3. Return the minimum element in the tree at a given depth d.
#4. Return the maximum element in the tree at a given depth d.
#5. Return the number of nodes in the tree at a given depth d.
#6. Print all the items in the tree at a given depth d.
#7. Return the number of nodes in the tree that are full.
#8. Return the number of leaves in the tree that are full.
#9. Given a key k, return the depth at which it is found in the tree, of -1 if k is not in the tree.
# Last modified March 24, 2019

import math as math

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
        
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
        
def FD(T,k):
    if k in T.item:
        return 0
    if T.isLeaf:
        return -1
    if k>T.item[-1]:
        d = FD(T.child[-1],k)
    else:
        for i in range(len(T.item)):
            if k < T.item[i]:
                d = FD(T.child[i],k)
    if d == -1:
        return -1
    return d +1
        
######################################################################### 
#                                LAB Start                              #
#########################################################################
#1 Compute the height of the tree

def height(T):
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])



########################################## 
#2. Extract the items in the B-tree into a sorted list.

def MakeList(T):
    if T.isLeaf:
        for t in T.item:
            List.append(t)
    else:
        for i in range(len(T.item)):
            MakeList(T.child[i])
            List.append(T.item[i])
        MakeList(T.child[len(T.item)])

########################################## 
#3. Return the minimum element in the tree at a given depth d.

def MinElementAtDepthD(T,d):
    if height(T) < d:
        return -math.inf
    if d==0:
        return T.item[0]
    else:
        return MinElementAtDepthD(T.child[0],d-1)    


########################################## 
#4. Return the maximum element in the tree at a given depth d

def MaximumElementAtDepthD(T,d):
    if height(T) < d:
        return -math.inf
    if d==0:
        return T.item[len(T.item)-1]
    else:
        return MaximumElementAtDepthD(T.child[len(T.item)],d-1)


########################################## 
#5. Return the number of nodes in the tree at a given depth d.

def NumNodesAtDepthD(T,d):
    count = 0
    if height(T) < d:
        return -math.inf
    if d==0:
        return len(T.item)
    else:
        for c in T.child:
            count += NumNodesAtDepthD(c,d-1)
    return count


########################################## 
#6. Print all the items in the tree at a given depth d.
def PrintAtDepthD(root, d): 
    if root is None: 
        return 
    if d == 0: 
        for i in range(len(root.item)):
            print(root.item[i],end=" ")
    else: 
        for c in root.child:
            PrintAtDepthD(c, d-1)


########################################## 
#7. Return the number of nodes in the tree that are full.

def FullNodeNum(T):
    tot = 0
    if T.max_items == len(T.item) and T.isLeaf:
        return 1
    elif T.max_items == len(T.item) and T.isLeaf == False:
        for c in T.child:
            tot += FullNodeNum(c)
        return tot +1
    else:
        for c in T.child:
            tot += FullNodeNum(c)
    return tot


########################################## 
#8. Return the number of leaves in the tree that are full

def FullNodeLeaf(T):
    tot = 0
    if T.max_items == len(T.item) and T.isLeaf:
        return 1
    else:
        for c in T.child:
            tot += FullNodeLeaf(c)
    return tot

########################################## 
#9. Given a key k, return the depth at which it is found in the tree,
# of -1 if k is not in the tree

def SearchAndDepth(T,k):
    if k in T.item:
        return 0
    if T.isLeaf:
        return -1
    d = SearchAndDepth(T.child[FindChild(T,k)],k) 
    if d == -1:
        return -1
    return d +1

#########################################                                   
    
L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45,12,13,14]

#L = [30, 50, 10, 20, 60, 70, 100, 40,21,22,23,24,25,26,27,19,18,17,11,16,15,14,13,12,9,8,7,6,5,4,3,28,29,31,32,33,34,35,41,42,80,90,95]
#L = [40,50,52,20,10,45,44,43,21,22,23,1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,53,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,53,53,53,53,53,53,53,60,60,60,60,60,60,60,30,60,60,22,22,22,22,22,22,22,22,22,22,22,22]
T = BTree()   
List = [] 
for i in L:
    print('Inserting',i)
    Insert(T,i)
    PrintD(T,'') 
    #Print(T)
    print('\n####################################')
    
#SearchAndPrint(T,60)
#SearchAndPrint(T,200)
#SearchAndPrint(T,25)
#SearchAndPrint(T,20)


#1 Compute the height of the tree

print("Height is:",end=" ")
print(height(T))
print()


#2. Extract the items in the B-tree into a sorted list.

MakeList(T)
print("Sorted List from B-tree T:")
print(List)
print()


#3. Return the minimum element in the tree at a given depth d.

print("Minimum element in the tree at depth 1:",end=" ")
print(MinElementAtDepthD(T,1)) 
print()


#4. Return the maximum element in the tree at a given depth d

print("Maximum element in the tree at depth 1:",end=" ")
print(MaximumElementAtDepthD(T,1))  
print()


#5. Return the number of nodes in the tree at a given depth d.

print("Number of Nodes in the tree at depth 1:",end=" ")
print(NumNodesAtDepthD(T,2))
print()


#6. Print all the items in the tree at a given depth d.

print("Printing all items in the tree at depth 1:",end=" ")
PrintAtDepthD(T,1) 
print()
print()


#7. Return the number of nodes in the tree that are full.

print("Number of Nodes that are full in the tree:",end=" ")
print(FullNodeNum (T))
print()


#8. Return the number of leaves in the tree that are full

print("Number of full leaf Nodes the tree:",end=" ")
print(FullNodeLeaf(T))
print()


#9. Given a key k, return the depth at which it is found in the tree,
# of -1 if k is not in the tree


print("The depth where this key resides is at depth:",end=" ")
print(SearchAndDepth(T,20))
print()
