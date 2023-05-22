from models.camera import Camera


class DigitalCamera(Camera):
    """
    Digital Camera Class which have 3 new params: resolution, zoom, memory_card_type
    """
    def __init__(self, brand, model, lens, resolution, zoom, memory_card_type):   # constructor
        super().__init__(brand, model, lens)
        self.resolution = resolution
        self.zoom = zoom
        self.memory_card_type = memory_card_type
        self.photos_count = 0

    def save_photo(self):                               # method which save photo to camera
        self.photos_count += 1

    def erase_memory(self):                            # method which delete all memory
        self.photos_count = 0

    def change_settings(self, resolution, zoom):       # method which changes resolution and zoom
        self.resolution = resolution
        self.zoom = zoom

    def take_photo(self):                              # To String take_photo
        return f"Digital Camera\nResolution: {self.resolution}\nZoom: {self.zoom}"

    def __str__(self):                                 # To String class Digital Camera
        return super().__str__() + f"\nResolution: {self.resolution}\nZoom: {self.zoom}"
