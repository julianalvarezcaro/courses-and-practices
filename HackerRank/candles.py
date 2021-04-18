# Link to the challenge:
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

# Summary:
# Given an array of integers, the number of occurrences of the biggest
# number of the array must be returned


def birthdayCakeCandles(candles):
    return (candles.count(max(candles)))


if __name__ == '__main__':
    candles = [3, 2, 1, 3]
    print(birthdayCakeCandles(candles))
