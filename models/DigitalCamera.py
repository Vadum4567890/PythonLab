from models.Camera import Camera


class DigitalCamera(Camera):
    def __init__(self, brand, model, lens, resolution, zoom, memory_card_type):
        super().__init__(brand, model, lens)
        self.resolution = resolution
        self.zoom = zoom
        self.memory_card_type = memory_card_type
        self.photos_count = 0

    def save_photo(self):
        self.photos_count += 1

    def erase_memory(self):
        self.photos_count = 0

    def change_settings(self, resolution, zoom):
        self.resolution = resolution
        self.zoom = zoom

    def take_photo(self):
        return f"Digital Camera\nResolution: {self.resolution}\nZoom: {self.zoom}"

    def __str__(self):
        return super().__str__() + f"\nResolution: {self.resolution}\nZoom: {self.zoom}"
