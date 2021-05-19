from Gameplay import Gameplay

'''
Implemented game of blackjack
'''

if __name__ == '__main__':
    game = Gameplay()

    game.get_number_of_players()
    game.adding_players()

    while game.game_on:
    game.everyone_bets()

    game.preparing_deck()
    game.starting_hands(game.deck)

    game.dealer_hidden_card()

    for contestant in game.list_of_players:
        game.player_turn = True

        while game.player_turn:
            game.display_table()
            game.player_hit_or_stop(game.deck, contestant)
            contestant.bust_check()

            if contestant.hand_value > 21:
                game.player_turn = False

    game.dealer_hidden_card()

    while not game.player_turn:
        game.display_table()
        game.dealer_turn(game.deck)

    game.compare_players_score()

    game.endgame()
    game.leaving_table()
    game.replay()
