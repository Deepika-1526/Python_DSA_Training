def Buildings(arr, n):
    count = 1
    curr_max = arr[0]
    for i in range(1, n):
        if arr[i] >= curr_max:
            count += 1
            curr_max = arr[i]
    return count

arr = [3, 5, 9, 6, 8, 10]
n = len(arr)
print(Buildings(arr, n))