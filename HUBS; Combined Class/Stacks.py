#Stacks 

# A stack is a linear data structure that follows the Last In First Out (LIFO) principle. This means that last element added to the stack is the first one to be removed. Stacks are commonly used in programming for tasks such as function call management, expression evaluation, and backtracking algorithms.

#Scenario: Imagine a stack of plates in a cafeteria; You place a new plate on top(adding), and when you need a plate, you take the top most one (removing).
# You can't easily grab a plate from the middle or bottom without disturbing the stack.

#Core Operations of a Stack:
# Push: Add an element to the top of the stack.
     #-Time complexity: O(1) (constant time, assuming no resizing in array-based stacks)
     #Example: Adding a new plate to the top of the stack. 
# Pop: Remove and return the top element from the stack.
     #- Time complexity: O(1)
     #Example: Taking the top plate off the stack.
#Peek (or top): Return the top element without removing it.
     #- Time complexity: O(1)
     #Example: Checking which plate is on top without removing it.
# IsEmpty: Check if the stack is empty.     
     #- Time complexity: O(1)
     #Example: Checking if there are any plates in the stack.
# Size: Return the number of elements in the stack.
     #- Time complexity: O(1)
     #Example: Getting the count of plates in the stack.
#IsFull: Check if the stack has reached its maximum capacity (relevant for fixed-size stacks).
     #- Time complexity: O(1)    
     #Example: Checking if the stack is full.
     
     
     #Implementing a Stack from Scratch using Python
     # Stacks can be implemented using either arrays or linked lists. 
     
     #Array-based Stack Implementation. An array - based stack uses a fixed or dynamically resizing array to store elements. The "top" of the stack is tracked using an index.
     
     #Pseudocode for Array-based Stack:
     
