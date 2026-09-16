class GameClass:
    def __init__(self, name, year, genre, rating):
        self.name = name
        self.year = year
        self.genre = genre
        self.rating = rating

    def __str__(self):
        return f"- {self.name} {self.year} {', '.join(self.genre)} {self.rating}/10"