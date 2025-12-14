'''

PROBLEM DESCRIPTION:

    1. Given an undirected graph
    2. You have to return TRUE if it has a cycle otherwise FALSE

THOUGHT PROCESS:

    1. Remember what the DFS does -> It continues untill finds DEAD END
    2. In DFS we skipped an iteration/recursive call if a perticular adj_ver was visited
    3. But here as we're detecting a cycle, we must check for a visited adj_ver
    4. Cause, if adj_ver is visited and it's not the parent 
       -> means that adj_ver was touched before while doing the DFS
    5. As now i'm also touching that from my current path -> it forms a cycle (UndirectedGraph)

TIME & SPACE COMPLEXITY:

    1. Time Complexity: O(V+E)
    2. Space Complexity: O(V)

NOTES:

    1. This cycly detection algorithm only works for UndirectedGraph
    2. For calculating TC & SC, i assumed graph is stored using adjacency list
       & considered only the required auxiliary space for the algorithm
    3. Assumed the graph might have multiple connected components
    4. Can be implemented with the Iterative-DFS as well -> detect(graph, source, visited)

'''



from collections import defaultdict

def detect(graph, source, parent, visited):
    visited[source] = 1

    for adj_ver in graph[source]:
        if (not(visited[adj_ver])):
            if (detect(graph, adj_ver, source, visited)):
                return True
        elif (adj_ver != parent):
            return True
    
    return False



def isCycle(graph, n):
    visited = [0]*(n+1)

    for node in range(1, n+1):
        if (not(visited[node])):
            if (detect(graph, node, -1, visited)):
                return True
    
    return False



vertices, edges = map(int, input().split())
adjacency_list = defaultdict(list)
for edge in range(edges):
    u, v = map(int, input().split())
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

print(isCycle(adjacency_list, vertices))