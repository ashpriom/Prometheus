# Prometheus Scientific Calculator
# SOEN 6011 - F
# The MIT License (MIT)
# Copyright (c) 2015 Syed Ashfaque Uddin Priom, Raveena Sharma, Gurpreet Singh Rehal,
# Karanvir Singh Sawhney, Het Makrandbhai Shah, Ajeet Singh, Vignesh Rajasekar Shanmugaraja
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

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
