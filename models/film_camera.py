# pylint: disable=too-many-arguments
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=import-error
from models.camera import Camera


class FilmCamera(Camera):
    """
    Film Camera Class which have 2 new params: film_type, film_iso
    """
    def __init__(self, brand, model, lens, film_type, film_iso):         # constructor
        super().__init__(brand, model, lens)
        self.film_type = film_type
        self.film_iso = film_iso
        self.electronic_matrix = {"CMD", "CMOS"}

    def take_photo(self):
        """
        Method to take a photo
        """
        return f"Film Camera\nFilm Type: {self.film_type}\nFilm ISO: {self.film_iso}"

    def __str__(self):                                          # To String class Film Camera
        return super().__str__() + f"\nFilm Type: {self.film_type}\nFilm ISO: {self.film_iso}"
