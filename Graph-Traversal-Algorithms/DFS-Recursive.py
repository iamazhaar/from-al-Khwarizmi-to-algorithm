'''

PROBLEM DESCRIPTION:

    1. You are given an undirected graph
    2. You have to print a valid DFS traversal order starting from a source

THOUGHT PROCESS:

    1. Similar to iterative DFS (See DFS-Iterative.py)
    2. But, we're not initializing a Stack rather we're using the call Stack (As it's recursive)

TIME & SPACE COMPLEXITY:

    1. Time Complexity: O(V+E)
    2. Space Complexity: O(V)

NOTES:

    1. DFS works for both directed & undirected graph
    2. There can be multiple valid DFS traversal order
    3. For calculating TC & SC, i assumed graph is stored using adjacency list
       & considered only the required auxiliary space for the algorithm

'''



from collections import defaultdict

def recursive_dfs(graph, source, visited):
    print(source, end=" ")

    for adj_ver in graph[source]:
        if (not(visited[adj_ver])):
            visited[adj_ver] = 1
            recursive_dfs(graph, adj_ver, visited)



def traversal(graph, n):
    visited = [0]*(n+1)

    for node in range(1, n+1):
        if (not(visited[node])):
            visited[node] = 1
            recursive_dfs(graph, node, visited)



vertices, edges = map(int, input().split())
adjacency_list = defaultdict(list)
for edge in range(edges):
    u, v = map(int, input().split())
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

traversal(adjacency_list, vertices)
print()