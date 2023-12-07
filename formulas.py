#SterlingArnold Lab 3 formulas.py
from random import choices
def main():
    print("No")
def add(values: list):
    """
    Add all positive numbers in list
    :param values: list of numbers
    :return: sum of all numbers that are not 0
    """
    temp1 = 0
    for value in values:
        if value > 0:
            temp1 += value
    return(temp1)
def subtract(values: list):
    """
    Subtract all negative numbers in list
    :param values: list of numbers
    :return: difference of all numbers that are not 0
    """
    temp1 = 0
    for value in values:
        if value < 0:
            temp1 += value
    return(temp1)
def multiply(values: list):
    """
    Multiply all numbers in list
    :param values: list of numbers
    :return: product of all numbers that are not 0
    """
    if all(v == 0 for v in values) == True:
        return(0)
    temp1 = 1
    for value in values:
        if value != 0:
            temp1 = temp1*value
    return(temp1)
def divide(values: list):
    """
    Divide all numbers in list
    :param values: list of numbers
    :return: quotient of all numbers that are not 0
    """
    temp1 = values[0]
    for value in values[1:]:
        if value == 0:
            return("Cannot divide by 0")
        temp1 = temp1 / value
    return(temp1)
def choose(values: list):
    """
    Choose a number at random from list
    :param values: list of numbers
    :return: random number from list
    """
    temp1 = choices(values)
    return(temp1[0])

if __name__ == "__main__":
    main()