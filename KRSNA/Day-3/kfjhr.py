class bird:
    def sound(self):
        print("chirp")

class cat:
    def sound(self):
        print("meow")

def make_sound(animal):
    animal.sound()
b=bird()
c=cat()
make_sound(b)
make_sound(c)
