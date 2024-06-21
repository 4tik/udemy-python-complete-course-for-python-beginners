# python class and objetc
class MyComplexNumber:
    def __init__(self, real=0, imag=0):
        print("MyComplexNumber constructor executing.......")
        self.real_part = real
        self.imag_part = imag
    
    def displayComplex(self):
        print(f"{self.real_part} + {self.imag_part}j")
    
# create a new object against MyComplexNumber class
complex_number = MyComplexNumber(40,50)
complex_number.displayComplex()

complex_number_new = MyComplexNumber(4, 8)
complex_number_new.new_attribute = 50