# program_09_File_handling_abstraction.py

from abc import ABC, abstractmethod

class File(ABC):

    @abstractmethod
    def open_file(self):
        pass


class TextFile(File):

    def open_file(self):

        print("Opening Text File")


obj = TextFile()

obj.open_file()