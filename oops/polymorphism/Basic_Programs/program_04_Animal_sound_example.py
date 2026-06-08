# program_04_Animal_sound_example.py

class Lion:

    def sound(self):

        print("Lion Roars")


class Cow:

    def sound(self):

        print("Cow Moos")


animals = [Lion(), Cow()]

# Same method behaves differently
for animal in animals:

    animal.sound()