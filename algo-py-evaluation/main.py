import guessing_game
import roulette_game

game_choice = -1

while game_choice != 0:
    print('\nJeux disponibles :\n')
    print('\t1 → Devinez le Nombre')
    print('\t2 → Roulette')
    print('\t0 → Quitter\n')

    try:
        game_choice = int(input('À quel jeu voulez-vous jouer ? '))
    except:
        game_choice = -1

    if game_choice == 1:
        guessing_game.run()
    elif game_choice == 2:
        roulette_game.run()
    elif game_choice == 0:
        print('\nÀ bientôt !')
    else:
        print('Choix non valide !!')
