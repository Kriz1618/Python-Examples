def examp():
    class MyComplexNumber:
        #  Contructor methods
        def __init__(self, real = 0, imag = 0) -> None:
            print('Calss constructing...')
            self.real_part = real
            self.imag_part = imag
        
        def displayComplex(self):
            print("{0} + {1}j".format(self.real_part, self.imag_part))        

    # Create a new object against MyComplex class

    cmpx1 = MyComplexNumber(40, 50)
    cmpx1.displayComplex()

    # Adding new property

    cmpx2 = MyComplexNumber(60, 70)
    cmpx2.new_attribute = 80
    print(cmpx2.real_part, cmpx2.imag_part,  cmpx2.new_attribute)
    cmpx2.displayComplex()

    # Deleting properties 

    cmpx3 = MyComplexNumber(60, 70)
    del cmpx3.real_part
    print(cmpx3)
    del cmpx3
    # print('cmpx3', cmpx3)



    class myBird:
        
        def __init__(self):
            print('myBird class constructor executing..')
            
        def whatType(self):
            print('I am a bird')
        
        def canSwim(self):
            print('I can swim..')
        
        def canFly(self):
            print('I can fly')
            
    class myPenguin(myBird):
        
        def __init__(self):
            super().__init__()
            print('myPenguin class contructor executing')
            
        def whoisthis(self):
            print('I am Penguin')
            
        def canRun(self):
            print('I can run faster...')
            
        def canFly(self):
            print('I can not fly..')
            
    pgl = myPenguin()

    pgl.whatType()
    pgl.whoisthis()
    pgl.canSwim()
    pgl.canFly()

    class Base1:
        def funcBase1(self):
            print('funcBase1() running...')
        
    class Base2:
        def funcBase2(self):
            print('funcBase2() running...')
        
    class Base3:
        def funcBase3(self):
            print('funcBase3() running...')
            
    class MultiInheritance(Base1, Base2, Base3):
        def funcMultiDerived(self):
            print('funcMultiInheritance() running...')
            
    md1 = MultiInheritance()

    md1.funcBase1()
    md1.funcBase2()
    md1.funcBase3()
    md1.funcMultiDerived()
    
def exm1():
    class Temp_Celsius:
        def __init__(self, temperature = 0):
            print('Assigning temperature value')   
            self._temperature = temperature
            self.temp = 500
            
        def convert_to_fahrenheit(self):
            return (self._temperature * 1.8) + 32
        
        def get_temperature(self):
            print('Getting temperature value')
            return self._temperature
        
        def set_temperature(self, value):
            if value < -273:
                raise ValueError('Temperature below -273 is not possible')
            print('Setting temperature')
            self._temperature = value
        
        temperature = property(get_temperature, set_temperature)
        
        # temperature = property()
        # temperature = temperature.getter(get_temperature)
        # temperature = temperature.setter(set_temperature)
        
    # c = Temp_Celsius(5)
    # print(c.temperature)
    # c.temperature=100
    # print(c.temperature)
    # print(c.__dict__)
    
    class Celsius:
        def __init__(self, temperature = 0):
            print('Assigning temperature value')   
            self._temperature = temperature
            
        def to_fahrenheit(self):
            return (self._temperature * 1.8) + 32
        
        @property
        def temperature(self):
            print('Getting temperature value')
            return self._temperature
        
        @temperature.setter
        def temperature(self, value):
            if value < -273:
                raise ValueError('Temperature below -273 is not possible')
            print('Setting temperature')
            self._temperature = value
    c = Celsius(5)
    print(c.temperature)
    c.temperature=100
    print(c.temperature)
exm1()