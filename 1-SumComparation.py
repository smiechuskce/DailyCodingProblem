# DailyCodingProblem #1
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# 
# Bonus: Can you do this in one pass?

# Solution 1: Naive - Compare every single number with another and find if the sum is k

def CompareSumWithK(numbers, k):

    if len(numbers) < 2:
        return False

    start = 0

    for number in numbers:
        for nextNumber in numbers[start+1:]:
            if (number + nextNumber) == k:
                return True
        start = start + 1
    return False

# Solution 2: One pass - Find the differences between numbers and k, store them in a set and after that search if number exists in this set

def CompareSumWithKInOnePass(numbers, k):

    if len(numbers) < 2:
        return False

    substractResults = set()

    for number in numbers:
        substractResults.add(k - number)

    for i in range(0, len(numbers)):
        if numbers[i] in substractResults:
            return True

    return False

numbers = [1, 15, 3, 7]
k = 4

result = "For loop version has given a: " + str(CompareSumWithK(numbers, k))
print result

result = "One pass version has given a: " + str(CompareSumWithKInOnePass(numbers, k))
print result