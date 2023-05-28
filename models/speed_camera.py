# pylint: disable=too-many-arguments
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=line-too-long
# pylint: disable=import-error
from models.camera import Camera


class SpeedCamera(Camera):
    """
    Hybrid Camera Class which have 2 new params: max_speed_detection, price
    """
    def __init__(self, brand, model, lens, max_speed_detection, price):              # constructor
        super().__init__(brand, model, lens)
        self.max_speed_detection = max_speed_detection
        self.price = price
        self.electronic_matrix = {"FSD", "ASFE"}

    def take_photo(self):
        """
        Method to take a photo
        """
        return f"Speed Camera\nMax Speed Detection: {self.max_speed_detection} km/h\nPrice: {self.price}"

    def __str__(self):
        return super().__str__() + f"\nMax Speed Detection: {self.max_speed_detection} km/h\nPrice: {self.price}"
