# Calculator
#add, sub... 

#Add

def calc_add(x, y):
    '''
    in: two numbers
    out: sum
    '''
    try:
        if isinstance(x, str):
            x = int(x) #int, float 
    except ValueError as ve:
        print("Looks like a floating point number, converting to float")
        x = float(x)
    except Exception as e:
        print("Some other issue!")

    try:
        if isinstance(y, str):
            y = int(y)
    except ValueError as ve:
        print("Looks like a floating point number, converting to float")
        y = float(y)
    except Exception as e:
        print("Some other issue!")

    return x+y

# Inputs, test cases
#------
# int,
# float
# int as str
# float as str