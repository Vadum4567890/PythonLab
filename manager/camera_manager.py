from models.digital_camera import DigitalCamera
from models.film_camera import FilmCamera
from models.hybrid_camera import HybridCamera
from models.speed_camera import SpeedCamera


class CameraManager:
    def __init__(self):
        self.cameras = []

    def add_camera(self, camera):
        self.cameras.append(camera)

    def find_all_with_same_brand(self, brand):
        return [camera for camera in self.cameras if camera.brand == brand]

    def find_all_with_same_model(self, model):
        return [camera for camera in self.cameras if camera.model == model]

    def __str__(self):
        return "\n".join(str(camera) for camera in self.cameras)


manager = CameraManager()

digital_camera1 = DigitalCamera("Canon", "XP", "18-55mm", "1024x768", 2.0, "SD")
film_camera1 = FilmCamera("Canon", "F1", "50mm", "35mm", 200)
hybrid_camera1 = HybridCamera("Sony", "A7 III", "24-70mm", "6240x4160", 3.0, "SD", "Black")
speed_camera1 = SpeedCamera("Hikvision", "DS-2CD2643G0-IZS", "Varifocal", 100, 500)

manager.add_camera(digital_camera1)
manager.add_camera(film_camera1)
manager.add_camera(hybrid_camera1)
manager.add_camera(speed_camera1)

print("Cameras with brand 'Canon':")
for camera in manager.find_all_with_same_brand("Canon"):
    print(camera)

print("\nCameras with model 'XP':")
for camera in manager.find_all_with_same_model("XP"):
    print(camera)
