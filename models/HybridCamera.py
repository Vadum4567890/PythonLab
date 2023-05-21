from Camera import Camera


class HybridCamera(Camera):
    def __init__(self, brand="", model="", lens="", resolution="", zoom=1, memoryCardType="", photosCount=0, fuelType="", batteryLife=0):
        super().__init__(brand, model, lens)
        self.resolution = resolution
        self.zoom = zoom
        self.memoryCardType = memoryCardType
        self.photosCount = photosCount
        self.fuelType = fuelType
        self.batteryLife = batteryLife

    def takePhoto(self):
        return f"Resolution: {self.resolution}, Zoom: {self.zoom}"

    def __str__(self):
        return super().__str__() + f", Resolution: {self.resolution}, Zoom: {self.zoom}, Memory Card Type: {self.memoryCardType}, Photos Count: {self.photosCount}, Fuel Type: {self.fuelType}, Battery Life: {self.batteryLife}"
