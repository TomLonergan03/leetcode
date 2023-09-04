def diagonalDifference(arr):
    difference = 0
    n = len(arr)
    for i in range(n):
        difference += arr[i][i]
        difference -= arr[i][n - i - 1]
    return abs(difference)
