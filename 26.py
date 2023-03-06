def power(number, p):
    if p > 1:
        return number * power(number, p - 1)
    else:
        return number

print(power(int(input()), int(input())))
