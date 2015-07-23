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
