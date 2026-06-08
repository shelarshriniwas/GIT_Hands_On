# program_05_Use_class_methods.py

class Demo:

    count = 0

    @classmethod
    def update(cls):
        cls.count += 1

Demo.update()

print(Demo.count)