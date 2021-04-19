# Link to the challenge:
# https://www.hackerrank.com/challenges/time-conversion/problem

# Summary:
# Given a 12-hour format time, return the equivalent in military time


def timeConversion(s):
    hhmmssm = s.split(':')

    if 'AM' in hhmmssm[-1]:
        if hhmmssm[0] == '12':
            return '00' + s[2:-2]
        return s[:-2]
    if hhmmssm[0] == '12':
        return s[:-2]
    return str(int(hhmmssm[0]) + 12) + s[2:-2]


if __name__ == '__main__':
    print(timeConversion('12:45:54PM'))
