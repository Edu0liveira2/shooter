class Player:
    def __init__(self, health, position):
        self.health = 100
        self.position = (0, 0)

    def is_alive(self):
        return self.health > 0
