##Depth -First -Search (DFS) is a traversal algorithm that explores as far as possible along each branch backtracking
##Core mechanics
##Starts at a root node (or arbitrary node in graphs)
##Marks node as visited
##Recursively ( or with explicit stack) visits an unvisited neighbor
##Continues until no unvisited neighbors that exist
##Backtracks to previous node and repeats
##Terminates when all reachable nodes are visited

#Two standard implementations
#1. Recursive DFS (simplest)
def dfs(node):
        if not node or visited(node): return
        visited[node]=True
        process(node)
        for neighbor in neighbors(node):
            dfs(neighbor)
#2.Iterative DFS (uses explicit stack)
stack = [start_node]
while stack:
    node = stack.pop ()
    if visited[node]:continue 
    visited[node]=True 
    process(node) 
    for neighbor in reversed (neighbors(node)):
        stack.append(neighbor)

##Key Properties 
# Time complexity : O(V+E)
# Space complexity: O(V)worst case (recursion stack or explicit stack)
# Explores deep first > discovers nodes far from the start quickly
# Naturally finds paths, connected components, cycles, topographical order (DAGs)
# Backtracking is inherent (stack-based)
# 
# In trees; DFS appears as pre-order, or post-order depending on when you process the node. 
# In Graphs:DFS must track visited nodes to avoid infinite loops on cycles/back edges.
# 
# DFS is the direct extension of the linked list traversal pattern. Instead of one fixed next pointer,each node
# can have multiple next pointers.          