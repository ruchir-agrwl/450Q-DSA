# Program to reverse and array

# This method will return the reversed array, the original array will still be in place
def reverse_2(arr):
    return arr[::-1]


# This methods makes changes to the original array
def reverse_1(ip, start, end):
    while start < end:
        ip[start], ip[end] = ip[end], ip[start]
        start += 1
        end -= 1
    return ip


a = [1, 2, 3, 4, 5, 6]
print(reverse_2(a))
print(reverse_1(a, 0, len(a) - 1))
