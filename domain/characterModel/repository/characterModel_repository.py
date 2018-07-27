from abc import ABC, abstractmethod

class CharacterModelRepository(ABC):

    @abstractmethod
    def find(self, id):
        pass

    @abstractmethod
    def save(self, model):
        pass

    @abstractmethod
    def ls(self):
        pass