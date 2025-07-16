class parent:
    def show(self):
        print("parents method")

class child(parent):
    def show(self):
        print("child method")

obj = child()
obj.show()
