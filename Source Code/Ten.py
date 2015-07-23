class Ten():
    def PowerTen(x):
        power = 1
        result = 1.0
        ln_10 = 2.3025850929940456840179914546844
        #  Getting integer part of x and store it in y
        y = int(x / 1)
        #  Getting decimal part of x and store it in z
        z = float(x % y)

        if y == 0:
            result = power
        elif y > 0:
            if z == 0:
                for i in range(0, y):
                    power *= 10
                result = power
            else:
                q = z * ln_10
                p = 2.718 ** q
                for i in range(0, y):
                    power *= 10
                power *= p
                result = power
        elif y < 0:
            if z == 0:
                for i in range(y, 0):
                    power *= 0.10
                result = power
            else:
                q = z * ln_10
                p = 2.718**q
                for i in range(y, 0):
                    power *= 0.10
                power *= p
                result = power
        return result;
    loop=0
    while True:
        print("Enter the value of x");
        x = float(input("Enter value of x:"))
        Output = PowerTen(x)
        print(Output);
        loop += 1    
