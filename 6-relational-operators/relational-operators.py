v = 4
c = 5
# equal comparison
r = c == v
print r

v = 5
r = c == v
print r

# not
v = 4
r = c != v
print r

# smaller than
c = 3
r = c < v
print r

# greater than
r = c > v
print r

# greater than or equal
c = 4
r = c >= v
print r

# less than or equal to
c = 5
r = c <= v
print r

# strings comparison by bytes
v = 'Hello'
c = 'Bye'
r = c == v
print r
r = c != v
print r

# comparison by bytes
c = 'xwz'
r = c >= v
print r

v = ['Hello', 3, 4]
c = ['Hello', 5]
r = c != v
print r
