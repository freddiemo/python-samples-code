# encoding: utf-8
def operator(n, m):
    if n is None or m is None:
        return 0
    return n + m


l1 = [1, 2, 3, 4]
t1 = (9, 8, 7, 6)
lr = map(operator, l1, t1)
print l1
print t1
print lr


l1 = [1, 2, 3, 4]
t1 = (9, 8, 7)
lr = map(operator, l1, t1)
print l1
print t1
print lr

s1 = "Hello"
s2 = "World"
lr = map(operator, s1, s2)
print s1
print s2
print lr
