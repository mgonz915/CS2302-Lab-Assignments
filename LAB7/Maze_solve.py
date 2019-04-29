#Author: Michael Gonzalez
#Course: CS 2302 Data Structures
#Lab 7
#TA: Anindita Nath & Eduuardo Lara
#Purpose:the purpose of this lab is to modify our maze code to handle 3 cases
#1.
#(a) A path from source to destination is not guaranteed to exist (when m < n -1)
#(b) The is a unique path from source to destination (when m = n-1)
#(c) There is at least one path from source to destination (when m > n -1).
#2.Write a method to build the adjacency list representation of your maze.
#3.Implement the following algorithms to solve the maze you created, assuming the starting position is
#bottom-left corner and the goal position is the top-right corner.
#(a) Breadth-first search.
#(b) Depth-first search using a stack. This is identical to breadth-first search. but the queue is replaced
#by a stack.
#(c) Depth-first using recursion.
# Last modified April,28 2019

import matplotlib.pyplot as plt
import numpy as np
import random
import time 
import queue
import dsf

def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)
    return ax
    

def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

def CountSets(S):
    num_sets = 0
    for i in range(len(S)):
        if S[i]<0:
            num_sets += 1
        dsf.find_c(S,i)
    return num_sets

###################################################
#                       LAB START


#created a method to draw a series off lines if there is a solution
def draw_path(ax,prev,v,xe,ye):
    if prev[v] != -1:
        if v == prev[v]+maze_cols:
            xi= xe
            yi=ye-1
            draw_path(ax,prev,prev[v],xi,yi)
            ax.plot([xi,xe],[yi,ye],linewidth=1,color='r')
            
        if  v == prev[v]-maze_cols:
            xi= xe
            yi=ye+1
            draw_path(ax,prev,prev[v],xi,yi)
            ax.plot([xi,xe],[yi,ye],linewidth=1,color='r')       
            
        if v == prev[v]+1:
            xi= xe-1
            yi=ye
            draw_path(ax,prev,prev[v],xi,yi)
            ax.plot([xi,xe],[yi,ye],linewidth=1,color='r')
            
        if v == prev[v]-1:
            xi= xe+1
            yi=ye
            draw_path(ax,prev,prev[v],xi,yi)
            ax.plot([xi,xe],[yi,ye],linewidth=1,color='r')

# method for if the user choses m < n-1
def Choice_1(S,walls,m):
    G = []
    for i in range(maze_cols*maze_rows):
        G.append([])
    while m > 0:
        d = random.randint(0,len(walls)-1)
        print('removing wall ',walls[d])
        if dsf.find(S,walls[d][0]) != dsf.find(S,walls[d][1]):    
     #       dsf.union(S,walls[d][0],walls[d][1])
            dsf.union_by_size(S,walls[d][0],walls[d][1])
            poppedWall = walls.pop(d)
            G[poppedWall[0]].append(poppedWall[1])
            G[poppedWall[1]].append(poppedWall[0])
        m = m-1
    dsf.draw_dsf(S)
    pic = draw_maze(walls,maze_rows,maze_cols)
    print()
    print("breadth_first_search")
    Path = breadth_first_search(G,0)
    draw_path(pic,Path,num_cells-1,maze_cols-.5,maze_rows-.5)
    print(Path)
    printPath(Path,num_cells-1)
    return G
    


# method for if the user choses m > n-1
def Choice_2(S,walls,m):
    G = []
    for i in range(maze_cols*maze_rows):
        G.append([])
    while m > 0:
        d = random.randint(0,len(walls)-1)
        if dsf.find(S,walls[d][0]) != dsf.find(S,walls[d][1]):    
            print('removing wall ',walls[d])
     #       dsf.union(S,walls[d][0],walls[d][1])
            dsf.union_by_size(S,walls[d][0],walls[d][1])
            poppedWall = walls.pop(d)
            G[poppedWall[0]].append(poppedWall[1])
            G[poppedWall[1]].append(poppedWall[0])
        m = m-1
    dsf.draw_dsf(S)
    pic = draw_maze(walls,maze_rows,maze_cols)
    print()
    print("breadth_first_search")
    Path = breadth_first_search(G,0)
    draw_path(pic,Path,num_cells-1,maze_cols-.5,maze_rows-.5)
    print(Path)
    printPath(Path,num_cells-1)
    return G


