from app import check_stock

def test_in_stock():
    assert check_stock("Laptop", 5) == "Laptop is in stock (5 units)"

def test_out_of_stock():
    assert check_stock("Mouse", 0) == "Mouse is OUT OF STOCK"
