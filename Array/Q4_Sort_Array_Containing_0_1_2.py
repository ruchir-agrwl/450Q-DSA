# Given an array which contains only 0s, 1s and 2s. Our task is to sort the array without using any sorting
# algorithm.

def sort(arr, n):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        if arr[i] == 0:
            cnt0 += 1
        elif arr[i] == 1:
            cnt1 += 1
        elif arr[i] == 2:
            cnt2 += 1
    i = 0
    while cnt0 > 0:
        arr[i] = 0
        cnt0 -= 1
        i += 1
    while cnt1 > 0:
        arr[i] = 1
        cnt1 -= 1
        i += 1
    while cnt2 > 0:
        arr[i] = 2
        cnt2 -= 1
        i += 1
    return arr


# Driver code
a = [0, 2, 1, 0, 1, 2, 1, 0, 2]
print(sort(a, len(a)))
