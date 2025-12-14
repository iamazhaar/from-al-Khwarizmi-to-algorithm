'''

PROBLEM DESCRIPTION:

    1. Given a Directed Acyclic Graph (DAG)
    2. Print a valid topological sort order

DEFINITION OF TOPOLOGICAL SORT:

    -> Topological Sort is a linear ordering of the vertices of a DAG such that
    for every directed edge from u to v (u -> v), vertex u comes before v in the ordering

THOUGHT PROCESS:

    1. Recall what DFS does -> It continues untill finds DEAD END
    2. After reaching a DEAD END, we backtrack
    3. But, before backtracking push that DEAD END node into a Stack
    4. Keep doing it until DFS finish traversal
    5. After DFS traversal done, pop one by one from the Stack -> A Valid TopoSort Order

TIME & SPACE COMPLEXITY:

    1. Time Complexity: O(V+E)
    2. Space Complexity: O(V)

NOTES:

    1. This TopoSort algorithm only works for DAG (Gives invalid order for other Graphs)
    2. For calculating TC & SC, i assumed graph is stored using adjacency list
       & considered only the required auxiliary space for the algorithm
    3. Assumed the graph might have multiple connected components
    4. Can be implemented with the Iterative-DFS as well (Using 2 Stacks)

'''



from collections import defaultdict, deque

def recursive_dfs(graph, source, visited, stack):
    visited[source] = 1

    for adj_ver in graph[source]:
        if (not(visited[adj_ver])):
            recursive_dfs(graph, adj_ver, visited, stack)
    
    stack.append(source)



def topoSort(graph, n):
    visited = [0]*(n+1)
    stack = deque()

    for node in range(1, n+1):
        if (not(visited[node])):
            recursive_dfs(graph, node, visited, stack)
    
    while stack:
        node = stack.pop()
        print(node, end=" ")



vertices, edges = map(int, input().split())
adjacency_list = defaultdict(list)
for edge in range(edges):
    u, v = map(int, input().split())
    adjacency_list[u].append(v)

topoSort(adjacency_list, vertices)
print()