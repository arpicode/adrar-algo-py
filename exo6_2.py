# Exercice 6.2 :

# Ecrire un script qui déclare une liste de 9 notes, dont on fait ensuite saisir les valeurs par
# l’utilisateur. Le script affichera ensuite la moyenne de ces neuf notes.

MAX_GRADES = 9

gradeList = [None] * MAX_GRADES

for i in range(0, MAX_GRADES):
    gradeList[i] = float(input(f'Saisir la note #{i + 1} : '))

print(f'Moyenne des notes : {round(sum(gradeList) / MAX_GRADES, 2)}')
