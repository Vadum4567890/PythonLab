from models.Camera import Camera


class FilmCamera(Camera):
    def __init__(self, brand, model, lens, film_type, film_iso):
        super().__init__(brand, model, lens)
        self.film_type = film_type
        self.film_iso = film_iso

    def take_photo(self):
        return f"Film Camera\nFilm Type: {self.film_type}\nFilm ISO: {self.film_iso}"

    def __str__(self):
        return super().__str__() + f"\nFilm Type: {self.film_type}\nFilm ISO: {self.film_iso}"