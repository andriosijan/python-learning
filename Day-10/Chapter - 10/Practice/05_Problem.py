# Write a class "Train" which has methods to book a ticket. get status ( no of seats) and get fare information of train running under indian Railways.


from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

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