import math


def pairSum(i, param):
    return i + param


def pairSumSequence(n):
    sum = 0
    for i in range(n):
        sum += pairSum(i, i + 1)

    return sum


def isPrime(numb):
    for i in range(2, numb):
        if numb % i == 0:
            return False
    return True


if __name__ == '__main__':
    # print(pairSumSequence(5))
    res = []
    val = 2
    # time complexity becomes n^2
    # the comparison for n-2 items and n times for checking all the numbers
    for num in range(2, 10):
        if isPrime(num):
            res.append(num)

    print(res)
