class Camera:
    def __init__(self, model="", resolution="", zoom=1, memoryCardType="", photosCount=0):
        self.model = model
        self.resolution = resolution
        self.zoom = zoom
        self.memoryCardType = memoryCardType
        self.photosCount = photosCount

    def resetZoom(self):
        self.zoom = 1

    def savePhoto(self):
        self.photosCount += 1

    def eraseMemory(self):
        self.photosCount = 0

    def changeSettings(self, resolution, zoom):
        self.resolution = resolution
        self.zoom = zoom

    def __str__(self):
        return f"Model: {self.model}, Resolution: {self.resolution}, Zoom: {self.zoom}, Memory Card Type: {self.memoryCardType}, Photos Count: {self.photosCount}"

    @staticmethod
    def getInstance():
        if not hasattr(Camera, "_instance"):
            Camera._instance = Camera()
        return Camera._instance


cameras = [Camera(),
           Camera("Canon EOS 5D Mark IV", "6720x4480", 1.5, "CFast 2.0", 100),
           Camera.getInstance(),
           Camera.getInstance()]

for camera in cameras:
    print(camera)
