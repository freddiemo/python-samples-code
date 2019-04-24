l0 = [2, "tres", True, ["uno", 10]]
print l0

# get item by index
l2 = l0[1]
print l2

# get item in a nested list
l3 = l0[3][0]
print l3

# changing content by index
l0[1] = 4
print l0[1]

# slicing copy
l4 = l0[0:3]
print l4

# slicing by two index positions
l5 = l0[0:3:2]
print l5

# slicing by two index positions all list
l6 = l0[1::2]
print l6

# changing range elements
l0[0: 2] = [4, 3]
print l0

# replacing two elements with a list with one element
l0[0:2] = [4]
print l0

# get last element
l7 = l0[-1]
print l7
