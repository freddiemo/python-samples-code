class Human:
    def __init__(self, age):
        self.age = age

    def talk(self, message):
        print message


class Systems_engineering(Human):
    def __init__(self):
        print "Hello"

    def program(self, language):
        print "I'm going to program in", language


class Law_student(Human):
    def study_case(self, of):
        print "I've study the case ", of


Brian = Systems_engineering()
Raul = Law_student(21)
Brian.program('Python')
Raul.study_case('Brian')

Brian.talk('Hello')
Raul.talk('Hello, Brian')
