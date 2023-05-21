from models.camera import Camera


class HybridCamera(Camera):
    def __init__(self, brand, model, lens, resolution, zoom, memory_card_type, color):
        super().__init__(brand, model, lens)
        self.resolution = resolution
        self.zoom = zoom
        self.memory_card_type = memory_card_type
        self.color = color

    def take_photo(self):
        return f"Hybrid Camera\nResolution: {self.resolution}\nZoom: {self.zoom}\nColor: {self.color}"

    def __str__(self):
        return super().__str__() + f"\nResolution: {self.resolution}\nZoom: {self.zoom}\nColor: {self.color}"
