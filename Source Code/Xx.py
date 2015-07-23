class Xx():
    def XPowerX(x):
        base = x
        value = 1
        if base > 0:
            exponent = int(base + 0.5)
        else:
            exponent = int(base - 0.5)
        if exponent > 0:
            while exponent > 0:
                value *= base
                exponent -= 1
            print(exponent)
        elif exponent < 0:
            base = 1 / base
            exponent *= -1
            while exponent > 0:
                value *= base
                exponent -= 1
        else:
            value = 0
        x = value
        return x
    loop = 0
    while True:
        print("Enter the value of x");
        x = float(input("Enter value of x:"))
        output = XPowerX(x)
        print(output);
        loop += 1
