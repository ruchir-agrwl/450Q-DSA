# For a given value k, find the kth smallest element in the array

def kth_smallest(arr, k):
    arr.sort()
    return arr[k-1]


# Driver Code
ip = [7, 2, 8, 9, 12, 1]
k = 3
print("Kth smallest element is ->", kth_smallest(ip, k))
