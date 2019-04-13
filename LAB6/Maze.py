#Author: Michael Gonzalez
#Course: CS 2302 Data Structures
#Lab 6
#TA: Anindita Nath & Eduuardo Lara
#Purpose:the purpose of this lab is to modify the code given to create a maze.
#Your maze should contain a collection of cells separated by walls in such a way 
#that there is exactly one simple path (that is, a path that does not
#visit any cell more than once) separating any two cells.
# Last modified April,12 2019

import matplotlib.pyplot as plt
import numpy as np
import random
import time 
import dp

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
###################################################
#                       LAB START
def CountSets(S):
    num_sets = 0
    for i in range(len(S)):
        if S[i]<0:
            num_sets += 1
        dp.find_c(S,i)
    return num_sets

plt.close("all") 
maze_rows = 10
maze_cols = 15
num_cells = maze_rows*maze_cols

walls = wall_list(maze_rows,maze_cols)

draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 

start = time.time()

S = dp.DisjointSetForest(num_cells)
dp.draw_dsf(S)
           
while CountSets(S) > 1:
    d = random.randint(0,len(walls)-1)
    print('removing wall ',walls[d])
    if dp.find(S,walls[d][0]) != dp.find(S,walls[d][1]):    
        dp.union(S,walls[d][0],walls[d][1])
#        dp.union_by_size(S,walls[d][0],walls[d][1])
        walls.pop(d)
    
dp.draw_dsf(S)
draw_maze(walls,maze_rows,maze_cols) 
elapsed_time = time.time()-start
print("Running time for Maze construction:", round(elapsed_time),"seconds")
