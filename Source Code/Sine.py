class Sine():
    PI = 3.141592653589793

    def __init__(self):
        super().__init__()
        self.current = x

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

loop = 0
while True:
    print("Enter the value of x");
    x = float(input("Enter value of x:"))
    sin = Sine()
    sin.checkOperation()
    output = sin.checkOperation()
    print(output);
    loop += 1
