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

from tkinter import *
from tkinter import ttk


def exp(x):
    e = 2.7182818285  # approximate value of e is used here
    result = e ** x
    return result


#   A pop up message is displayed when the user clicks "?" button
def popupmsg(msg):
    popup = Tk()
    popup.wm_title("Prometheus Usage")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=30, padx=30)
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


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


# Calc is the main class. Additionally it is linked with Sine and Cosine classes.
class Calc:
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False

    #   The number on the text box or the input number, is defined in this function
    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2

        self.display(self.current)  # self.current is the input value / the x for all functions

    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def do_sum(self):
        if self.op == "add":
            self.total += self.current  # self.total is the latest result
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current

        # Calculate pi to the power x
        if self.op == "pi":
            result = 1.0
            pi = 3.1415926536
            n = self.current
            if n < 1000:
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
            else:
                result = "unbound input"
            self.total = result
            self.current = self.total

        # Calculate ln(x)
        if self.op == "ln":
            result = 1.0
            num1 = self.current
            if num1 == 0:
                result = -8
            elif num1 < 0:
                result = "undefined"
            else:
                result = ln(num1)
            self.total = result
            self.current = self.total

        # Calculate e to the power x
        if self.op == "e":
            x = self.current
            result = exp(x)
            self.total = result
            self.current = self.total

        # Calculate x to the power x
        if self.op == "xx":
            base = self.current
            value = 1

            if base > 0:
                exponent = int(base + 0.5)
            else:
                exponent = int(base - 0.5)

            if exponent > 0:
                while exponent > 0:
                    value *= base
                    exponent -= 1
                print(exponent)
            elif exponent < 0:
                base = 1 / base
                exponent *= -1
                while exponent > 0:
                    value *= base
                    exponent -= 1
            else:
                value = 0
            self.total = value
            self.current = self.total

        # Calculate 10 to the power x
        if self.op == "ten":
            power = 1
            result = 1.0
            ln_10 = 2.3025850929940456840179914546844
            x = self.current

            if x < 10000:
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
                        p = exp(q)
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
                        p = exp(q)
                        for i in range(y, 0):
                            power *= 0.10
                        power *= p
                        result = power
            else:
                result = "unbound input"

            self.total = result
            self.current = self.total

        # Calculate Sine(x)
        if self.op == "sine":
            sin = Sine()
            sin.checkOperation()
            self.total = sin.checkOperation()
            self.current = self.total

        # Calculate Cos(x)
        if self.op == "cosine":
            sin = Cosine()
            sin.checkOperation()
            self.total = sin.checkOperation()
            self.current = self.total

        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = 0
        self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def cancel(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_cancel(self):
        self.cancel()
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)


class Sine(Calc):
    PI = 3.141592653589793

    def __init__(self):
        super().__init__()
        self.current = float(text_box.get())

    def print_rad(self):
        print('radians=', self.radians)

    def print_deg(self):
        print('degrees=', self.degrees)

    def checkOperation(self, now=None):
        self.degrees = 1
        result = 1
        self.degrees = self.current
        choice2 = 2
        if choice2 == 1:
            print("wrong block")
        elif choice2 == 2:
            res = self.sine_degrees(self.degrees)
            result = round(res, 6)
        else:
            self.checkOperation(now)
        return res

    def fact(self, y):
        if y == 0 or y == 1:
            return 1
        else:
            return y * self.fact(y - 1)

    def sine_radians(self, x):
        """

        :rtype : sin
        """
        sum = 0
        if x == 0:
            sum = 0.0
        else:
            i = 1
            while i <= 10:
                tmp = 2 * i - 1
                q = x ** tmp
                fact_i = self.fact(tmp)
                if i % 2 == 1:
                    sum += (q / fact_i)
                else:
                    sum -= (q / fact_i)
                i += 1
        return sum

    def sine_degrees(self, y):
        y = int(self.degrees)
        if y >= 0:
            tmp = y
        else:
            tmp = -y
        rem = int(tmp) % 360
        if 0 <= rem <= 90:
            x = (self.PI / 180) * rem
            res = self.sine_radians(x)
        elif 90 < rem <= 180:
            x = (self.PI / 180) * (rem - 90)
            res = (1 - self.sine_radians(x) ** 2) ** (1 / 2)
        elif 180 < rem <= 270:
            x = (self.PI / 180) * (rem - 180)
            res = -self.sine_radians(x)
        else:
            x = (self.PI / 180) * (rem - 270)
            res = -(1 - self.sine_radians(x) ** 2) ** (1 / 2)
        return res


