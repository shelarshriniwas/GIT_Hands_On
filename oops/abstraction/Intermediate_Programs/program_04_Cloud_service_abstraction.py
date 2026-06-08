# program_04_Cloud_service_abstraction.py
from abc import ABC, abstractmethod

class Server(ABC):

    @abstractmethod
    def deploy(self):
        pass


class Azure(Server):

    def deploy(self):

        print("Application Deployed on Azure")


obj = Azure()

obj.deploy()