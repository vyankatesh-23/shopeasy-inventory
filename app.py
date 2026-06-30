def check_stock(item, quantity):
    if quantity > 0:
        return f"{item} is in stock ({quantity} units)"
    else:
        return f"{item} is OUT OF STOCK"

if __name__ == "__main__":
    print(check_stock("Laptop", 5))
    print(check_stock("Mouse", 0))
