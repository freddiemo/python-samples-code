# encoding: utf-8
age = 18
m_age = 18

if age >= m_age:
    print "You're of age"
    if True:
        print "this is executed as long as he is of age"
else:
    print "You're not of age"

age = 18
if age >= m_age:
    print "You're of age"
    if False:
        print "this is executed as long as he is of age"
else:
    print "Anything"

print "This is always executed"
