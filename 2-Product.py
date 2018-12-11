# Given an array of integers, return a new array such that each element 
# at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

def GetProduct(numbers, i):

    product = 1

    for number in numbers:
        if number != i:
            product = product * number
    
    if product == 1:
        return 0
    else:
        return product


def GetProducts(numbers):

    products = []

    for i in range(0, len(numbers)):
        products.append(GetProduct(numbers, numbers[i]))

    return products

numbers = [1, 2, 3, 4, 5]

products = GetProducts(numbers)
print products