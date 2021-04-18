# Link to the challenge:
# https://www.hackerrank.com/challenges/mini-max-sum/problem

# Summary:
# Given an array of 5 integers, the maximun posible sum and
# the minimun posible with 4 of the 5 integers sum must be printed


def miniMaxSum(arr):
    totalSum = sum(arr)
    print(f'{totalSum - max(arr)} {totalSum - min(arr)}')


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9]
    miniMaxSum(arr)
