# combine with 2.py

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def shownumber(self):
        print(self.real,"i +",self.img,"j")
    def __add__(num1, num2):
        newReal = num1.real + num2.real
        newImg = num1.img + num2.img
        return Complex(newReal, newImg)
    def __sub__(num1, num2):
        newReal = num1.real - num2.real
        newImg = num1.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(1,3)
num1.shownumber()
num2 = Complex(4,6)
num2.shownumber()
num3 = num2 + num1
num3.shownumber()
num4 = num1 - num2
num4.shownumber()