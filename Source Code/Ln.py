loop = 0
def ln(x):
    n = 100000
    value = 0.0
    if x > 0.0:
        if x <= 2.0:
            sign = -1
            base = x - 1.0
            lnpower = 1.0
            for i in range(1, n + 1):
                sign *= -1
                lnpower *= base
                value += lnpower * sign / i
            return value
        elif x > 2.0:
            return -1 * ln(1.0 / x)
    elif x > 2.0:
        return -1 * ln(1.0 / x)

while True:
    print("Enter the value of x");
    x = float(input("Enter value of x:"))
    result = 1.0
    num1 = x
    if num1 == 0:
        result = -8
    elif num1 < 0:
        result = "undefined"
    else:
        result = ln(num1)
    print(result)
    loop += 1    
    
