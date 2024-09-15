marks = {
    "sijan": 100,
    "arafat":50,
    "sanjia":23,
    "Rifat":50,
    0:"harry"
}

# items method
print(marks.items()) # Returns a list of (key,value)tuples.

# keys method
print(marks.keys()) # Returns a list containing dictionary's keys.

# update method
marks.update({"sanjia":80, "Renuka":100}) # Updates the dictionary with supplied key-value pairs. It can also add new key-value
print(marks)

# get method
print(marks.get("sijan")) #Returns the value of the specified kays (and value is returned eg.100 is returned here)