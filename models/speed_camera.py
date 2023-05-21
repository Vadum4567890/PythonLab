from models.camera import Camera


class SpeedCamera(Camera):
    def __init__(self, brand, model, lens, max_speed_detection, price):
        super().__init__(brand, model, lens)
        self.max_speed_detection = max_speed_detection
        self.price = price

    def take_photo(self):
        return f"Speed Camera\nMax Speed Detection: {self.max_speed_detection} km/h\nPrice: {self.price}"

    def __str__(self):
        return super().__str__() + f"\nMax Speed Detection: {self.max_speed_detection} km/h\nPrice: {self.price}"
