#What are sets?
#Sets are unordered collections of unique elements. They are mutable, meaning you can add or remove elements, but they do not allow duplicate values.
#Sets are defined using curly braces {} or the set() constructor.
#Sets are useful for membership testing, removing duplicates from a list, and performing mathematical set operations like union, intersection, and difference.

#Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

fruits = {"apple", "banana", "cherry"}
print(fruits)  # Output: {'banana', 'apple', 'cherry'}

#adding elements to a set
fruits.add("orange")
print(fruits)  # Output: {'banana', 'apple', 'cherry', 'orange'}

#removing elements from a set
#Note: If you try to remove an element that does not exist, it will raise a KeyError.
#You can use discard() to remove an element without raising an error if it doesn't exist.
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry', 'orange'}

#discarding an element
fruits.discard("banana")  # No error raised
print(fruits)  # Output: {'apple', 'cherry', 'orange'}

#set union
#what is set union?
#Set union is the operation of combining two sets to create a new set that contains all unique elements from both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set_union = set1.union(set2)
print(set_union)  # Output: {1, 2, 3, 4, 5}

#or using the | operator
set_union = set1 | set2
print(set_union)  # Output: {1, 2, 3, 4, 5}

#Set intersection
#what is set intersection?
#Set intersection is the operation of finding common elements between two sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set_intersection = set1.intersection(set2)
print(set_intersection)  # Output: {3}

#or using the & operator
set_intersection = set1 & set2
print(set_intersection)  # Output: {3}

#Set difference
#what is set difference?    
#Set difference is the operation of finding elements that are in one set but not in another.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set_difference = set1.difference(set2)
print(set_difference)  # Output: {1, 2}

#or using the - operator
set_difference = set1 - set2
print(set_difference)  # Output: {1, 2}

#Set symmetric difference
#what is set symmetric difference?
#Set symmetric difference is the operation of finding elements that are in either of the sets but not in both.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set_symmetric_difference = set1.symmetric_difference(set2)
print(set_symmetric_difference)  # Output: {1, 2, 4, 5}

#or using the ^ operator
set_symmetric_difference = set1 ^ set2
print(set_symmetric_difference)  # Output: {1, 2, 4, 5}

#Set membership testing
#what is set membership testing?    
#Set membership testing is the operation of checking if an element is present in a set.
my_set = {1, 2, 3, 4, 5}    
print(3 in my_set)  # Output: True
print(6 in my_set)  # Output: False

#Set length
#what is set length?
#Set length is the operation of finding the number of unique elements in a set.
my_set = {1, 2, 3, 4, 5}    
print(len(my_set))  # Output: 5

#Set iteration
#what is set iteration?
#Set iteration is the operation of looping through each element in a set.
#Note: Sets are unordered collections, so the order of elements may vary when iterating.
my_set = {1, 2, 3, 4, 5}
for element in my_set:
    print(element)
# Output: 1 2 3 4 5 (order may vary)
