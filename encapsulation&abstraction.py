

from abc import ABC, abstractmethod

# abstraction


class insurance(ABC):
    def visitsCovered(self, amount):
        print("Visits remaining: ", amount)

    @abstractmethod
    def therapyNeeded(self, amount):
        pass


class therapyVisits(insurance):
    def therapyNeeded(self, amount):
        print("{} visits are needed for full recovery. We will need to get more approved visits.".format(amount))


obj = therapyVisits()
obj.visitsCovered("8")
obj.therapyNeeded("12")

# encapsulation


class Patient:
    def __init__(self):
        self.name = 'John Doe'      # public
        self._coPay = '$50'     # protected

    def setPrivate(self, private):
        self.__diagnosis = private      # private

    def getPrivate(self):
        print(self.__diagnosis)


obj = Patient()
print(obj.name)
obj._coPay = '$25'
print(obj._coPay)
obj.setPrivate('Torn ACL')
obj.getPrivate()
