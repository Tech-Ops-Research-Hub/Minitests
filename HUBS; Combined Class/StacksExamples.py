class StackUsingList:
    def __init__(self):
        self.stack = []  # Initialize empty list

    def push(self, item):
        self.stack.append(item)  # O(1) amortized

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack.pop()  # O(1)

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[-1]  # O(1)

    def is_empty(self):
        return len(self.stack) == 0  # O(1)

    def size(self):
        return len(self.stack)  # O(1)

# ...existing code...
if __name__ == "__main__":
    s = StackUsingList()  # Creates a new empty set
    s.push(1)  # Adds 1 to the stack: [1]
    s.push(2)  # Adds 2 to the stack: [1 , 2]
    s.push(3)  # Adds 3 to the stack: [1 , 2 , 3]
    print(f"Top element: {s.peek()}")  # Output: Top element: 3
    print(f"Popped: {s.pop()}")  # Output: Popped: 3 {Removes and prints 3; stack becomes [1 , 2]}
    print(f"Size: {s.size()}")  # Output: Size: 2
    print(f"Is empty? {s.is_empty()}")  # Output: Is empty? False
# ...existing code...


# Visualizing the Stack's Behavior 
#Imagine the stack as vertical pile.
#Start: [] (empty)
#After push (1): [1] (1 is at the top)
#After push (2): [1, 2] (2 is at the top)
#After push (3): [1, 2, 3] (3 is at the top)
#After peek (): [1, 2,3] (no change, just looks at 3)
#After pop (): [1 , 2 ] (3 is removed, 2 is now at the top)

#The list's end (right side) represents the top of the stack which is why append and pop (without index) are used. 