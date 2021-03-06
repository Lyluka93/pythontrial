import unittest


class TestTicketMachine(unittest.TestCase):

    def test_identity(self):
        # Given:
        from greeting.ticket_machine import TicketMachine
        # When:
        machine = TicketMachine()
        # Then:
        assert machine is not None

    def test_ticket_machine_gives_you_ticket(self):
        # Given
        from greeting.ticket_machine import TicketMachine
        # When
        machine = TicketMachine()
        # Then:
        sorszam = machine.getNewTicket()
        assert sorszam is not None

    def test_ticket_machine_does_not_give_the_same_twice(self):
        # Given
        from greeting.ticket_machine import TicketMachine
        # When
        machine = TicketMachine()
        one = machine.getNewTicket()
        other = machine.getNewTicket()
        # Then:
        self.assertNotEqual(one, other, "Tickets should be unique")

    def test_customer_identity(self):
        # Given
        from greeting.ticket_machine import Customer
        # When
        sarah = Customer()
        # Then:
        assert sarah is not None

    def test_customer_gets_a_ticket(self):
        # Given
        from greeting.ticket_machine import TicketMachine
        from greeting.ticket_machine import Customer
        # When
        machine = TicketMachine()
        one = machine.getNewTicket()
        sarah = Customer()
        sarahticket = sarah.receiveTicket(machine)
        # Then:
        self.assertNotEqual(one, sarahticket, "Customer should get another ticket")

