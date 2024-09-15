# Can you change the self-parameter inside a class to something else (stay "harry"). Try changing self to "slf" of "harry" and see the effects.

from random import randint

class Train:
    def __init__(harry, trainNo):
        harry.trainNo = trainNo

    def book(self, from_ , to):
        print(f"Ticket is booked in train no: {self.trainNo} from {from_} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, from_ , to):
        print(f"Ticket fare in train no: {self.trainNo} from {from_} to {to} is {randint(222,5555)}")

t = Train(1235)
t.book("Rampur", "Dehli")
t.getStatus()
t.getFare("Rampur", "Dehli")

# Nothing will happen and the output will be same.