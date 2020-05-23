# Fizzbuzz Problem
# For all numbers from 1 to 100, every number divisible by 3 is a "fizz", every number divisible by 5 is a "buzz",
# Every number divisible by both is "Fizzbuzz"


def isFizz(testNum):
    if testNum % 3 == 0:
        return True
    else:
        return False


def isBuzz(testNum):
    if testNum % 5 == 0:
        return True
    else:
        return False


nums = []
for i in range(1, 100):
    if isFizz(i) & isBuzz(i):
        nums.append("Fizzbuzz")
    elif isFizz(i):
        nums.append("Fizz")
    elif isBuzz(i):
        nums.append("Buzz")
    else:
        nums.append(i)
for value in nums:
    print(value)

print("end")