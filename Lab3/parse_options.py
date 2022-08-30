from abc import ABC, abstractmethod

class ParseOption(ABC):
    @abstractmethod
    def display_menu(self):
        pass
    @abstractmethod
    def get_option(self):
        pass