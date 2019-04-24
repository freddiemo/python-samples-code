# encoding: utf-8
list1 = [1, "Two", 3]

# find element
search = 1
print search in list1

# get index
if search in list1:
    print list1.index(search)
else:
    print 'element is not in the list1'

print list1
# add element
list1.append("New element")
print list1

# count matches an item
print list1.count(3)

# insert in a specific index
list1.insert(2, "New")
print list1

# extend list
iterable = "String"
list1.extend(iterable)
print list1

iterable = (1, 2, 3, 4)
list1.extend(iterable)
print list1

iterable = [1, 2, 3, 4]
list1.extend(iterable)
print list1

# delete last item
list1.pop()
print list1

# delete by index
list1.pop(2)
print list1
list1.pop(3)
print list1

# reverse order
list1.reverse()
print list1
