# Program to find out minimum and maximum values in an array using minimum number of comparisons
class MinMax:
    def __init__(self):
        self.min = 0
        self.max = 0


# Method to find the minimum and maximum values in the array.
def get_min_max(arr, n):
    pair = MinMax()
    if n == 1:
        pair.min = arr[0]
        pair.max = arr[0]
        return pair
    if arr[0] > arr[1]:
        pair.min = arr[1]
        pair.max = arr[0]
    else:
        pair.min = arr[0]
        pair.max = arr[1]
    for i in range(2, len(arr)):
        if arr[i] > pair.max:
            pair.max = arr[i]
        elif arr[i] < pair.min:
            pair.min = arr[i]

    return pair


# Driver Code
a = [1, 3, 7, 0, 2, 8]
min_max = get_min_max(a, len(a))
print("Min Element is ->", min_max.min)
print("Max Element is ->", min_max.max)
