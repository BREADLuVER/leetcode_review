import collections
from datetime import date

class Ticketsystem:
    def __init__(self):
        self.ticket_id = 0
        self.tickets = collections.defaultdict(list)
    
    def create_ticket(self, customer_name):
        self.ticket_id +=1
        d = date.today()
        ticket_info = {'ticket_id': self.ticket_id, "customer_name": customer_name, "date": d}

        self.tickets[customer_name].append(ticket_info)
        print(f"tickert created for customer {customer_name}. Ticket ID: {self.ticket_id}")
    
    def get_ticket(self, customer_name, ticket_id):
        if customer_name in self.tickets:
            for t in self.tickets[customer_name]:
                if t["ticket_id"] == ticket_id:
                    d = t["date"]
                    print(f"This is the tickert created for customer {customer_name}. date: {d}")
                    return t
        else:
            return None

    def resolve_ticket(self, customer_name, ticket_id):
        if customer_name in self.tickets:
            for t in self.tickets[customer_name]:
                if t["ticket_id"] == ticket_id:
                    resolved_ticket = t
                    self.tickets[customer_name].remove(t)
                    print(f"This is the tickert removed for customer {customer_name}.")
                    return resolved_ticket
        else:
            return None

ticket_system = Ticketsystem()
ticket_system.create_ticket("John Doe")
ticket_system.create_ticket("Alice Smith")

# Retrieve a specific ticket
ticket = ticket_system.get_ticket("John Doe", 1)
r = ticket_system.resolve_ticket("John Doe", 1)
print(ticket if ticket else "Ticket not found")

