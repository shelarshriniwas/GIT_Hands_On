# program_06_Notification_abstraction.py
from abc import ABC, abstractmethod

class Alert(ABC):

    @abstractmethod
    def message(self):
        pass


class SMS(Alert):

    def message(self):

        print("SMS Alert Sent")


obj = SMS()

obj.message()