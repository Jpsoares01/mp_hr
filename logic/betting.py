def place_bets(players, horses):
    horse_names = [horse.name for horse in horses]

    for player in players:
        print(f"\n{player.name}'s turn:")
        print(f'Available money: {player.money}€')
        print('Horses: ', horse_names)

        while True:
            bet = input('Choose a horse to bet on: ').lower()
            if bet in horse_names:
                player.horse_bet = bet
                break
            print('Invalid horse name. Please choose again.')

        while True:
            try:
                amount = int(input('Enter the bet amount: €'))
                if 0 < amount <= player.money:
                    player.bet_amount = amount
                    break
                else:
                    print('Invalid bet amount.')
            except ValueError:
                print("Invalid input. Please enter a valid number.")
