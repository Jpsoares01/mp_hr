import random

class Horse:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.velocity = 0
        self.stamina = random.randint(10, 40)
        self.control = random.randint(1, 10)
        self.speed = random.randint(1, 10)
        self.strength = random.randint(1, 10)

    def movement(self):
        self.velocity = int(self.speed * 0.5 + self.strength * 0.3 + self.control * 0.2)
        self.stamina -= random.randint(5, 10)
        if self.stamina <= 0:
            self.velocity //= 2
            