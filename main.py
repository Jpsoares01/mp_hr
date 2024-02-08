import time
from models.horse import Horse
from models.player import Player
from logic.race import race
from logic.betting import place_bets
from utils.utils import get_valid_int

def game():
    horse_names = ['carrots', 'thunder', 'winter', 'hercules', 'buster']
    horses = [Horse(name) for name in horse_names]

    number_of_players = get_valid_int('Enter the number of players: ', condition=lambda x: x > 0, error_msg='Number of players must be greater than 0.')
    buy_in_amount = get_valid_int('Enter the Buy-in: ', condition=lambda x: x > 0, error_msg='Buy-in must be greater than 0.')

    players = [Player(input(f"Enter Player {i + 1}'s name: "), buy_in_amount) for i in range(number_of_players)]

    while all(player.money > 0 for player in players):
        print('\nHorse attributes:')
        for horse in horses:
            print(f'{horse.name}: Stamina - {horse.stamina}, Control - {horse.control}, '
                  f'Speed - {horse.speed}, Strength - {horse.strength}')

        place_bets(players, horses)
        winner = race(horses)

        print(f'\nThe winner is: {winner}')

        for player in players:
            if player.horse_bet == winner.lower():
                print(f'\n{player.name} won {player.bet_amount * 2}€!')
                player.money += player.bet_amount
            else:
                print(f'\n{player.name} lost {player.bet_amount}€.')
                player.money -= player.bet_amount

            print(f"{player.name}'s remaining money: {player.money}€")
            player.bet_amount = 0
            time.sleep(0.7)

        players = [p for p in players if p.money > 0]

        if len(players) <= 1:
            print(f'\nCongratulation, {players[0].name}, you won.')
            break


if __name__ == "__main__":
    game()
