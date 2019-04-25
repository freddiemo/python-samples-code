# encoding: utf-8
class Test1(object):
    def __init__(self):
        self.__privateAttribute = "I'm a private attribute"
        self.publicAttribute = "I'm a public attribute"

    def __privateMethod(self):
        print "I'm a private method"

    def publicMethod(self):
        print "I'm a public method"

    def getPrivateAttribute(self):
        return self.__privateAttribute

    def setPrivateAttribute(self, value):
        self.__privateAttribute = value


obj = Test1()
print obj.publicAttribute
obj.publicMethod()
obj.setPrivateAttribute("New value")
print obj.getPrivateAttribute()
