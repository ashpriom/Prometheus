class Pi():
    def PiToX(x):
        result = 1.0
        pi = 3.1415926536
        n = x
        if n > 0:
            for i in range(1, int(n + 1)):
                result *= pi
        else:
            for i in range(1, int(n + 1)):
                result *= pi
            result = 1 / result
        while n < 0:
            result /= pi
            n += 1
        return result
    loop = 0
    while True:
        print("Enter the value of x");
        x = float(input("Enter value of x:"))
        output = PiToX(x)
        print(output);
        loop += 1
