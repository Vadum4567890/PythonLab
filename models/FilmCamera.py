from Camera import Camera


class FilmCamera(Camera):
    def __init__(self, brand="", model="", lens="", filmType="", filmISO=0):
        super().__init__(brand, model, lens)
        self.filmType = filmType
        self.filmISO = filmISO

    def takePhoto(self):
        return f"Film Type: {self.filmType}, Film ISO: {self.filmISO}"

    def __str__(self):
        return super().__str__() + f", Film Type: {self.filmType}, Film ISO: {self.filmISO}"
