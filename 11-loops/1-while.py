age = 19
while age <= 20:
    print "You have: " + str(age)
    age = age + 1

age = 18
while age <= 20:
    if age == 19:
        age = age + 1
        continue
    print "You have: " + str(age)
    age = age + 1

age = 17
while age <= 20:
    if age == 18:
        break
    print "You have: " + str(age)
    age = age + 1
