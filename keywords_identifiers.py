# Python Keywords And Identifiers

# True/False
print("True/False Example : ")
print(5 == 5)
print(5 > 5)

# None
print("\nNone Example")
print(None == 0)
print(None == [])
print(None == False)
print(None == True)
print(None == None)

# void/None function
print("\nvoid/None function")
def void_function():
    a=10; b=20
    print(f"sum : {a+b}")

print(void_function())

# and, or, not
print("\nand, or, not")
print(True and True)
print(True and False)
print(not False)

# try...raise...catch...finally
print("\ntry...raise...catch...finally")
try:
    x=9
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Division cannot be performed ")
finally:
    print("Execution Successfully")

# Global
print("\nGlobal")
global_var = 10
def read_func():
    print(global_var)

def write_func():
    global global_var
    global_var = 20

def rewrite_func():
    global_var = 30

read_func()
write_func()
read_func()
rewrite_func()
read_func()