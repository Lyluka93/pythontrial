class TicketMachine:
    def __init__(self):
        self.i = 0

    def getNewTicket(self):
        self.i += 1
        return self.i

class Customer:
    def __init__(self):
        self.ticket = None

    def receiveTicket(self, machine:TicketMachine):
        self.ticket = machine.getNewTicket()
        return self.ticket 