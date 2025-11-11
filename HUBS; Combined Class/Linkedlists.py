## Traversal = moving from one node to the next in the linked list. 

## Simple meaning; Start at head > Follow .next pointers > Visit each node one by one

#In code (example)
temp = self.head
while temp:
    print(temp.data)
    temp = temp.next

#Traverses entire list, printing each value.

#Purpose in deletion
   #To find the node before the one to delete
   #Walk pos-1 steps > reach predecessor > SKip target

# Traversal=walking the chain




