from abc import ABC, abstractmethod


class Camera(ABC):
    """
    Abstract class Camera which have 3 params
    """
    def __init__(self, brand, model, lens):        # constructor
        self.brand = brand
        self.model = model
        self.lens = lens

    @abstractmethod
    def take_photo(self):       # abstract method
        pass

    def __str__(self):          # To String
        return f"Brand: {self.brand}\nModel: {self.model}\nLens: {self.lens}"

