#SIMPLE Calculator
import math

print("The simple calculator is only for two numbers")
def summa(a:float,b:float):
    """[counts sum of two numbers]

    Args:
        a (float): [number1]
        b (float): [number2]

    Returns:
        [float]: [sum]
    """
    return a+b

def ero(a:float,b:float):
    """[counts substraction of two numbers]

    Args:
        a (float): [number1]
        b (float): [number2]

    Returns:
        [float]: [substarction: number1-number2]
    """
    return a-b

def tulo(a:float,b:float):
    """[return multiplication of two numbers]

    Args:
        a (float): [number1]
        b (float): [number2]

    Returns:
        [float]: [multiplication]
    """
    return a*b

def jako(a:float,b:float):
    """[returns division of two numbers]

    Args:
        a (float): [number1]
        b (float): [number2]

    Returns:
        [type]: [division of number1 by number2]
    """
    return a/b

def potenssi(a:float,b:float):
    """[returns power]

    Args:
        a (float): [number1]
        b (float): [number2]

    Returns:
        [float]: [number1 powered by number2]
    """
    return a**b

def root(a:float,b:float):
    """[returns 2 roots of two different numbers]

    Args:
        a (float): [number1]
        b (float): [number2]

    Returns:
        [float]: [square root of number1 and square root of number2]
    """
    return math.sqrt(a),"and",math.sqrt(b)

try:
    print("1=summa; 2=substraction; 3=multiplication; 4=division; 5=power(number1^number2); 6=square root of two numbers")
    valinta=int(input("Please choose what would you like to count(1-6): "))
    number1=float(input("Please enter the 1. number: "))
    number2=float(input("Please enter the 2.number: "))
    if valinta==1:
        print(summa(number1,number2))
    elif valinta==2:
        print(ero(number1,number2))
    elif valinta==3:
        print(tulo(number1,number2))
    elif valinta==4:
        print(jako(number1,number2))
    elif valinta==5:
        print(potenssi(number1,number2))
    elif valinta==6:
        print(root(number1,number2))
    else:
        print("Wrong input, you can choose only between 1-6")
except:
    print("Wrong input, you can choose only between 1-6")