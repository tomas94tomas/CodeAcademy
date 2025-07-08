class Animal:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print(self.sound)

if __name__ == "__main__":
    dog = Animal("Woof!")
    dog.make_sound()
