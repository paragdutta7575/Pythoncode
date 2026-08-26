
def divide (a,b):
    try:
        result = a/b
        print (f"Result is here {result}")
    except ZeroDivisionError:
        print("Can not be divisible by 0")

divide (12,2)
divide (10, 0)        
