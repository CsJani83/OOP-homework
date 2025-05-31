from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, rendszam, marka, berleti_dij):
        self.rendszam = rendszam
        self.marka = marka
        self.berleti_dij = berleti_dij
    
    @abstractmethod
    def get_auto_tipus(self):
        pass
