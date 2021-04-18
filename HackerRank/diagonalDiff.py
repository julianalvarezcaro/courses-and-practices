# Link to the challenge:
# https://www.hackerrank.com/challenges/diagonal-difference/problem

# Summary:
# Find the absolute difference between the sums of
# both diagonals of a square matrix


def diagonalDifference(arr):
    lrDiagSum = sum([arr[x][x] for x in range(len(arr))])
    rlDiagSum = sum([row[-n-1] for n, row in enumerate(arr)])

    return (abs(lrDiagSum - rlDiagSum))


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
    print(diagonalDifference(array))
