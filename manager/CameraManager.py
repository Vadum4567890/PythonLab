from models.DigitalCamera import DigitalCamera
from models.FilmCamera import FilmCamera
from models.HybridCamera import HybridCamera
from models.SpeedCamera import SpeedCamera


class CameraManager:
    def __init__(self):
        self.cameras = []

    def addCamera(self, camera):
        self.cameras.append(camera)

    def findAllWithSameBrand(self, brand):
        return [camera for camera in self.cameras if getattr(camera, 'brand', None) == brand]

    def findAllWithSameModel(self, model):
        return [camera for camera in self.cameras if getattr(camera, 'model', None) == model]


manager = CameraManager()
manager.addCamera(DigitalCamera("Canon EOS 5D Mark IV", "Canon", "6720x4480", 1.5, "CFast 2.0", 100))
manager.addCamera(FilmCamera("Nikon FM2", "Nikon", "35mm", "ISO 400"))
manager.addCamera(SpeedCamera("Nikon FM2", "Nikon", "35mm", "ISO 400"))
manager.addCamera(HybridCamera("Nikon FM2", "Nikon", "35mm", "ISO 400"))

print("Cameras with brand 'Canon EOS 5D Mark IV':")
for camera in manager.findAllWithSameBrand("Canon EOS 5D Mark IV"):
    print(camera)

print("Cameras with model 'Nikon':")
for camera in manager.findAllWithSameModel("Nikon"):
    print(camera)
