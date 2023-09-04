def countingSort(arr):
    count = [0 for _ in range(100)]
    for item in arr:
        count[item] += 1
    return count
