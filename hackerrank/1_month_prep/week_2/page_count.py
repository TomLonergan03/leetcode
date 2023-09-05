def pageCount(n, p):
    left_to_right = p // 2
    return min(left_to_right, n // 2 - left_to_right)


print(pageCount(6, 5))
print(pageCount(5, 4))
