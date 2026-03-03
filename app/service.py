import uuid
from typing import Dict
from app.models import Customer

class CustomerNotFoundException(Exception):
    def __init__(self, id: str):
        super().__init__(f"Customer not found: {id}")
        self.id = id

class CustomerService:
    def __init__(self):
        self.customers: Dict[str, Customer] = {}

    def create_customer(self, name: str, email: str) -> Customer:
        id = str(uuid.uuid4())
        customer = Customer(id=id, name=name, email=email)
        self.customers[id] = customer
        print(f"Created customer {customer}")
        return customer

    def get_customer(self, id: str) -> Customer:
        if id in self.customers:
            print(f"Found customer with id {id}")
            return self.customers[id]
        else:
            print(f"Customer not found with id {id}")
            raise CustomerNotFoundException(id)
