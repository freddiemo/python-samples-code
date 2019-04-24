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
    def __init__(self, school):
        print 'Graduate in law graduated from: ', school

    def study_case(self, of):
        print "I've study the case ", of


class studious(Law_student, Systems_engineering):
    pass


josep = studious('IUPSM')
josep.talk("Hello, I'm of multiple inheritance")
josep.program('C++')
josep.study_case('Maria')