# method for if the user choses m = n-1
def Choice_3(S,walls,num_cells):
    G = []
    for i in range(num_cells):
        G.append([])
    while CountSets(S) > 1:
        d = random.randint(0,len(walls)-1)
        print('removing wall ',walls[d])
        if dsf.find(S,walls[d][0]) != dsf.find(S,walls[d][1]):    
     #       dsf.union(S,walls[d][0],walls[d][1])
            dsf.union_by_size(S,walls[d][0],walls[d][1])
            poppedWall = walls.pop(d)
            G[poppedWall[0]].append(poppedWall[1])
            G[poppedWall[1]].append(poppedWall[0])
    dsf.draw_dsf(S)
    pic = draw_maze(walls,maze_rows,maze_cols)
    print()
    print("breadth_first_search")
    Path = breadth_first_search(G,0)
    draw_path(pic,Path,num_cells-1,maze_cols-.5,maze_rows-.5)
    print(Path)
    printPath(Path,num_cells-1)
    return G

#method used to print path as an array
def printPath(prev,v):
    if prev[v] != -1:
        printPath(prev,prev[v])
        print(" - ")
    print(v)



def breadth_first_search(G,v):
    visited =np.zeros(len(G),dtype=bool)
    prev = np.zeros(len(G),dtype=int)-1
    Q = queue.Queue()
    Q.put(v)
    visited[v] = True
    while not Q.empty():
        u = Q.get()
        for t in G[u]:
            if not visited[t]:
                visited[t] = True
                prev[t] = u
                Q.put(t)
    return prev

def Depth_first_search_Stack(G,v):
    visited =np.zeros(len(G),dtype=bool)
    prev = np.zeros(len(G),dtype=int)-1
    stack = []
    stack.append(v)
    visited[v] = True
    while not len(stack)<=0:
        u = stack.pop()
        for t in G[u]:
            if not visited[t]:
                visited[t] = True
                prev[t] = u
                stack.append(t)
    return prev

def depth_first_search_Rec(G,source):
    visited[source] = True
    for t in G[source]:
        if not visited[t]:
            prev[t] = source
            depth_first_search_Rec(G,t)
   





if __name__ == "__main__":
    #########################################
    #           User Interface              #
    #########################################
    
    start = time.time()
    maze_rows = 8
    maze_cols = 12
    num_cells = maze_rows*maze_cols
    
    plt.close("all") 
    #Maze creation
    
    walls = wall_list(maze_rows,maze_cols)
    
    draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 
    
    S = dsf.DisjointSetForest(num_cells)
    dsf.draw_dsf(S)
    
    
    
    
    
    print("n, the number of cells:",num_cells)
    x =input("Type m, the number of walls to remove:")
    print()
    
    #Choice m < n-1
    if int(x) < num_cells-1:
        print("A path from source to destination is not guaranteed to exist (m < n -1)")
        Gr = Choice_1(S,walls,int(x))
        print("depth_first_search Stack")
        path3 = Depth_first_search_Stack(Gr,0)
        printPath(path3,num_cells-1)
        print(path3)
        print()
        visited =np.zeros(len(Gr),dtype=bool)
        prev = np.zeros(len(Gr),dtype=int)-1
        print("depth_first_search recursive")
        depth_first_search_Rec(Gr,0)
        print(prev)
        printPath(prev,num_cells-1)
        
    #Choice m > n-1
    elif int(x) > num_cells-1:
        print("here is at least one path from source to destination (m > n-1)")
        Gr = Choice_2(S,walls,int(x))
        print("depth_first_search Stack")
        path3 = Depth_first_search_Stack(Gr,0)
        print(path3)
        printPath(path3,num_cells-1)
        print()
        visited =np.zeros(len(Gr),dtype=bool)
        prev = np.zeros(len(Gr),dtype=int)-1
        print("depth_first_search recursive")
        depth_first_search_Rec(Gr,0)
        print(prev)
        printPath(prev,num_cells-1)
    #Choice m = n-1   
    else:
        print("The is a unique path from source to destination (m = n -1)")
        Gr = Choice_3(S,walls,num_cells)
        print("depth_first_search Stack")
        path3 = Depth_first_search_Stack(Gr,0)
        printPath(path3,num_cells-1)
        print(path3)
        print()
        visited =np.zeros(len(Gr),dtype=bool)
        prev = np.zeros(len(Gr),dtype=int)-1
        print("depth_first_search recursive")
        depth_first_search_Rec(Gr,0)
        print(prev)
        printPath(prev,num_cells-1)
        
    elapsed_time = time.time()-start
    print("Running time for Maze construction:", round(elapsed_time),"seconds")
    
    
