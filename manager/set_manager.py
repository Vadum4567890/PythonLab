# pylint: disable=missing-module-docstring
class SetManager:
    """
    The SetManager class is a wrapper class that provides additional functionality
    for managing a collection of cameras. It is designed to work with an existing
    regular_manager object that represents a collection of cameras.
    """
    def __init__(self, regular_manager):
        self.index = 0
        self.regular_manager = regular_manager

    def __iter__(self):
        return self

    def __len__(self):
        count = 0
        for camera in self.regular_manager:
            count += len(camera.electronic_matrix)
        return count

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError("SetManager index out of range")
        for camera in self.regular_manager:
            if index < len(camera.electronic_matrix):
                return list(camera.electronic_matrix)[index]
            index -= len(camera.electronic_matrix)
        return None

    def __next__(self):
        if self.index >= len(self.regular_manager):
            raise StopIteration("Iteration was stopped")
        item = self.regular_manager[self.index]
        self.index += 1
        return item
