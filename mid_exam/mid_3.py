
class MyComplex:
    def __init__(self, a, b):
        if a[0] == '-':
            self.real_1, self.imaginary_1 = int(a[:2]), int(a[2:-1])
        else:
            self.real_1, self.imaginary_1 = int(a[0]), int(a[1:-1])
        
        if b[0] == '-':
            self.real_2, self.imaginary_2 = int(b[:2]), int(b[2:-1])
        else:
            self.real_2, self.imaginary_2 = int(b[0]), int(b[1:-1])
    
    def plus(self):
        plus_real = self.real_1 + self.real_2
        plus_imaginary = self.imaginary_1 + self.imaginary_2
        if plus_imaginary > 0:
            print(str(plus_real) + '+' + str(plus_imaginary) + 'i')
        else:
            print(str(plus_real) + str(plus_imaginary) + 'i')
        
    def minus(self):
        plus_real = self.real_1 - self.real_2
        plus_imaginary = self.imaginary_1 - self.imaginary_2
        if plus_imaginary > 0:
            print(str(plus_real) + '+' + str(plus_imaginary) + 'i')
        else:
            print(str(plus_real) + str(plus_imaginary) + 'i')

mycalss = MyComplex('2-3i', '-5+4i')
mycalss.plus()
mycalss.minus()