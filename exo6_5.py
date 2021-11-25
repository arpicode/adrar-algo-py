# Exercice 6.5 :

# Créer un programme qui permette de gérer une liste de course. Il doit permettre de :
# 1) Ajouter un élément à la liste de courses
# 2) Retirer un élément de la liste de courses
# 3) Afficher la liste de courses

COLOR_BLACK = '\033[30m'
COLOR_GRAY = '\033[90m'
COLOR_RED = '\033[31m'
COLOR_LIGHT_RED = '\033[91m'
COLOR_GREEN = '\033[32m'
COLOR_LIGHT_GREEN = '\033[92m'
COLOR_YELLOW = '\033[33m'
COLOR_LIGHT_YELLOW = '\033[93m'
COLOR_BLUE = '\033[34m'
COLOR_LIGHT_BLUE = '\033[94m'
COLOR_MAGENTA = '\033[35m'
COLOR_LIGHT_MAGENTA = '\033[95m'
COLOR_CYAN = '\033[36m'
COLOR_LIGHT_CYAN = '\033[96m'
COLOR_END = '\033[0m'
BOLD = '\033[1m'
MSG_ERROR = '\033[30m\033[41m ERROR \033[0m'
MSG_SUCCESS = '\033[30m\033[42m SUCCESS \033[0m'
MSG_WARNING = '\033[30m\033[43m WARNING \033[0m'
CHECK = '\033[32m✔\033[0m'
CROSS = '\033[31m✘\033[0m'

shoppingList = []
choice = ''

while choice != 4:
    print()
    print(f"{COLOR_LIGHT_CYAN}Choisir une d'action :{COLOR_END}")
    print()
    print(f'\t{BOLD}1{COLOR_END} → Ajouter un élément.')
    print(f'\t{BOLD}2{COLOR_END} → Retirer un élément.')
    print(f'\t{BOLD}3{COLOR_END} → Afficher la liste de courses.')
    print(f'\t{BOLD}4{COLOR_END} → Terminer la saisie.')
    print()

    try:
        choice = int(input(f"\t{COLOR_LIGHT_CYAN}Action N° ? {COLOR_END}"))
    except:
        choice = 0

    print()
    if (choice == 1):
        # Ajouter un élément
        shoppingList.append(input("Saisir l'élément à rajouter : "))
        print()
        print(f'{CHECK} {BOLD}{shoppingList[-1]}{COLOR_END} ajouté à la liste')

    elif (choice == 2):
        # Retirer un élément
        if (len(shoppingList) == 0):
            print(f"{MSG_WARNING} La liste est vide ! Aucun élément à supprimer.")
        else:
            item = input("Saisir l'élément à supprimer : ")
            print()
            if shoppingList.count(item) != 0:
                shoppingList.remove(item)
                print(f'{CROSS} {item} supprimer de la liste')
            else:
                print(f"{MSG_WARNING} {item} n'est pas dans la liste !")

    elif (choice == 3):
        # Afficher la liste
        print('Contenu de la liste :')
        print(f'{COLOR_LIGHT_GREEN}{shoppingList}{COLOR_END}')

    elif (choice == 4):
        # Quitter
        print(f'{COLOR_LIGHT_MAGENTA}Liste terminée, bon shopping !{COLOR_END}')
    else:
        print(f"{MSG_ERROR} Cette action n'existe pas !")
