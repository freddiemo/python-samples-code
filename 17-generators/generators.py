# encoding: utf-8
l1 = [1, 2, 3, -1, 4]
s = ["H", "E", "L", "L", "O"]
l2 = (c * num for c in s
        for num in l1
            if num > 0)
print l1
print s
print l2.next()
print l2.next()
for letter in l2:
    print letter


def factorial(n):
    i = 1
    while n > 1:
        i = n * i
        yield i
        n -= 1


for e in factorial(5):
    print e
