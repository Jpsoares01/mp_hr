import time
import random
import os

def print_race(horses):
    os.system('cls' if os.name == 'nt' else 'clear')

    print("=" * 50)
    for horse in horses:
        print(f"{horse.name: >8}: {' ' * horse.position}{'*' if horse.position < 30 else '-'}")
    print("=" * 50)
    time.sleep(0.7)


def race(horses):
    distance = 30
    winner = None

    while not winner:
        for horse in horses:
            horse.position += horse.velocity
            horse.movement()
            if horse.position >= distance:
                winner = horse.name
                break
        print_race(horses)

    for horse in horses:
        horse.position = 0
        horse.stamina = random.randint(10, 40)
        horse.control = random.randint(1, 10)
        horse.speed = random.randint(1, 10)
        horse.strength = random.randint(1, 10)

    return winner
