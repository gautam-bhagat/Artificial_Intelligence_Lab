# BFS Algorithm
tosearch = input("Which node is to be searched? :")
G={ 'A':['B','C'] , 'B':['D','E'] , 'D':['H','I'] , 'E':[] , 'C':['F','G'] ,'F':[] , 'G':[],'H':[],'I':[]}
visited =[]
queue =[]

def bfs(node,G,visited,queue,tosearch):
    flag=0
    visited.append(node)
    queue.append(node)
    while( queue ) :
        n=queue.pop(0)
        print(n,end='->')
        if ( n==tosearch ):
            flag=1
            break
        for neighbour in G[n]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    if(flag):
        print("\nElement found")
    else:
        print("Search unsuccessfull")
    
print("The path is:")
bfs('A',G,visited,queue,tosearch)

"""In this algorithm, we use a queue to keep track of the vertices to be visited. 
We start by choosing a starting vertex, marking it as visited, and adding it to the queue. 
Then, while the queue is not empty, we dequeue a vertex from the queue, process it (e.g., print its value), 
and enqueue all its adjacent vertices that have not been visited yet, marking them as visited."""