# pylint: disable=import-error
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
from abc import ABC, abstractmethod


class Camera(ABC):
    """
    Camera Abstract Class which has params: brand, model, lens
    """
    def __init__(self, brand, model, lens):
        self.brand = brand
        self.model = model
        self.lens = lens
        self.electronic_matrix = set()

    @abstractmethod
    def take_photo(self):
        pass

    def __iter__(self):
        return iter(self.electronic_matrix)

    def __len__(self):
        return len(self.electronic_matrix)

    def __getitem__(self, index):
        return list(self.electronic_matrix)[index]

    def __str__(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nLens: {self.lens}"
