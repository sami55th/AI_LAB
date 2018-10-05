class shape:
    def __init__(self):
        print("Shape constructor called")

    @staticmethod
    def printType():
        print("shape")


class rectangle(shape):
    def __init__(self):
        super().__init__()
        self.lenght=0
        self.width=0

    def draw(self):
        print("Draw Rectangle")

class Triangle(shape):
    def __init__(self):
        super().__init__()
        self.a=0
        self.b=0
        self.c=0

    def draw(self):
        print("draw triangle")


s=rectangle().draw()
t=Triangle().draw()