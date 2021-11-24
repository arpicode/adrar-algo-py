# Exercice 6.5 :

# Créer un programme qui permette de gérer une liste de course. Il doit permettre de :
# 1) Ajouter un élément à la liste de courses
# 2) Retirer un élément de la liste de courses
# 3) Afficher la liste de courses
COLOR_BLUE = '\33[94m'
COLOR_RED = '\033[31m'
COLOR_YELLOW = '\33[33m'
COLOR_GREEN = '\033[92m'
COLOR_END = '\033[0m'
BOLD = '\33[1m'
shoppingList = []

choice = ''

while choice != 4:
    print(f"\n{COLOR_BLUE}Choisir une d'action :{COLOR_END}")
    print(f'  {BOLD}1{COLOR_END} → Ajouter un élément.')
    print(f'  {BOLD}2{COLOR_END} → Retirer un élément.')
    print(f'  {BOLD}3{COLOR_END} → Afficher la liste de courses.')
    print(f'  {BOLD}4{COLOR_END} → Terminer la saisie.\n')
    choice = int(input(f"Action N° ? "))
    print()

    if (choice == 1):
        # Ajouter un élément
        shoppingList.append(input("Saisir l'élément à rajouter : "))
        print(
            f'{COLOR_GREEN}+{COLOR_END} {shoppingList[-1]} ajouté à la liste')

    elif (choice == 2):
        # Retirer un élément
        if (len(shoppingList) == 0):
            print(f"{COLOR_YELLOW}La liste est vide !{COLOR_END}")
        else:
            item = input("Saisir l'élément à supprimer : ")
            if shoppingList.count(item) != 0:
                shoppingList.remove(item)
                print(f'{COLOR_RED}-{COLOR_END} {item} supprimer de la liste')
            else:
                print(f"❌ {item} n'est pas dans la liste !")

    elif (choice == 3):
        # Afficher la liste
        print(f'{COLOR_BLUE}Contenu de la liste :{COLOR_END}\n{shoppingList}')

    elif (choice == 4):
        # Quitter
        print(f'{COLOR_YELLOW}Liste terminée, bon shopping !{COLOR_END}')
    else:
        print("❌ Cette action n'existe pas !")
