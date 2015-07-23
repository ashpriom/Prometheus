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

class Cosine:
    PI = 3.141592653589793

    def printRad(self):
        print('radians=',self.radians)

    def printRad(self):
        print('degrees=',self.degrees)

    def checkOperation(self, now=None):
        choice2 = 1
   
        if choice2 == 1:
            self.degrees=x
            res=self.cosine_degrees(self.degrees)
            print("cosine(",self.degrees,'degrees)=',round(res,6))
        else:
            self.checkOperation(now)

    def fact(self, y):
        if y == 0 or y==1:
         return 1
        else:
         return y * self.fact(y - 1)

    def cosine_radians(self, x):
        sum=0
        if x==0:
            sum=1.0
        else:
           if x==1.57:
              sum=0
           else:
               for i in range(1,10):
                    tmp= 2*i-2
                    q = x**tmp
                    fact_i= self.fact(tmp)
                    if i%2==1:
                        sum+= (q/fact_i)
                    else:
                     sum-=(q/fact_i)
        return sum

    def cosine_degrees(self, y):
        if y>=0:
            tmp = y
        else:
            tmp = -y
        rem = int(tmp)%360
        if rem >= 0 and rem <= 90:
            x = (self.PI/180)*rem
            res = self.cosine_radians(x)
        elif rem > 90 and rem <= 180:
            x = (self.PI/180)*(rem-90)
            res = -(1 - self.cosine_radians(x)**2)**(1/2)
        elif rem>180 and rem <= 270:
            x = (self.PI/180)*(rem-180)
            res = -self.cosine_radians(x)
        else:
            x = (self.PI/180)*(rem-270)
            res = (1 - self.cosine_radians(x)**2)**(1/2)
        return res

    
loop = 0
while True:
    print("Enter the value of x");
    x = float(input("Enter value of x:"))
    sin = Cosine()
    sin.checkOperation()
    loop += 1

