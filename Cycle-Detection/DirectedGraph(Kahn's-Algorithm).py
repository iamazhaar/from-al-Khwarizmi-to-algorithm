'''

PROBLEM DESCRIPTION:

    1. Given an directed graph
    2. You have to return TRUE if it has a cycle otherwise FALSE

THOUGHT PROCESS:

    1. Recall the idea of Topological-Sort -> Kahn's Algorithm
    2. Topological Sort is only possible for DAG
    3. Hence, if I am given a directed graph, still there's is no valid topo sort order
       -> means, the given directed graph is cyclic
    4. So, all i've to check whether there's a valid topo sort order
    5. I can easily do that by just using a count variable within the Kahn's Algorithm

TIME & SPACE COMPLEXITY:

    1. Time Complexity: O(V+E)
    2. Space Complexity: O(V)

NOTES:

    1. This cycly detection algorithm only works for DirectedGraph
    2. For calculating TC & SC, i assumed graph is stored using adjacency list
       & considered only the required auxiliary space for the algorithm
    3. Assumed the graph might have multiple connected components

'''



from collections import defaultdict, deque

def isCycle(graph, n):
    indegree = [0]*(n+1)
    for node in range(1, n+1):
        for adj_ver in graph[node]:
            indegree[adj_ver] += 1
    
    q = deque()
    for node in range(1, n+1):
        if (indegree[node] == 0):
            q.append(node)
        
    nodeCount = 0
    while q:
        node = q.popleft()
        nodeCount += 1
        for adj_ver in graph[node]:
            indegree[adj_ver] -= 1
            if (indegree[adj_ver] == 0):
                q.append(adj_ver)

    if (nodeCount == n):
        return False
    else:
        return True



vertices, edges = map(int, input().split())
adjacency_list = defaultdict(list)
for edge in range(edges):
    u, v = map(int, input().split())
    adjacency_list[u].append(v)

print(isCycle(adjacency_list, vertices))