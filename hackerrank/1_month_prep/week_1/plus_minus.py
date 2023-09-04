def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for item in arr:
        if item > 0:
            positive += 1
        elif item == 0:
            zero += 1
        else:
            negative += 1
    total = len(arr)
    print(round(positive / total, 6))
    print(round(negative / total, 6))
    print(round(zero / total, 6))
