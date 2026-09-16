class GameClass:
    def __init__(self, name, year, genre, rating):
        self.name = name
        self.year = year
        self.genre = genre
        self.rating = rating

    # __str__ anropas automatiskt och gör om objektet till en sträng 
    def __str__(self):
        # eftersom genre är en lista sätter jag ihop listan till en sträng med .join().
        # annars ser det så fult ut när den printas
        return f"- {self.name} {self.year} {', '.join(self.genre)} {self.rating}/10"