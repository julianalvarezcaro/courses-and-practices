# Link to the challenge:
# https://www.hackerrank.com/challenges/plus-minus/problem

# Summary:
# Given an array of integers, print the ratio of positive, negatives and zeros
# in the array with a precision of 6 decimal places


def plusMinus(arr):
    # Array to store the amount of [positive, negative, zero] numbers that are
    # in the original array
    quantities = [0, 0, 0]

    for n in arr:
        if n > 0:
            quantities[0] += 1
        elif n < 0:
            quantities[1] += 1
        else:
            quantities[2] += 1
    length = len(arr)
    print("{:.6f}\n{:.6f}\n{:.6f}".format(
        quantities[0] / length,
        quantities[1] / length,
        quantities[2] / length))


if __name__ == '__main__':
    array = [-1, -1, 1, 1, 0]
    plusMinus(array)
