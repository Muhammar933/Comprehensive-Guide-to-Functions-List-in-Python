#Define Function for basic arthematic operations

def add(x , y , z):
    return x + y + z
def Sub(x ,y ,z):
    return x - y - z
def Mul(x , y , z):
    return x * y * z
def Div(x ,y ,z):
    if z != 0:
        return x / y / z
    else:
        return "Error: Division by Zero"

#Test the function
num1 = 15
num2 = 10
num3 = 5

print("Addition Result: ", add(num1, num2, num3))
print("Subtraction Result: ", Sub(num1, num2, num3))
print("Multiplication Result: ", Mul(num1, num2, num3))
print("Division Result: ", Div(num1, num2, num3))