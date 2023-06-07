# pylint: disable=too-many-arguments
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=line-too-long
# pylint: disable=import-error

from models.camera import Camera


class HybridCamera(Camera):
    """
    Hybrid Camera Class which have 4 new params: resolution, zoom, memory_card_type, color
    """
    def __init__(self, brand, model, lens, battery_level, resolution, zoom, memory_card_type, color):  # constructor
        super().__init__(brand, model, lens, battery_level)
        self.resolution = resolution
        self.zoom = zoom
        self.memory_card_type = memory_card_type
        self.color = color
        self.electronic_matrix = {"CRD", "CSOS"}

    def charge(self):
        """
        Method to charge the Hybrid camera
        """
        print("Hybrid camera charging...")

    def take_photo(self):
        """
        Method to take a photo
        """
        return f"Hybrid Camera\nResolution: {self.resolution}\nZoom: {self.zoom}\nColor: {self.color}"

    def __str__(self):
        return super().__str__() + f"\nResolution: {self.resolution}\nZoom: {self.zoom}\nColor: {self.color}"
