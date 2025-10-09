my_set = {1, 2, 3}
elements_to_add = [4, 5, 6, 7, 8, 9]
my_set.update(elements_to_add)  # Adding multiple elements
print(my_set) 
print(len(my_set))

#Alternatives for accessing Elements in a se. While you cannot access set elements by index, you can; 
#i) Iterate over a set; Use loop to access elements

#my_set = {1, 2, 3, 4, 5}
#for item in my_set:
#    print(item)

#ii) Convert to a list for indexing. If you need index-based access, convert the set to alist. Note that the order of elements in the resulting list is not guaranteed unless you sort it. 

# my_set= {1,6,12,18,24}
# my_list = list (my_set)
# print(my_list[0],my_list[1],my_list[2],my_list[3],my_list[4])