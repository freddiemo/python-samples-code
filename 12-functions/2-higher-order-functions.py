# encoding: utf-8
def test1(f):
    return f()


def toSend():
    return 2 + 2


print test1(toSend)


def selection(operation):
    def sum(n, m):
        return n + m

    def multiplication(n, m):
        return n * m
    if operation == "sum":
        return sum
    elif operation == "multi":
        return multiplication


fSaved = selection("sum")
print fSaved(3, 4)

fSaved = selection("multi")
print fSaved(12, 12)
