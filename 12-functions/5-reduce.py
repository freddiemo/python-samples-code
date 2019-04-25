# encoding: utf-8
s = ('H', 'e', 'l', 'l', 'o', '', 'W', 'o', 'l', 'd')


def concatenate1(a, b):
    return a + b


sr = reduce(concatenate1, s)

print type(sr)
print sr

l1 = (1, 2, 3)


def sum(a, b):
    return a + b


sr = reduce(sum, l1)
print type(sr)
print sr
