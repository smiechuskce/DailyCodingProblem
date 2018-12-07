# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# 
# Bonus: Can you do this in one pass?

def CompareSumWithK(numbers, k):

    start = 0

    for number in numbers:
        for nextNumber in numbers[start+1:]:
            if (number + nextNumber) == k:
                return True
        start = start + 1
    return False

numbers = [10, 15, 3, 7]
k = 10

result = CompareSumWithK(numbers, k)
print result 