import random
from guessing_game import SAVE_FILENAME
import shared

ROULETTE_MIN = 0
ROULETTE_MAX = 36
DEFAULT_CREDIT = 1000
SAVE_FILENAME = 'roulette_save.txt'


def run() -> None:
    credit = get_credit_from_save(SAVE_FILENAME)
    bet_type = -1
    bet_amount = 0

    shared.display_game_name('Roulette')

    while bet_type != 0 and credit > 0:
        secret = random.randint(0, 36)

        display_bet_menu(credit)
        try:
            bet_type = int(input('Choix ? '))
        except:
            bet_type = -1

        if bet_type > 0 and bet_type <= 3:
            bet_amount = ask_for_bet(credit)
            credit -= bet_amount

        print()
        if bet_type == 1:
            # Mise sur PAIR
            if secret % 2 == 0:
                print(f'Le résultat {secret} est PAIR !')
                print('Gagné ! Vous doublez votre mise !')
                credit += bet_amount * 2
            else:
                print(f'Le résultat {secret} est IMPAIR !')
                print(f"C'est Perdu !")

        elif bet_type == 2:
            # Mise sur IMPAIR
            if secret % 2 != 0:
                print(f'Le résultat {secret} est IMPAIR !')
                print('Gagné ! Vous doublez votre mise !')
                credit += bet_amount * 2
            else:
                print(f'Le résultat {secret} est PAIR !')
                print(f"C'est Perdu !")

        elif bet_type == 3:
            # Mise sur NB EXACT
            guess = -1

            while guess < 0 or guess > 36:
                try:
                    guess = int(
                        input(f'Quel numéro choisissez-vous entre {ROULETTE_MIN} et {ROULETTE_MAX} ? '))
                except:
                    guess = -1

                if guess < 0 or guess > 36:
                    print(
                        f'Il faut un numéro compris entre {ROULETTE_MIN} et {ROULETTE_MAX} !\n')

            print(f'Le résultat est {secret} !')
            if guess == secret:
                print('Gagné ! Vous remportez votre mise x10 !!')
                credit += bet_amount * 10
            else:
                print("C'est perdu !")

        elif bet_type == 0:
            print("Merci d'avoir joué !")
        else:
            print('Choix non valide !!')

    if credit <= 0:
        print("Vous n'avez plus d'argent !")
        print("Contactez votre banquier pour qu'il supprime votre save !")

    save_credit(SAVE_FILENAME, credit)


def display_bet_menu(remaining_credit) -> None:
    print()
    print(f'Il vous reste ${remaining_credit}')
    print()
    print('Sur quoi voulez-vous miser ?')
    print('  1 → Pair')
    print('  2 → Impair')
    print('  3 → Nombre Exact')
    print("  0 → Je veux arrêter là.")
    print()


def ask_for_bet(remaining_credit) -> int:
    is_valid_bet = False
    bet_amount = 0

    while not is_valid_bet:
        print()
        try:
            bet_amount = int(input(f'Combien voulez-vouz miser ? '))
        except:
            bet_amount = -1

        if bet_amount > remaining_credit:
            print(f'Vous ne pouvez pas miser plus de ${remaining_credit} !')
        elif bet_amount <= 0:
            print('Il faut miser au moins $1')
        else:
            is_valid_bet = True

    return bet_amount


def get_credit_from_save(filename) -> int:
    try:
        file = open(filename, "r")
        credit = int(file.readline())
    except:
        credit = DEFAULT_CREDIT

    return credit


def save_credit(filename, remaining_credit) -> None:
    try:
        file = open(filename, "w")
        file.write(f'{remaining_credit}')
        file.close()
    except:
        print()
        print(f"Erreur : Impossible d'écrire dans le fichier {SAVE_FILENAME}")
        print(f"Vérifiez qu'il n'est pas utilisé par un autre programme.")
