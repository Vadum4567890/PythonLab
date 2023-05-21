from abc import ABC, abstractmethod


class Camera(ABC):
    def __init__(self, brand, model, lens):
        self.brand = brand
        self.model = model
        self.lens = lens

    @abstractmethod
    def take_photo(self):
        pass

    def __str__(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nLens: {self.lens}"

