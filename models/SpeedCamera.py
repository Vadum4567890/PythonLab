from Camera import Camera


class SpeedCamera(Camera):
    def __init__(self, brand="", model="", lens="", resolution="", zoom=1, speedRange="", maxSpeedCaptured=0):
        super().__init__(brand, model, lens)
        self.resolution = resolution
        self.zoom = zoom
        self.speedRange = speedRange
        self.maxSpeedCaptured = maxSpeedCaptured

    def takePhoto(self):
        return f"Resolution: {self.resolution}, Zoom: {self.zoom}, Speed Range: {self.speedRange}"

    def __str__(self):
        return super().__str__() + f", Resolution: {self.resolution}, Zoom: {self.zoom}, Speed Range: {self.speedRange}, Max Speed Captured: {self.maxSpeedCaptured}"
