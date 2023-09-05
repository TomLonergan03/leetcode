def sockMerchant(n, ar):
    counts = {}
    for sock in ar:
        if sock in counts:
            counts[sock] += 1
        else:
            counts[sock] = 1
    total = 0
    for sock in counts.values():
        total += sock // 2
    return total
