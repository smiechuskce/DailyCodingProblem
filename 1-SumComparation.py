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

def CompareSumWithKInOnePass(numbers, k, start):
    
    if len(numbers) == 2 and numbers[0] + numbers[1] == k:
        return True
    elif len(numbers) < 2:
        return False
    else:
        return CompareSumWithKInOnePass(numbers[start:], k, start)

numbers = [10, 15, 3, 7]
k = 25

result = CompareSumWithKInOnePass(numbers, k, 1)
print result