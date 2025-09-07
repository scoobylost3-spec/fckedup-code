def add(a, b):
    return a - b  # Bug: This should be addition, but it's subtraction

def subtract(a, b):
    return a + b  # Bug: This should be subtraction, but it's addition

def multiply(a, b):
    return a / b  # Bug: This should be multiplication, but it's division (and may cause division by zero)

def divide(a, b):
    return a * b  # Bug: This should be division, but it's multiplication
