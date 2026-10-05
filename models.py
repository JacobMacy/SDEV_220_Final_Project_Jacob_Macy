#Classes for the bowling score and league tracker

class Game:
    
    def __init__(self, score):
        if type(score) is not int or  not 0 <= score <= 300:
            raise ValueError("Score must be a whole number from 0 to 300")
        self.score = score

class Bowler:

    def __init__(self, name):
        name = name.strip()
        if not name:
            raise ValueError("Enter a bowler's name.")
        self.name = name
        self.games = []

    def add_game(self, score):
        self.games.append(Game(score))

    def average(self):
        if not self.games:
            return 0.0
        return sum(game.score for game in self.games) / len(self.games)

class League:

    def __init__(self, name):
        name = name.strip()
        if not name:
            raise ValueError("Enter a league name.")
        self.name = name
        self.bowlers = {}
        self.next_id = 1

    def add_bowler(self, name):
        bowler = Bowler(name)
        bowler_id = self.next_id
        self.bowlers[bowler_id] = bowler
        self.next_id += 1
        return bowler_id