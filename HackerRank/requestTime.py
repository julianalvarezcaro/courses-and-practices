# This problem was part of a technical challenge. I could NOT complete this task
# I didn't save the problem statement nor test cases

# TODO: Complete later

def droppedRequests(requestTime):
    dropped = 0
    ocurr = 0
    past = requestTime[0]
    pos = 0

    tenSec = 0
    minSec = 0
    if len(requestTime) == 1:
        return dropped
    for current in requestTime:
        # print(f'In a minute: {len(requestTime[minSec:pos])}')
        # print(minSec)
        if len(requestTime[minSec:pos]) > 60:
            # print("Minute")
            dropped += 1
        elif len(requestTime[tenSec:pos]) > 20:
            # print("10 seconds")
            dropped += 1
        else:
            if current == past:
                ocurr += 1
            else:
                past = current
                ocurr = 1
            if ocurr > 3:
                dropped += 1
        while(requestTime[pos] - requestTime[tenSec] > 10):
            # print("Im in ten")
            # print (f'pos - tenSec = {pos} - {tenSec} = {pos - tenSec}')
            if tenSec == pos - 1:
                break
            tenSec += 1
        while(requestTime[pos] - requestTime[minSec] > 59):
            #print("Im in min")
            if minSec == pos - 1:
                break
            minSec += 1
        pos += 1
    return dropped

if __name__ == '__main__':
    arr = [1,1,1,1,2]
    print(droppedRequests(arr))