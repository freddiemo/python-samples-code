# encoding: utf-8
s = "Hello World"

# size
print len(s)

# match count
print s.count('o')
print s.count('D')

# match count by range
print s.count('o', 0, 3)
print s.count('W', 5)

# convert a minúsculos
print s.lower()

print s.upper()

# replace in string
print s.replace('o', 'x')
print s.replace('o', 'x', 1)
print s.replace('Hello', 'x', 1)

# split by separator
print s.split()
print s.split('o')
print s.split('d')
print s.split('o', 1)

print s.find('e')
print s.rfind('o')

t = ("H", "e", "l", "l", "o")
s = ";"
print s.join(t)
print type(s.join(t))
