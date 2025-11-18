#Traversal is the process of systematically visiting each node (or elements) in a data structure exactly once (or as required) to access, process, or search its data. 

##Common types and definitions 

#Tree Traversal (most frequent context)
##In-order: left > root > right
##Pre-order: root > left > right
##Post-order: left > right > root
##level-order (breadth-first); Visit nodes level by level using a queue

#Graph Traversal
##Depth-First-Search(DFS); Explores as far as possible along each branch before backtracking (uses stack or recursion)
##Breadth-First Search (BFS); Explores level by level (uses queues)

##Array/Linear structure traversal: Simply iterating from index 0 to n-1(or reverse)

##Noted: Traversal defines how you move through the structure; the choice affects time complexity, memory usage, and the output order.No single "best" traversal exists - selection depends on 
#required operation (search,copy,delete,print etc)

def print_list(self):
    temp = self.head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

##Core elements of the code, mapped directly to fundamental linked list concepts
#1.Node structure assumptions; Each node has at least two attributes. 
  #data - store the value
  #next - reference to the next node (or None at all)

#2.Head reference; self.head - entry point to the entire list;traversal always starts here
#3.Temporary pointer (temp); temp = self.head; moving pointer that walks the list without losing the head reference
#4.Loop condition; while temp; In python, None is falsy. Loop runs as long as current node exists.
#5.Accessing node data; temp.data - direct attribute access of current node's value.
#6.Moving to the next node: temp=temp.next - core traversal step; advances one node per iteration
#7.Termination detection; When temp becomes None, loop ends - natural end of a singly linked list
#8.Iterative traversal pattern; Classic O(n) time, O(1) extra space linear traversal of a singly linked list.