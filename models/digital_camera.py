# pylint: disable=too-many-arguments
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=import-error
from manager.decorator_manager import RedundantChargeException, DecoratorManager
from models.camera import Camera


class DigitalCamera(Camera):
    """
    Digital Camera Class which has 3 new params: resolution, zoom, memory_card_type
    """

    def __init__(self, brand, model, lens, battery_level,resolution, zoom, memory_card_type):
        super().__init__(brand, model, lens, battery_level)
        self.resolution = resolution
        self.zoom = zoom
        self.memory_card_type = memory_card_type
        self.photos_count = 0
        self.electronic_matrix = {"CCD", "CMOS"}

    def save_photo(self):
        """
        Method to save photo to camera
        """
        self.photos_count += 1

    def erase_memory(self):
        """
        Method to delete all memory
        """
        self.photos_count = 0

    def charge(self):
        """
        Method to charge the digital camera
        """
        print("Digital camera charging...")

    def change_settings(self, resolution, zoom):
        """
        Method to change resolution and zoom
        """
        self.resolution = resolution
        self.zoom = zoom

    def take_photo(self):
        """
        Method to take a photo
        """
        return f"Digital Camera\nResolution: {self.resolution}\nZoom: {self.zoom}"

    def __str__(self):
        return super().__str__() + f"\nResolution: {self.resolution}\nZoom: {self.zoom}"
