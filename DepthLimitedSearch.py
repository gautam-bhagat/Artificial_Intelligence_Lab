#DLS Algorithm
graph ={0: [(4, 1)], 1: [(3, 1), (4, 1)], 2: [(3, 1), (5, 1), (5, 1)], 3: [(1, 1), (2, 1), (4, 1)], 4: [(3, 1), (0, 1), (1, 1)], 5: [(2, 1), (2, 1)]}

def DLS(start , goal , path , level , maxD):
    flag =1
    print("Goal node testing for :",start)
    path.append(start)
    if start==goal:
        return path
    flag=0
    if level == maxD:
        return False
    print("Expanding current Node:",start)
    for child,weigt in graph[start]:
        if DLS(child,goal,path,level+1,maxD):
            return path
        path.pop()
    return False

    
    

start = int(input("Enter a starting Node:"))
goal = int(input("Enter the Goal Node:"))
maxD = int(input("Enter the limit for search:"))
print()
path=[]
res = DLS(start , goal ,path , 0, maxD)
if(res):
    print("The path to the goal node is :")
    print(path)
else:
    print("No path is available to the given goal node.")


#Depth-limited search is found to terminate under these two clauses:

#When the goal node is found to exist.
#When there is no solution within the given depth limit domain.