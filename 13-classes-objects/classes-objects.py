class Human:
    def __init__(self, age):
        # self.age = 25
        self.age = age
        print "I'm a new object"

    def talk(self, message):
        print self.age
        print message


Brian = Human(26)
Raul = Human(21)
print "I'm Brian and I've, ", Brian.age
print "I'm Raul and I've, ", Raul.age
Brian.talk('Hello')
Raul.talk('Hello, Brian')
