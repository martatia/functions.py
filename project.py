#SIMPLE Calculator
import math

print("The simple calculator is only for two numbers")
def addition(a:float,b:float):
    """[counts sum of two numbers]

    Args:
        a (float): [number1]
        b (float): [number2]

    Returns:
        [float]: [sum]
    """
    return a+b

def substraction(a:float,b:float):
    """[counts substraction of two numbers]

    Args:
        a (float): [number1]
        b (float): [number2]

    Returns:
        [float]: [substarction: number1-number2]
    """
    return a-b

def multiplication(a:float,b:float):
    """[return multiplication of two numbers]

    Args:
        a (float): [number1]
        b (float): [number2]

    Returns:
        [float]: [multiplication]
    """
    return a*b

def division(a:float,b:float):
    """[returns division of two numbers]

    Args:
        a (float): [number1]
        b (float): [number2]

    Returns:
        [type]: [division of number1 by number2]
    """
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by 0."

def power(a:float,b:float):
    """[returns power]

    Args:
        a (float): [number1]
        b (float): [number2]

    Returns:
        [float]: [number1 powered by number2]
    """
    return a**b

def root(a:float,b:float):
    """[returns 2 square roots of two different numbers]

    Args:
        a (float): [number1]
        b (float): [number2]

    Returns:
        [float]: [square root of number1 and square root of number2]
    """
    try:
        if a<0 and b>0:
            return f"The first number is bellow 0, the second square root is {math.sqrt(b)}."
        elif a>0 and b<0:
            return f"The first square root is {math.sqrt(a)}, number is bellow 0."
        else:
            return f"{math.sqrt(a)} and {math.sqrt(b)}."
    except:
        return "Cannot find square root from negative numbers."


try:
    while True:
        print("1=addition; 2=substraction; 3=multiplication; 4=division; 5=power(number1^number2); 6=square root of two numbers; 7=exit")
        choice=int(input("Please choose what would you like to count(1-7): "))
        if choice==7:
            break
        elif choice>7 or choice<1:
            print("Please choose between 1-7.")
            continue
        else:

            number1=float(input("Please enter the 1. number: "))
            number2=float(input("Please enter the 2.number: "))

            if choice==1:
                print(addition(number1,number2))
            elif choice==2:
                print(substraction(number1,number2))
            elif choice==3:
                print(multiplication(number1,number2))
            elif choice==4:
                print(division(number1,number2))
            elif choice==5:
                print(power(number1,number2))
            elif choice==6:
                print(root(number1,number2))
except ValueError:
    print("Wrong input. Please start over.")

print("Thank you for using the calculator!")