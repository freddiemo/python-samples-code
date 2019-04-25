# encoding: utf-8
# function with map() and filter()


def sum1(n, m):
    if n is None or m is None:
        return 0
    return n + m


# function with filter()
def filter1(n):
    return (n == 'o')


li = [1, -2, 1, -4]
lo = [5, 3, 6, 7]
s = "Hello world"

print map(sum1, li, lo)
print filter(filter1, s)
print reduce(sum1, lo)


print map(lambda n, m: n + m, li, lo)
print filter(lambda n: n == 'o', s)
print reduce(lambda n, m: n + m, lo)

sum2 = lambda n, m: n + m
print map(sum2, li, lo)
print filter(lambda n: n == 'o', s)
print reduce(sum2, lo)

print sum2(3, 4)
