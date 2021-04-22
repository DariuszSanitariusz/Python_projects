from Gameplay import Gameplay

'''
Implemented game of blackjack
'''

game = Gameplay()

game.get_number_of_players()
game.adding_players()

while game.game_on:
    game.everyone_bets()

    gameplay_deck = game.preparing_deck()
    game.starting_hands(gameplay_deck)

    game.dealer_hidden_card()

    for contestant in game.list_of_players:
        game.player_turn = True

        while game.player_turn:
            game.display_table()
            game.player_hit_or_stop(gameplay_deck, contestant)
            contestant.get_hand_value()

            if contestant.hand_value > 21:
                game.player_turn = False

    game.dealer_hidden_card()

    while not game.player_turn:
        game.display_table()
        game.dealer.get_hand_value()
        game.dealer_turn(gameplay_deck)

    game.compare_players_score()

    game.endgame()
    game.leaving_table()
    game.replay()
