# Check that tuple data type cannot be changed in python.
a = ("hello",23,654,343)
a[0] = 454 #TypeError: 'tuple' object does not support item assignment