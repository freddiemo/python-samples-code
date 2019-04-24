l = [2, "tres", True, ["uno", 10]]
print l

# get item by index
l2 = l[1]
print l2

# get item in a nested list
l3 = l[3][0]
print l3

# changing content by index
l[1] = 4
print l[1]

# slicing copy
l4 = l[0:3]
print l4

# slicing by two index positions
l5 = l[0:3:2]
print l5

# slicing by two index positions all list
l6 = l[1::2]
print l6

# changing range elements
l[0:2] = [4,3]
print l

# replacing two elements with a list with one element
l[0:2] = [4]
print l

# get last element
l7 = l[-1]
print l7







