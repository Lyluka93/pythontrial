class TicketMachine:
    def __init__(self):
        self.i = 0

    def getNewTicket(self):
        self.i += 1
        return self.i