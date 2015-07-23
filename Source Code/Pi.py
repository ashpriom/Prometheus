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
