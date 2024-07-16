class Vehicle:      #Base class
    def start_engine(self):
        message="Engine started."       #Local variable
        print(message,traffic_light,"\n")

class Car(Vehicle):     #Inherited from vehicle class (Inheritance)
    def __init__(self,make):
        self.make=make
    def start_engine(self):     #Overrides base class method (Polymorphism)
        message="Car Engine started."       #Local variable
        print(message,traffic_light,"\n")

class Bike(Vehicle):        #Inherited from vehicle class (Inheritance)
    def __init__(self,type):
        self.type=type
    def start_engine(self):     #Overrides base class method (Polymorphism)
        message="Bike Engine started."      #Local variable
        print(message,traffic_light,"\n")

speed_limit=60      #Module-level variable

if __name__ == "__main__":      #So that below lines of code is executed only when this file is directly executed and not executed when this file is imported as a module
    traffic_light="Green"       #Global variable

    v1=Vehicle()        #Vehicle class object instantiated
    v1.start_engine()

    c1=Car("Ford")      #Car class object instantiated
    print(c1.make)
    c1.start_engine()

    b1=Bike("Sport")        #Bike class object instantiated
    print(b1.type)
    b1.start_engine()