# Link to the challenge:
# https://www.hackerrank.com/challenges/2d-array/problem

# Summary:
# In a given a 6x6 array are 16 sets of 'hourglasses', like this:
# a b c
# - d -
# e f g

# The problem consists of finding all the sums of the different hourglasses
# and returning the biggest result of them all.


def hourglassSum(arr):
    # Takes in a 6x6 array
    # Return: greater possible sum among all the possible hourglasses

    # ! Notes for coding self: because of the size of the hourglass,
    # ! the start (top-left) of it cannot be passed the row or col 3
    # ? In case of a different size of array, the limits would be defined by:
    # ? numberOfRows - 3 / numberOfCols - 3

    posRow = 0

    sums = []

    for row in arr[:4]:
        posCol = 0
        for col in row[:4]:
            sumTop = sum(row[posCol:posCol+3])
            sumBot = sum(arr[posRow+2][posCol:posCol+3])
            totalSum = sumTop + arr[posRow+1][posCol+1] + sumBot
            sums.append(totalSum)
            posCol += 1
        posRow += 1

    return max(sums)


if __name__ == '__main__':
    # ! Just a test case
    array = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
        ]
    print(hourglassSum(array))
