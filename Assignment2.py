class Animal:
    def __init__(self, description):
        self.description = description

    def make_sound(self):
        print(f"{self.description} makes a generic animal sound")

class Dog(Animal):
    def __init__(self):
        super().__init__("Dog")

    def make_sound(self):
        super().make_sound()
        print("Bark!")

class Cat(Animal):
    def __init__(self):
        super().__init__("Cat")

    def make_sound(self):
        super().make_sound()
        print("Meow!")

def animal_sound_in_zoo(animal):
    animal.make_sound()

if __name__ == "__main__":
    dog_instance = Dog()
    cat_instance = Cat()

    animal_sound_in_zoo(dog_instance)
    animal_sound_in_zoo(cat_instance)
