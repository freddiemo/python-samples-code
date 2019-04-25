# encoding: utf-8


def decorator1(function1):
    def decoratedFunction1(*args, **kwargs):
        # print "Executed function", function1.__name___
        print "Executing function"
        function1(*args, **kwargs)
    return decoratedFunction1


def rest1(n, m):
    print n - m


# decorating
rest1(5, 3)
decorated = decorator1(rest1)(5, 3)


@decorator1
def rest2(n, m):
    print n - m


logged = False
user = "User1"


def admin(f):
    print "jslkad"

    def checking1(*args, **kwargs):
        print "jslkad"
        if logged:
            f(*args, **kwargs)
        else:
            print "You don't have permission"
    return checking1


@admin
def rest1(n, m):
    print n - m
