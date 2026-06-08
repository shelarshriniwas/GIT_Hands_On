# program_08_Data_hiding_demonstration.py

class Demo:

    def __init__(self):

        self.__data = "Private Data"

    def show(self):

        print(self.__data)


obj = Demo()

obj.show()