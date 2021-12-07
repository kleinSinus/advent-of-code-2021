# takes number array arr, computes the sums over a window of size i, returns array with sums
def window_sums(arr, i):
    out_array_size = len(arr)-i+1
    window_sums = [0]*out_array_size
    for a in range(out_array_size):
        for b in range(i):
            window_sums[a] += arr[a+b]
    return window_sums

# takes number array arr, computes number of increases between values
def count_increments(arr):
    array_size = len(arr)
    counter = 0
    for i in range(array_size-1):
        if arr[i+1] > arr[i]:
            counter += 1
    return counter

# goes through an int array arr
# compares the values
# returns 1 for increase, -1 for decrease,
# 0 for nothing and at index 0 where nothing can be compared yet
def pairwise_compare(arr):
    result = [0] * len(arr)
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            result[i+1] = 1
        elif arr[i] > arr[i+1]:
            print("foo")
            result[i+1] = -1
    return result

# sum over an int array
def array_sum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum
