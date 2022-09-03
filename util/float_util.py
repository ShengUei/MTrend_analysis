import math

def greatter_than(num1, num2):
    int_1 = math.floor(num1)
    fraction_1 = math.floor((num1 - int_1) * 10)

    int_2 = math.floor(num2)
    fraction_2 = math.floor((num2 - int_2) * 10)

    if int_1 == int_2:
        return fraction_1 > fraction_2

    return int_1 > int_2

def equal(num1, num2):
    int_1 = math.floor(num1)
    fraction_1 = math.floor((num1 - int_1) * 10)

    int_2 = math.floor(num2)
    fraction_2 = math.floor((num2 - int_2) * 10)

    return int_1 == int_2 and fraction_1 == fraction_2
