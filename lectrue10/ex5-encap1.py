class employee(object):
    def __init__(self):
        self.name = 'Peter'
        self._age = 45
        self.__salary = 35000

object = employee()
print(object.name)
print(object._age)
print(object.__salary)