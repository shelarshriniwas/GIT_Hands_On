# program_10_Report_generation_framework.py
from abc import ABC, abstractmethod

class Export(ABC):

    @abstractmethod
    def export(self):
        pass


class ExcelExport(Export):

    def export(self):

        print("Excel File Exported")


obj = ExcelExport()

obj.export()