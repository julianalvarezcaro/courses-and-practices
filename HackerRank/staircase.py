# Link to the challenge:
# https://www.hackerrank.com/challenges/staircase/problem

# Summary:
# Write a function that will print a staircase using spaces and '#' characters

def staircase(n):
    for row in range(n):
        for col in range(n):
            if col <= (n - 2 - row):
                print(' ', end='')
            else:
                print('#', end='')
        print("")

if __name__ == '__main__':
    n = int(input())

    staircase(n)
