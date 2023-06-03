# pylint: disable=import-error
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
from abc import ABC, abstractmethod
from manager.decorator_manager import DecoratorManager, RedundantChargeException


class Camera(ABC):
    """
    Camera Abstract Class which has params: brand, model, lens
    """

    def __init__(self, brand, model, lens, battery_level):
        self.brand = brand
        self.model = model
        self.lens = lens
        self.battery_level = battery_level
        self.electronic_matrix = set()

    @abstractmethod
    def take_photo(self):
        pass

    @abstractmethod
    def charge(self):
        pass

    @DecoratorManager.logged("file")
    def default_charge(self):
        if self.battery_level == 100:
            raise RedundantChargeException("The camera battery is already fully charged.")
        else:
            self.battery_level += 10
            print("Charging...")

    def __iter__(self):
        return iter(self.electronic_matrix)

    def __len__(self):
        return len(self.electronic_matrix)

    def __getitem__(self, index):
        return list(self.electronic_matrix)[index]

    def __str__(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nLens: {self.lens}\nBattery level: {self.battery_level}"

