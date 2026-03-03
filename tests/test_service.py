from app.service import CustomerService, CustomerNotFoundException

def test_create_customer():
    service = CustomerService()
    customer = service.create_customer("Alice", "alice@example.com")

    assert customer.name == "Alice"
    assert customer.email == "alice@example.com"
    assert customer.id in service.customers

def test_get_customer_success():
    service = CustomerService()
    created = service.create_customer("Bob", "bob@example.com")

    fetched = service.get_customer(created.id)
    assert fetched == created

def test_get_customer_not_found():
    service = CustomerService()

    try:
        service.get_customer("unknown-id")
        assert False, "Expected exception"
    except CustomerNotFoundException:
        pass
