#Classes for the bowling score and league tracker

class Game:
    def __init__(self, score):
        if type(score) is not int:
            pass