#Dictionaries (in python) or Objects (in JavaScript) are data structures that store data in key-value pairs allowing
#you to associate data with unique key identifiers. They are mutable, meaning they can be changed after creation. Think of them like a real world dictionary where you look up a word (the key) to find the definition (the value).

#Dictionaries in Python. 
#A dictionary in python is a collection of key-value pairs where each key is unique and maps to a value. Keys are typically strings or numbers, and values can be any data type (numbers, strings, lists, other dictionaries etc.)

my_dict= {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict["name"]) # Output: Alice
my_dict["age"]=30 # Update age
my_dict["city"]="New York" # Add new key-value pair
print(my_dict)# Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

#Key Features of Dictionaries:
#Key Value Pairs: Each entry has a key (e.g a sword) and a value (e.g the definition of the word)
#Unique Keys: Keys must be unique and immutable (e.g strings, numbers, or tuples
#Useful for organizing and accessing data quickly using keys instead of numeric indices
#Mutable Values: Values can be of any data type and can be changed (e.g lists, other dictionaries, etc)
#Unordered: Dictionaries do not maintain any order for their items (prior to Python 3.7)