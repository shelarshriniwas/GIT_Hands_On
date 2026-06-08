# program_09_Video_streaming_application.py
from abc import ABC, abstractmethod

class OTTPlatform(ABC):

    @abstractmethod
    def subscription(self):
        pass


class Netflix(OTTPlatform):

    def subscription(self):

        print("Netflix Premium Subscription")


obj = Netflix()

obj.subscription()