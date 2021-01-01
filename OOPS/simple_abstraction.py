from abc import ABC, abstractmethod

# Abstraction required when you know in multiple classes you need to \
    # create exactly same methods (Body/Code may vary)

class Car(ABC):

    # Abstract methods must be Over Ridden when any class Inherited this class.
    def __init__(self):
        pass

    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def runs_on(self):
        pass


class Tesla(Car):


    def __init__(self):
        print("Yo!!! Elon :)")
        super().__init__()

    # Over Riding Here
    def type(self):
        print("Proudly Electric")

    def runs_on(self):
        print("Electricity ...")


class BMW(Car):

    # Abstract methods must be OverRidden
    def __init__(self):
        print("Yo!!! BMW :)")
        super().__init__()

    # Over Riding Here
    def type(self):
        print("Diesel Engine ")

    def runs_on(self):
        print("Fuel ...")

if __name__ == "__main__":
    model_x = Tesla()
    # Try commenting runs_on or type method in Tesla Class. It will throw an error \
        # saying it must be over ridden beacuse it is an abstract method
    bmw_m = BMW()



