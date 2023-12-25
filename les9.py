
def sum_range(start, end):
    if start > end:
        start, end = end, start
    s = 0
    for i in range(start, end + 1):
        s += i

    return s

print(sum_range(5, 10))

