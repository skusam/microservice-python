from fastapi import FastAPI, HTTPException
from app.models import Customer, CreateCustomerRequest
from app.service import CustomerService, CustomerNotFoundException

app = FastAPI()
service = CustomerService()

@app.post("/customers", response_model=Customer)
def create_customer(req: CreateCustomerRequest):
    return service.create_customer(req.name, req.email)

@app.get("/customers/{id}", response_model=Customer)
def get_customer(id: str):
    try:
        return service.get_customer(id)
    except CustomerNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
