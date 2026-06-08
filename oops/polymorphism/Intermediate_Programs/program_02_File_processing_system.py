# program_02_File_processing_system.py

class TextFile:

    def process(self):

        print("Processing Text File")


class PDFFile:

    def process(self):

        print("Processing PDF File")


files = [TextFile(), PDFFile()]

for file in files:

    file.process()