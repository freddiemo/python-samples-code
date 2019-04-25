# simple function with arguments
def my_function(num1, num2):
    print num1 + num2


my_function(3, 4)


# arguments initialized
def my_function2(num1=0, num2=0):
    print num1 + num2


my_function2()
my_function2(3)


# with string arguments
def my_function3(string, v=2):
    print string * v


my_function3('Python')
my_function3('Python', 5)


# with tuple arguments
def my_function4(string, v=2, *somethingMore):
    print string * v
    for s in somethingMore:
            print s


my_function4('Python', 5, 'Hello', 'Bye', 'N', 'strings')


# with dictionary arguments
def my_function5(string, v=2, **somethingMore):
    print string * v
    print somethingMore['stringExtra']
    print somethingMore['stringInAddition']


my_function5('Python', 5, stringExtra='Hello', stringInAddition='Bye')


# returning value
def my_function6(num1, num2):
    return num1 + num2


sum_result = my_function6(3, 4)
print sum_result
