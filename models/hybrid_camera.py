from models.camera import Camera


class HybridCamera(Camera):
    """
    Hybrid Camera Class which have 4 new params: resolution, zoom, memory_card_type, color
    """
    def __init__(self, brand, model, lens, resolution, zoom, memory_card_type, color):  # constructor
        super().__init__(brand, model, lens)
        self.resolution = resolution
        self.zoom = zoom
        self.memory_card_type = memory_card_type
        self.color = color

    def take_photo(self):                                                               # To String take_photo
        return f"Hybrid Camera\nResolution: {self.resolution}\nZoom: {self.zoom}\nColor: {self.color}"

    def __str__(self):                                                                  # To String class Hybrid Camera
        return super().__str__() + f"\nResolution: {self.resolution}\nZoom: {self.zoom}\nColor: {self.color}"
