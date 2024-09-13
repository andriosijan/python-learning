ls = ["Apple", "Orange", 5, 3435.45, False, "Akash", "Rohan"]

print(ls)

# append method
ls.append("Harry") # This will add new data at the end
print(ls)

# sort method
numbers = [1,4,2,5,77,5656,78]
numbers.sort() # This will sort the numbers small to large
print(numbers)

# reverse method
ls.reverse() # This will reverse the whole list
print(ls)

# insert method
ls.insert(0,"Papaya") # This will add new data in any index you want
print(ls)

# pop method
value = ls.pop(2) # By default this will remove an element from at the end . but if you provide index number of the element you what to remove then this will remove it. and this method also return the removed element as a value
print(ls)
print(value)

# remove method
ls.remove(False) # This one is also like pop method . this method remove the item you want. this method does not take the index but take the item to remove it from the list.
print(ls)