from abc import ABC, abstractmethod

class ICrud(ABC):

    @abstractmethod
    def create(self):
        raise NotImplementedError

    @abstractmethod
    def read(self):
        raise NotImplementedError

    @abstractmethod
    def relation(self):
        raise NotImplementedError