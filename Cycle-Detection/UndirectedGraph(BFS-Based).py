'''

PROBLEM DESCRIPTION:

    1. Given an undirected graph
    2. You have to return TRUE if it has a cycle otherwise FALSE

THOUGHT PROCESS:

    1. Remember what the BFS does -> It traverses level-wise
    2. In BFS we skipped an iteration if a perticular adj_ver was visited
    3. But here as we're detecting a cycle, we must check for a visited adj_ver
    4. Cause, if adj_ver is visited and it's not the parent 
       -> means that adj_ver was touched through some other path while doing the BFS
    5. As now i'm also touching that from my current path -> it forms a cycle (UndirectedGraph)

TIME & SPACE COMPLEXITY:

    1. Time Complexity: O(V+E)
    2. Space Complexity: O(V)

NOTES:

    1. This cycly detection algorithm only works for UndirectedGraph
    2. For calculating TC & SC, i assumed graph is stored using adjacency list
       & considered only the required auxiliary space for the algorithm
    3. Assumed the graph might have multiple connected components

'''



from collections import defaultdict, deque

def detect(graph, source, visited):
    visited[source] = 1
    q = deque()
    q.append((source, -1))

    while q:
        node, parent = q.popleft()
        for adj_ver in graph[node]:
            if (not(visited[adj_ver])):
                visited[adj_ver] = 1
                q.append((adj_ver, node))
            elif (adj_ver != parent):
                return True
    
    return False
 


def isCycle(graph, n):
    visited = [0]*(n+1)

    for node in range(1, n+1):
        if (not(visited[node])):
            if (detect(graph, node, visited)):
                return True
    
    return False



vertices, edges = map(int, input().split())
adjacency_list = defaultdict(list)
for edge in range(edges):
    u, v = map(int, input().split())
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

print(isCycle(adjacency_list, vertices))