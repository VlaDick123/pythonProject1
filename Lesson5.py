# class Hello:
#     def __init__(self):
#         print("Hello!")
# class Hello_World(Hello):
#     def __init__(self):
#         super().__init__()
#         print("World!")
# hello_world = Hello_World()

# class Class1:
#     var = 20
#     def __init__(self):
#         self.var = 10
# class Class2(Class1):
#     def __init__(self):
#         print(self.var)
#         super().__init__()
#         print(self.var)
#         print(super().var)
# hello_world = Class2()

class Computer:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.memory = 128
class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = "4k"
class SmartPhone(Display, Computer):
    def print_info(self):
        print(self.model)
        print(self.resolution)
        print(self.memory)
iphone = SmartPhone(model ="Last")
iphone.print_info()