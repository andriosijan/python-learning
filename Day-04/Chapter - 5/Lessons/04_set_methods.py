s = {1,5,8,2,4,4,5,5,30,"Sijan"}

# add method
s.add(455) # This will add new item in set
print(s)

# remove method
s.remove(2) # Updates the set s and removes 2 from set
print(s)

# pop method
s.pop() # Removes an arbitary element from the set and return the element removed.
print(s)

# clear method
s.clear() # empties the set s.
print(s)

# union method
s = s.union({8,11,15}) # Return a new set with all items from both sets
print(s)

# intersection method
s = s.intersection({2,5,8,11}) # Return a set which contains only item in both sets
print(s)