class Cosine(Calc):
    PI = 3.141592653589793

    def __init__(self):
        super().__init__()
        self.current = float(text_box.get())

    def printRad(self):
        print('radians=', self.radians)

    def printRad(self):
        print('degrees=', self.degrees)

    def checkOperation(self, now=None):
        self.degrees = 1
        result = 1
        self.degrees = self.current
        choice2 = 2
        if choice2 == 1:
            print('Wrong choice')
        elif choice2 == 2:
            res = self.cosine_degrees(self.degrees)
        else:
            self.checkOperation(now)
        return res

    def fact(self, y):
        if y == 0 or y == 1:
            return 1
        else:
            return y * self.fact(y - 1)

    def cosine_radians(self, x):
        """

        :rtype : sin
        """
        sum = 0
        if x == 0:
            sum = 1.0
        else:
            if x == 1.57:
                sum = 0
            else:
                for i in range(1, 10):
                    tmp = 2 * i - 2
                    q = x ** tmp
                    fact_i = self.fact(tmp)
                    if i % 2 == 1:
                        sum += (q / fact_i)
                    else:
                        sum -= (q / fact_i)
        return sum

    def cosine_degrees(self, y):
        y = int(self.degrees)
        if y >= 0:
            tmp = y
        else:
            tmp = -y
        rem = int(tmp) % 360
        if 0 <= rem <= 90:
            x = (self.PI / 180) * rem
            res = self.cosine_radians(x)
        elif 90 < rem <= 180:
            x = (self.PI / 180) * (rem - 90)
            res = -(1 - self.cosine_radians(x) ** 2) ** (1 / 2)
        elif 180 < rem <= 270:
            x = (self.PI / 180) * (rem - 180)
            res = -self.cosine_radians(x)
        else:
            x = (self.PI / 180) * (rem - 270)
            res = (1 - self.cosine_radians(x) ** 2) ** (1 / 2)
        return res


sum1 = Calc()
root = Tk()
calc = Frame(root)
calc.grid()

root.title("Prometheus")
text_box = Entry(calc, justify=RIGHT)
text_box.grid(row=0, column=0, columnspan=100, ipady=5, ipadx=10, pady=5, padx=5)
text_box.insert(0, "0")

#   Buttons for 1-9 are defined here
numbers = "789456123"
i = 0
bttn = []
for j in range(1, 4):
    for k in range(3):
        bttn.append(Button(calc, text=numbers[i]))
        bttn[i].grid(row=j, column=k, pady=5, ipadx=10, ipady=10)
        bttn[i]["command"] = lambda x=numbers[i]: sum1.num_press(x)
        i += 1

# The Zero Button
button_0 = Button(calc, text="0")
button_0["command"] = lambda: sum1.num_press(0)
button_0.grid(row=4, column=1, pady=5, ipadx=10, ipady=10)

#   Division
button_div = Button(calc, text=chr(247))
button_div["command"] = lambda: sum1.operation("divide")
button_div.grid(row=1, column=3, pady=5, ipadx=8, ipady=10)

#   Multiplication
button_mult = Button(calc, text="x")
button_mult["command"] = lambda: sum1.operation("times")
button_mult.grid(row=2, column=3, pady=5, ipadx=10, ipady=10)

#   Subtraction
button_minus = Button(calc, text="-")
button_minus["command"] = lambda: sum1.operation("minus")
button_minus.grid(row=3, column=3, pady=5, ipadx=10, ipady=10)

#   Pi to the power x
button_pi = Button(calc, text="Pi^x")
button_pi["command"] = lambda: sum1.operation("pi")
button_pi.grid(row=1, column=4, pady=5, padx=5, ipadx=20, ipady=10)

#   ln(x)
button_lnx = Button(calc, text="ln(x)")
button_lnx["command"] = lambda: sum1.operation("ln")
button_lnx.grid(row=2, column=4, pady=5, padx=5, ipadx=20, ipady=10)

#   e to the power x
button_exp = Button(calc, text="e^x")
button_exp["command"] = lambda: sum1.operation("e")
button_exp.grid(row=3, column=4, pady=5, padx=5, ipadx=22, ipady=10)

#   Sin(x)
button_sin = Button(calc, text="Sin(x)")
button_sin["command"] = lambda: sum1.operation("sine")
button_sin.grid(row=2, column=5, pady=5, padx=5, ipadx=18, ipady=10)

#   Cos(x)
button_cos = Button(calc, text="Cos(x)")
button_cos["command"] = lambda: sum1.operation("cosine")
button_cos.grid(row=3, column=5, pady=5, padx=5, ipadx=15, ipady=10)

#   x to the power x
button_xx = Button(calc, text="x^x")
button_xx["command"] = lambda: sum1.operation("xx")
button_xx.grid(row=5, column=4, pady=5, padx=5, ipadx=22, ipady=10)

#   10 to the power x
button_ten = Button(calc, text="10^x")
button_ten["command"] = lambda: sum1.operation("ten")
button_ten.grid(row=4, column=4, pady=5, padx=5, ipadx=20, ipady=10)

#   The Dot
point = Button(calc, text=".")
point["command"] = lambda: sum1.num_press(".")
point.grid(row=4, column=2, pady=5, ipadx=10, ipady=10)

#   Addition
add = Button(calc, text="+")
add["command"] = lambda: sum1.operation("add")
add.grid(row=4, column=3, pady=5, ipadx=10, ipady=10)

#   Reverse positivity/negativity of a digit
neg = Button(calc, text="+/-")
neg["command"] = sum1.sign
neg.grid(row=4, column=0, pady=5, ipadx=5, ipady=10)

#   Shows a pop up menu with information
popup = Button(calc, text="?")
popup["command"] = lambda: popupmsg(
    " Step 1:Press the number pad for input \n Step 2: Select the desired function \n "
    "Step 3: Press = button to see result. \n ")
popup.grid(row=1, column=5, pady=5, padx=5, ipadx=30, ipady=10)

#   Clear input and result (AC)
all_clear = Button(calc, text="AC")
all_clear["command"] = sum1.all_cancel
all_clear.grid(row=5, column=0, pady=5, columnspan=4, padx=0, ipadx=40, ipady=10)

# Calculate result
equals = Button(calc, text="=")
equals["command"] = sum1.calc_total
equals.grid(row=4, column=5, rowspan=2, pady=5, ipadx=28, ipady=40)

root.mainloop()
