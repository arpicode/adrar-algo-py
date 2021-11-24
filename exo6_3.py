# Exercice 6.3 :

# Ecrivez un script permettant à l’utilisateur de saisir un nombre quelconque de valeurs, qui
# devront être stockées dans un liste. L’utilisateur doit donc commencer par entrer le nombre de
# valeurs qu’il compte saisir. Il effectuera ensuite cette saisie. Enfin, une fois la saisie
# terminée, le programme affichera le nombre de valeurs négatives et le nombre de valeurs positives.

numValue = int(input('Saisir le nombre de valeurs : '))
myList = []
numPositiveValues = 0

for i in range(0, numValue):
    myList.append(int(input(f'Saisir la valeur #{i + 1} : ')))
    if (myList[-1] >= 0):
        numPositiveValues += 1

print(f'Il y a {numPositiveValues} valeur(s) positive(s) et {numValue - numPositiveValues} négative(s).')
