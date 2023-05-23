def power(a, b):
    if (b == 0):
        return 1
    else:
        if (b % 2 == 0):
            return power(a, b//2)*power(a, b//2)
        else:
            return a * power(a, b//2)*power(a, b//2)


print(power(6,4))
