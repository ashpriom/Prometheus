# Prometheus
Prometheus is a scientific calculator made with Python.

	Sine 
1.	Start
2.	Read the input "y" via GUI.
3.	Initialize variables "rem", "result" and "tmp" to 1.
4.	tmp = AbsoluteValue(y)
5.	rem= Remainder of division tmp/360
6.	If( 0 ≤ rem ≤ 90) then
a)	x=(PI/ 180)*rem
b)	result=sine(x)
7.	Else If( 90 < rem ≤ 180) then 
a)	x=(PI/ 180)*(rem - 90)
b)	result=  √(1-(sine(x))2)
8.	Else If( 180 < rem ≤ 270)
a)	x=(PI/ 180)*(rem - 180)
b)	result= -sine(x)
9.    Else
a)	x=(PI/ 180)*(rem - 270)
b)	result=  -√(1-(sine(x))2)
10.   Display result
11.   End

	Cosine
1.	Start
2.	Read the input "y" via GUI.
3.	Initialize variables "rem", "result" and "tmp" to 1.
4.	tmp=AbsoluteValue(y)
5.	rem= Remainder of division tmp/360
6.	If( 0 ≤ rem ≤ 90) then
a)	x=(PI/ 180)*rem
b)	result=cosine(x)
       7.   Else If( 90 < rem ≤ 180) then
a)	x=(PI/ 180)*(rem - 90)
b)	result= - √(1-(cosine(x))2)
8.   Else If( 180 < rem ≤ 270) then
a)	x=(PI/ 180)*(rem - 180)
b)	result= -cosine(x)
9.   Else
a)	x=(PI/ 180)*(rem - 270)
b)	result=  √(1-(cosine(x))2)
10.   Display result
11.   End.

	x^x
1.	Start
2.	Read the input "base" via GUI
3.	Initialize variables "exp" to O and "value" to 1
4.	if (base > 0) , then
a)	exp = int(base + 0.5)
5.	else
       a)   exp = int(base - 0.5)
6.	if (exp > 0), then
       a)   while(exp > 0 )
       	(i)    value = value * base
             (ii)   exp = exp - 1
             (iii)  Display exp
7.	else if(exp < 0), then
        a)   base = 1/base
       b)   exp = exp * (-1)
       c)   while (exp > 0)
	(i)   value = value * base
	(ii)  exp = exp - 1
8.	else
        a)   value = 0
        b)   Display value
9.	Exit

	Pi ^ x
1.	Start
2.	Read the input "n" via GUI
3.	Initialize variables "result" to 1 and "pi" to 3.1415926536
4.	if(n > 0), then
a)	for i in range(1,int(n+1))
(i).	result = result * pi
5.	else
a)	for i in range(1,int(n+1))
(i).	result = result * pi
(ii).	result = 1/result
6.	while n<0
a)	result = result /pi
b)	n=n+1
7.	Display result
8.	Exit

	10 ^ x
1.	Start
2.	Read the input "x" via GUI
3.	Initialize variables power =1 and ln_10 = 2.3025850929940445684017991454684
4.	y = int(x/1)
5.	z= float(x%y)
6.	if (y==0),then
a)	result = power
7.	else if ( y > 0)
a)	if (z==0)
a)	for i in range(0,y)
I.	power = power * 10
b)	result = power
b)   else
             (i).   q = z * ln_10
             (ii).  p = exp(q)
             (iii). for i in range(0,y)
	    I.       power = power*10
       (iv).  power = power * p
       (v).   result = power
8.	else if ( y < 0)
b)	if (z==0)
(i).	for i in range(y,0)
I.	power = power * 0.10
(ii).	result = power
b)   else
             (i).   q = z * ln_10
             (ii).  p = exp(q)
             (iii). for i in range(y,0)
	    I.       power = power*0.10
       (iv).  power = power * p
       (v).   result = power
9.    Display result
10.    Exit

	e ^ x
1.	Start
2.	Read the input "x" via GUI
3.	result = e ** x
4.	Display result
5.	End

	ln(x)
1.	Start
2.	Read the input "num1" via GUI
3.	Initialize variable "n" to 10,000 and "value" to 0.0
4.	if(num1 == 0)
a)	Display infinity
5.	else if ( num1 < 0), then
a)	Display undefined
6.	else if ( x >2.0)
a)	Display -1 * ln(1.0/x)
7.	else
a)	if((x > 0.0) && (x <= 2.0))
(i).	sign = -1 
(ii).	base = x - 1.0
	       (iii).lnpower = 1.0
	       (iv).for i in range(1,n+1)
I.	sign = sign * -1
II.	lnpower = lnpower * base
III.	value += lnpower * sign/i
	       (v).return value
b)	else if(x > 2.0)
(i).	Display -1 * ln(1.0/x)
8.	End




