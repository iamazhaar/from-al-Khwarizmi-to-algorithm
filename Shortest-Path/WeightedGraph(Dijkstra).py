'''

PROBLEM DESCRIPTION:

    1. Given a directed/undirected and weighted graph
    2. Find the shortest path from a source vertex to a given node
    3. If no shortest path exists, print -1

THOUGHT PROCESS:

    1. Dijkstra's Algorithm is similar to BFS but instead of
       -> visited array we use distance array
       -> Queue we use Priority Queue (Min-Heap)
    2. Mark distance[source]=0 and push it into the PQ as (distance, node)
    3. While PQ isn't empty
       -> pop the topmost one from the PQ
       -> go through each of it's adjacent node
       -> If (previousDist+adj_node weight < distance[adj_node]) update distance[adj_node] and push into the PQ
    4. After loop ends, we get the shortest distance of each node from the source node

TIME & SPACE COMPLEXITY:

    1. Time Complexity: O(E*logV)
    2. Space Complexity: O(V)

NOTES:

    1. For calculating TC & SC, i assumed graph is stored using adjacency list
       & considered only the required auxiliary space for the algorithm
    2. The algorithm won't work if the graph has any negative weight

'''



from collections import defaultdict
import heapq
 
def dijkstra(graph, source, distance, parent):
    distance[source] = 0
    heap = []
    heapq.heappush(heap, (0, source))
 
    while heap:
        previous_distance, node = heapq.heappop(heap)
        for tup in graph[node]:
            adj_node, wt = tup
            if (previous_distance+wt < distance[adj_node]):
                distance[adj_node] = previous_distance+wt
                parent[adj_node] = node
                heapq.heappush(heap, (distance[adj_node], adj_node))
 
 
 
def find_shortest_path(graph, source, destination, n):
    distance = [float("+inf")]*(n+1)
    parent = [-1]*(n+1)
 
    dijkstra(graph, source, distance, parent)
 
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



N, M, S, D = map(int, input().split())
adjacency_list = defaultdict(list)
for i in range(M):
    u, v, w = map(int, input().split())
    adjacency_list[u].append((v, w))

find_shortest_path(adjacency_list, S, D, N)