## Inheritance ##


class Animal:  # Base class (parent class)
    def __init__(self):
        pass  # Placeholder for initialization in the Animal class

class Fish(Animal):  # Inherits from Animal class (child class)
    def __init__(self):
        super().__init__()  # Call the parent class's __init__ method
        pass  # Placeholder for Fish-specific initialization


# # Example a) without inheritance
# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#     def breath(self):
#         print("Inhale, exhale.")
#
#
# class Fish():
#     def swim(self):
#         print("Moving in water.")
# nemo = Fish()
# nemo.swim()

## Example a) with inheritance
class Animal:
    def __init__(self):
        self.num_eyes = 2
    def breath(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()
    def breath(self):
        super().breath()
        print("Doing this underwater")
    def swim(self):
        print("Moving in water.")

nemo = Fish()
# nemo.swim()
nemo.breath()
# print(nemo.num_eyes)













