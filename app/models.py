from pydantic import BaseModel

class Customer(BaseModel):
    id: str
    name: str
    email: str

class CreateCustomerRequest(BaseModel):
    name: str
    email: str
