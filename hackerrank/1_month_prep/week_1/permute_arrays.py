def twoArrays(k, A, B):
    A = sorted(A)
    B = sorted(B, reverse=True)
    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"
    return "YES"


print(twoArrays(10, [2, 1, 3], [7, 8, 9]))
