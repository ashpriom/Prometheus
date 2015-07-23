class E():
    def exp(x):
        e = 2.7182818285  # approximate value of e is used here
        result = e ** x  # calculate e^x and print the result
        return result

    loop = 0
    while True:
        print("Enter the value of x");
        x = float(input("Enter value of x:"))
        output = exp(x)
        print(output);
        loop += 1
