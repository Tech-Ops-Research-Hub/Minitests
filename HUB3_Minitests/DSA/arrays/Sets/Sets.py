# a set is a data structure that represents a collection of unique elements.
# Sets are unordered, meaning the elements do not have a specific order and cannot be accessed by index.
# Sets are mutable, allowing you to add or remove elements after creation.


# Creating a set in Python
my_set = {1, 2, 3}
my_set.add(5)  # Adding an element {1,2,3,5}
print (5 in my_set)
other_set = {3,4,5}
print(my_set | other_set) # Union
print (my_set & other_set) # Intersection