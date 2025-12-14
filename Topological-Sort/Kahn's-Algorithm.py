'''

PROBLEM DESCRIPTION:

    1. Given a Directed Graph
    2. Print a valid topological sort order if it's a DAG
    3. Print -1 if no valid topological sort order

DEFINITION OF TOPOLOGICAL SORT:

    -> Topological Sort is a linear ordering of the vertices of a DAG such that
    for every directed edge from u to v (u -> v), vertex u comes before v in the ordering

THOUGHT PROCESS:

    1. We'll use something similar to BFS (using a Stack)
    2. We initialize an indegree array storing the indegree of each node
    3. Initialize a Stack -> put the nodes that has indegree = 0
    4. Pop from Stack and print it (As indegree 0, it should appear first in linear ordering)
    5. Iterate over the adj_ver of that poped node and decrease the indegree of adj_ver by 1
    6. After decrementing, immediately check if indegree[adj_ver] = 0 -> If so, push into the Stack
    6. Continue until the Stack becomes empty

TIME & SPACE COMPLEXITY:

    1. Time Complexity: O(V+E)
    2. Space Complexity: O(V)

NOTES:

    1. This TopoSort algorithm only works for DAG (Gives -1 for other Graphs)
    2. For calculating TC & SC, i assumed graph is stored using adjacency list
       & considered only the required auxiliary space for the algorithm
    3. Assumed the graph might have multiple connected components

'''



from collections import defaultdict, deque

def topoSort(graph, n):
    indegree = [0]*(n+1)
    for node in range(1, n+1):
        for adj_ver in graph[node]:
            indegree[adj_ver] += 1
    
    q = deque()
    for node in range(1, n+1):
        if (indegree[node] == 0):
            q.append(node)
        
    nodeCount = 0
    nodeOrder = []
    while q:
        node = q.popleft()
        nodeCount += 1
        nodeOrder.append(node)
        for adj_ver in graph[node]:
            indegree[adj_ver] -= 1
            if (indegree[adj_ver] == 0):
                q.append(adj_ver)

    if (nodeCount == n):
        print(*nodeOrder)
    else:
        print(-1)



vertices, edges = map(int, input().split())
adjacency_list = defaultdict(list)
for edge in range(edges):
    u, v = map(int, input().split())
    adjacency_list[u].append(v)

topoSort(adjacency_list, vertices)