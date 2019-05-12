#Author: Michael Gonzalez
#Course: CS 2302 Data Structures
#Lab 8
#TA: Anindita Nath & Eduuardo Lara
#Purpose:the purpose of this lab is to write specific algorithim techniques to solve 2 problems
#1.(Randomized algorithms) Write a program to "discover" trigonometric identities. Your program should
#test all combinations of the trigonometric expressions shown below and use a randomized algorithm to
#detect the equalities. For your equality testing, generate random numbers in the 􀀀 to  range.
#(a) sin(t)
#(b) cos(t)
#(c) tan(t)
#(d) sec(t)
#(e) -sin(t)
#(f) -cos(t)
#(g) -tan(t)
#(h) sin(-t)
#(i) cos(-t)
#(j) tan(-t)
#(k) sin(t)/cos(t)
#(l) 2 sin(t=2) cos(t=2)
#(m) sin2(t)
#(n) 1 - cos2(t)
#(o) 1-cos(2t)/2
#(p) 1/cos(t)
#2. (Backtracking) The partition problem consists of determining if there is a way to partition a set of integers
#S into two subsets S1 and S2 such that P S1 = P S2. Recall that S1 and S2 are a partition of S if and only
#if S1[S2 = S and S1\S2 = fg. Write a function that solves the partition problem using backtracking. If a
#partition exists, your program should display it; otherwise it should indicate that no partition exists. For
#example, if S = f2; 4; 5; 9; 12g, your program should output the partition S1 = f2; 5; 9g and S2 = f4; 12g
#and if S = f2; 4; 5; 9; 13g your program should indicate that no partition exists.
#Given the little time available, a demo will not be required, thus it is very important

# Last modified May, 11 2019

import random
import math


##################################################
#                  LAB START                     #
##################################################
    
def random_Identity_testing():
    
    t = random.randrange(-360,360)
    
    a = math.sin(t)
    b = math.cos(t)
    c = math.tan(t)
    d = 1/math.cos(t)   #sec is defiend as 1/cos(thetha) since there is no math.sec this had to be done
    e = -math.sin(t)
    f = -math.cos(t)
    g = -math.tan(t)
    h = math.sin(-t)
    i = math.cos(-t)
    j = math.tan(-t)
    k = math.sin(t)/math.cos(t)
    l = 2*math.sin(t/2)*math.cos(t/2)
    m = math.sin(t)*math.sin(t)       # sin^2(t) is not defined in Math so i substituted it by (sin(t)*sin(t))
    n = 1-(math.cos(t)*math.cos(t))   # Cos^2(t) is not defined so i substituded it by (cos(t)*cos(t))
    o = (1-math.cos(2*t))/2
    p = 1/math.cos(t)
    
    L = []
    L.append([a,"sin(t)"])
    L.append([b,"cos(t)"])
    L.append([c,"tan(t)"])
    L.append([d,"sec(t)"])
    L.append([e,"-sin(t)"])
    L.append([f,"-cos(t)"])
    L.append([g,"-tan(t)"])
    L.append([h,"sin(-t)"])
    L.append([i,"cos(-t)"])
    L.append([j,"tan(-t)"])
    L.append([k,"sin(t)/cos(t)"])
    L.append([l,"2sin(t/2)cos(t/2)"])
    L.append([m,"sin^2(t)"])
    L.append([n,"1-cos^2(t)"])
    L.append([o,"1-cos(2*t)/2"])
    L.append([p,"1/cos(t)"])
#    print(L)
    
    z = random.randint(0,15)
    print("Checking identities for:", L[z][1])
    for j in range(len(L)):
        if round(L[z][0],5) == round(L[j][0],5):
            if z != j:
                print("Identity exists:",L[z][1],"=",L[j][1])
            
    
# Function to print the equal sum sets of the array. 
def printSets(set1, set2) : 
  
    # Print set 1. 
    print ("S1: {",set1,"}")
  
    # Print set 2. 
    print ("S2: {",set2,"}")
  
# function to find the sets of the  
# array which have equal sum. 
def findSets(arr, n, set1, set2, sum1, sum2, pos) : 
  
    if (pos == n) :  

        if (sum1 == sum2) : 
            print("A partition exists:")
            printSets(set1, set2) 
            return True
        else : 
            return False     
  
    set1.append(arr[pos]) 
    res = findSets(arr, n, set1, set2, sum1 + arr[pos], sum2, pos + 1) 
  
    if (res) : 
        return res 
    set1.pop() 
    set2.append(arr[pos]) 
  
    return findSets(arr, n, set1, set2, sum1, sum2 + arr[pos], pos + 1) 
  
# Return true if array arr can be partitioned 
# into two equal sum sets or not. 
def isPartitionPoss(arr, n) : 
  
    # Calculate sum of elements in array. 
    sum = 0
  
    for i in range(0, n): 
        sum += arr[i] 
  
    # If sum is odd then array cannot be 
    # partitioned. 
    if (sum % 2 != 0) : 
        return False
  
    # Declare vectors to store both the sets. 
    set1 = [] 
    set2 = [] 
  
    # Find both the sets. 
    return findSets(arr, n, set1, set2, 0, 0, 0) 
  
if __name__ == "__main__":   
    arr = [5, 5, 1, 11] 
    n = len(arr) 
    print("S = {",arr,"}")     #cool trick to print the list 
    if (isPartitionPoss(arr, n) == False) : 
        print ("A partition does not exist") 
    random_Identity_testing()
    
