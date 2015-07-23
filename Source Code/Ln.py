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
    
