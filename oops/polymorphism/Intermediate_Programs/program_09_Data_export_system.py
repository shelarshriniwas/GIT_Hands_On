# program_09_Data_export_system.py

class XMLExport:

    def save(self):

        print("Saved as XML")


class PDFExport:

    def save(self):

        print("Saved as PDF")


x = XMLExport()
p = PDFExport()

x.save()
p.save()