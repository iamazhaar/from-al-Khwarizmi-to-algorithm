'''

PROBLEM DESCRIPTION:

    1. Given a directed/undirected and unweighted graph
    2. Find the shortest path from a source vertex to a given node
    3. If no shortest path exists, print -1

THOUGHT PROCESS:

    1. Recall BFS traverse level-wise -> Hence, it can give us the shortest path of a node
    2. But, instead of a visited array I will keep
       -> Distance Array: Denotes the shortest distance of a visited node
       -> Parent Array: Denotes the parent of a particular vertex
    3. I will call the BFS set the distance[source]=0 & push it into the Q
    4. BFS traversal will happen and the distance and parrent array will get updated
    5. Finally get the shortest distance from distance[destination] and construct path from the parent array

TIME & SPACE COMPLEXITY:

    1. Time Complexity: O(V+E)
    2. Space Complexity: O(V)

NOTES:

    1. For calculating TC & SC, i assumed graph is stored using adjacency list
       & considered only the required auxiliary space for the algorithm
    2. The algorithm won't work if the graph is WEIGHTED

'''



from collections import defaultdict, deque

def bfs(graph, source, distance, parent):
    distance[source] = 0
    parent[source] = -1
    q = deque()
    q.append(source)

    while q:
        node = q.popleft()
        for adj_ver in graph[node]:
            if (distance[adj_ver] == float("+inf")):
                distance[adj_ver] = distance[node] + 1
                parent[adj_ver] = node
                q.append(adj_ver)



def find_shortest_path(graph, source, destination, n):
    distance = [float("+inf")]*(n+1)
    parent = [-1]*(n+1)

    bfs(graph, source, distance, parent)

    if (distance[destination] == float("+inf")):
        print(-1)
        return
    
    path = []
    currentNode = destination
    path.append(currentNode)
    while (parent[currentNode] != -1):
        path.append(parent[currentNode])
        currentNode = parent[currentNode]

    print(distance[destination])
    print(*reversed(path))



vertices, edges, source, destination = map(int, input().split())
adjacency_list = defaultdict(list)
for edge in range(edges):
    u, v = map(int, input().split())
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

find_shortest_path(adjacency_list, source, destination, vertices)