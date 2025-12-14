'''

PROBLEM DESCRIPTION:

    1. Given an directed graph
    2. You have to return TRUE if it has a cycle otherwise FALSE

THOUGHT PROCESS:

    1. Recall the idea of UndirectedGraph(DFS-Based) cycle detection algorithm
    2. The previous algo won't work -> we need to modify (As solving for DirectedGraph)
    3. For UndirectedGraph, the core logic is if adj_ver is visited and it's not the parent -> Cycle
    4. But for DirectedGraph the core logic is if adj_ver is visited and it's visited on the same path -> Cycle
    5. Hence, we need two arrays -> visited and pathVisited

TIME & SPACE COMPLEXITY:

    1. Time Complexity: O(V+E)
    2. Space Complexity: O(V)

NOTES:

    1. This cycly detection algorithm only works for DirectedGraph
    2. For calculating TC & SC, i assumed graph is stored using adjacency list
       & considered only the required auxiliary space for the algorithm
    3. Assumed the graph might have multiple connected components
    4. Can be implemented with the Iterative-DFS as well -> detect(graph, source, visited, pathVisited)

'''



from collections import defaultdict

def detect(graph, source, visited, pathVisited):
    visited[source] = 1
    pathVisited[source] = 1

    for adj_ver in graph[source]:
        if (not(visited[adj_ver])):
            if (detect(graph, adj_ver, visited, pathVisited)):
                return True
        elif (pathVisited[adj_ver]):
            return True
    
    pathVisited[source] = 0
    return False



def isCycle(graph, n):
    visited = [0]*(n+1)
    pathVisited = [0]*(n+1)

    for node in range(1, n+1):
        if (not(visited[node])):
            if (detect(graph, node, visited, pathVisited)):
                return True
    
    return False



vertices, edges = map(int, input().split())
adjacency_list = defaultdict(list)
for edge in range(edges):
    u, v = map(int, input().split())
    adjacency_list[u].append(v)

print(isCycle(adjacency_list, vertices))