class Phone:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.memory = 128

class Joystick:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.price = "1.500UAH"
class Tablet(Joystick, Phone):
    def print_info(self):
        print(self.model)
        print(self.price)
        print(self.memory)
apple = Tablet(model ="Last")
apple.print_info()