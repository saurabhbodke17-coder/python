# set 
s = {}
print(type(s))

# because for set and dict you have the same bracets 
# thats why with s = {} ->dict as datatype
# to declare empty set you should declare as s = set()
# set is by default mutable 
# frozenset is immutable 

s = {1,2,3,4,1,2,3,2,1}
print(s) # --> it will return only the unique elements 

s.add(5)
print(s)
print(len(s))

# in set memory is allodcated only to the unique elements 
# methods in set

fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

# frozenset
s = frozenset((1,2,3,3,2,1,2))
print(s) # frozenset({1, 2, 3})
s.add(34) #AttributeError: 'frozenset' object has no attribute 'add'
print(s)
