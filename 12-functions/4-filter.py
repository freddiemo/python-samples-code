# encoding: utf-8
def filter1(elem):
    return (elem > 0)


l1 = [1, -3, 2, -7, -8, -9, 10]
lr = filter(filter1, l1)
print l1
print lr


def filter2(elem):
    return (elem == 'l')


s = "Hello world"
print s
lr = filter(filter2, s)
print type(lr)
print lr
