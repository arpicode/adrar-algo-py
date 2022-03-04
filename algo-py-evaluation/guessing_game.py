import random
import csv
from datetime import datetime
import shared

NUM_MIN = 1
NUM_MAX = 1000
NUM_TRIES_MAX = 10

# Save au format CSV avec 3 colonnes :
#   ► col 1 : date et heure de la partie.
#   ► col 2 : nombre de coup(s) utilisé(s) ou 0 si le secret n'a pas été trouvé.
#   ► col 3 : secret qu'il fallait trouver.
SAVE_FILENAME = 'guessing_game_save.csv'


def run() -> None:
    secret = random.randint(NUM_MIN, NUM_MAX)
    guess = -1
    tries = 0

    shared.display_game_name('Devinez le Nombre')

    while guess != secret:
        if tries < NUM_TRIES_MAX:
            display_remaining_tries(tries)
            guess = ask_for_number_to_guess()
            tries += 1

            print()
            if guess < secret:
                print(f'Le nombre {guess} est trop petit !')
            elif guess > secret:
                print(f'Le nombre {guess} est trop grand !')
            else:
                print(f'Bravo, {secret} était le nombre secret !')
                print(f"Vous l'avez trouvé en {tries} coup{plural(tries)} !")

        else:
            print(
                f'Vous avez utilisé tous vos essais ! Le nombre secret était {secret}.')
            tries = 0
            break

    save_result(SAVE_FILENAME, tries, secret)


def display_remaining_tries(current_guess_count) -> None:
    remaining_tries = NUM_TRIES_MAX - current_guess_count
    print()
    print(f"Il vous reste {remaining_tries} essai{plural(remaining_tries)}.")


def ask_for_number_to_guess() -> int:
    is_guess_valid = guess = False

    while not is_guess_valid:
        try:
            print()
            guess = int(
                input(f'Choisisser un nombre entre {NUM_MIN} et {NUM_MAX} : '))
            is_guess_valid = True
        except:
            print(
                f'Erreur : Vous devez choisir un nombre entre {NUM_MIN} et {NUM_MAX} !')

    return guess


def plural(number) -> str:
    if number > 1:
        return 's'
    return ''


def get_date() -> str:
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')


def save_result(filename, tries_count, secret) -> None:
    try:
        with open(filename, 'a', newline='', encoding='UTF-8') as csvfile:
            filewriter = csv.writer(
                csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

            filewriter.writerow([get_date(), tries_count, secret])
    except:
        print()
        print(f"Erreur : Impossible d'écrire dans le fichier {SAVE_FILENAME}")
        print(f"Vérifiez qu'il n'est pas utilisé par un autre programme.")
