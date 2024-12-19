def function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero error"

result = function(10, 0)
print(result) # Output: Division by zero error