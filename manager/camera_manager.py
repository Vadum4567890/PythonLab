"""This module defines a CameraManager class that represents a manager for cameras"""
# pylint: disable=line-too-long
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=import-error

from models.digital_camera import DigitalCamera
from models.film_camera import FilmCamera
from models.hybrid_camera import HybridCamera
from models.speed_camera import SpeedCamera
from manager.decorator_manager import DecoratorManager
from manager.set_manager import SetManager


class CameraManager:
    """
    The CameraManager class provides methods to manage a collection of cameras.
    It supports adding cameras, finding cameras based on brand or model,
    retrieving results of camera methods, accessing cameras by index, iterating over cameras, and more.
    """
    def __init__(self):
        self.cameras = []

    def __str__(self):
        return "\n".join(str(camera) for camera in self.cameras)

    def __len__(self):
        return len(self.cameras)

    def __getitem__(self, index):
        return self.cameras[index]

    def __iter__(self):
        return iter(self.cameras)

    def add_camera(self, camera):
        self.cameras.append(camera)

    @DecoratorManager.method_name_decorator
    @DecoratorManager.argument_count_decorator
    def find_all_with_same_brand(self, brand):
        return [camera for camera in self.cameras if camera.brand == brand]

    @DecoratorManager.method_name_decorator
    @DecoratorManager.save_result_decorator
    def find_all_with_same_model(self, model):
        return [cam for cam in self.cameras if cam.model == model]

    @DecoratorManager.method_name_decorator
    @DecoratorManager.call_count_decorator
    def get_results_of_method(self, method_name):
        return [getattr(camera, method_name)() for camera in self.cameras]

    @DecoratorManager.method_name_decorator
    @DecoratorManager.call_limit_decorator
    def get_enumerated_objects(self):
        return list(enumerate(self.cameras))

    @DecoratorManager.method_name_decorator
    @DecoratorManager.save_result_decorator
    def get_zip_results(self, method_name):
        return [(camera, getattr(camera, method_name)()) for camera in self.cameras]

    def get_attributes_by_type(self, data_type):
        return {k: v for camera in self.cameras for k, v in camera.__dict__.items() if isinstance(v, data_type)}

    def check_all_and_any(self, condition):
        return {"all": all(condition(camera) for camera in self.cameras),
                "any": any(condition(camera) for camera in self.cameras)}


manager = CameraManager()

digital_camera1 = DigitalCamera("Canon", "XP", "18-55mm", "1024x768", 2.0, "SD")
film_camera1 = FilmCamera("Canon", "F1", "50mm", "35mm", 200)
hybrid_camera1 = HybridCamera("Sony", "A7 III", "24-70mm", "6240x4160", 3.0, "SD", "Black")
speed_camera1 = SpeedCamera("Hikvision", "DS-2CD2643G0-IZS", "Strong", 100, 500)

manager.add_camera(digital_camera1)
manager.add_camera(film_camera1)
manager.add_camera(hybrid_camera1)
manager.add_camera(speed_camera1)

set_manager = SetManager(manager)

print("Number of items in SetManager:", len(set_manager))
print("Iterating through SetManager:")
for item in set_manager:
    print(item)
print("Accessing item at index 2:", set_manager[2])

print("\n\n\n")

results = manager.get_results_of_method("take_photo")
enumerated_objects = manager.get_enumerated_objects()
zip_results = manager.get_zip_results("take_photo")
attributes_by_type = manager.get_attributes_by_type(int)
all_and_any = manager.check_all_and_any(lambda x: len(x.model) > 0)

print("Results:", results)
print("Enumerated Objects:", enumerated_objects)
print("Zip Results:", zip_results)
print("Attributes by Type:", attributes_by_type)
print("All and Any:", all_and_any)

print("\n\n\n")
print("Cameras with brand 'Canon':")
for cam in manager.find_all_with_same_brand("Canon"):
    print(cam)

print("\nCameras with model 'XP':")
for cam in manager.find_all_with_same_model("XP"):
    print(cam)
