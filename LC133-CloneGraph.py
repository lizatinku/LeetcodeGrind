"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# My plan
# we want to create a deep copy of the graph
# we initialize an empty dictionary
# for an edge case: if the input node is none, we return none
# Recursively traverse the graph using DFS.
# If a node is already cloned, we return the cloned node.
# if not:
#   Create a copy of the node.
#   Add the new copy to the hashmap.
#   Recurse through the neighbors and add the cloned neighbors to the copy.

# Concepts
# 1) Deep Copy: A deep copy creates a new object that is a complete and independent replica of the original object, including all its nested objects or references.
# 2) DFS: Starting from the given node, the DFS function visits each connected node recursively.This ensures all nodes and their neighbors are explored and cloned systematically
# 3) A hashmap is used to maintain a one-to-one mapping between nodes in the original graph and their corresponding clones.


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy

        return dfs(node) if node else None
