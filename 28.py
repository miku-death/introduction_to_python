def strange_sum(a, b):
    if b > 0:
        return strange_sum(a + 1, b - 1)
    else:
        return a

print(strange_sum(int(input()), int(input())))
