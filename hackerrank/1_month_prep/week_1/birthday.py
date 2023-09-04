def birthday(s, d, m):
    total = 0
    for i in range(len(s) - m + 1):
        if sum(s[i:i + m]) == d:
            total += 1
    return total


print(birthday([2, 2, 1, 3, 2], 4, 2))
