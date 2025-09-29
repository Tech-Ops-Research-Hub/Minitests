#Dictionaries are data structure that store data in key-value pairs
#Dictionaries are mutable, meaning they can be changed after creation. Think of them like a real world dictionary where you look up a word (the key) to find the definition (the value).

#Key features of dictionaries:
#Key Value Pairs: Each entry has a key (e.g a sword) and a value (e.g the definition of the word)
#Unique Keys: Keys must be unique and immutable (e.g strings, numbers, or tuples)
#Mutable Values: Values can be of any data type and can be changed (e.g lists, other dictionaries, etc)
#Unordered: Dictionaries do not maintain any order for their items (prior to Python 3.7)

#Examples of creating and using dictionaries:

my_dict= {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict["name"]) # Output: Alice
my_dict["age"]=26 # Update age
my_dict["job"]="Engineer" # Add new key-value pair
print(my_dict)# Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'job': 'Engineer'}
