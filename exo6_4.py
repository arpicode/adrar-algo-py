# Exercice 6.4 :

# La liste suivante représenta les moyennes d’une classe
# moyennes = [14.84,14.14,16.22,86,85,85,14.84,13,15.85,9.99,12.04,15.03,16.22,12,84,10.20,11.03,11.03]
# Afficher les trois bonnes moyennes (Les 3 plus hautes entre 0 et 20)
# Afficher les trois mauvaises moyennes (Les 3 plus mauvaises entre 0 et 20)(triées de plus petites au plus grandes)

moyennes = [14.84, 14.14, 16.22, 86, 85, 85, 14.84, 13, 15.85,
            9.99, 12.04, 15.03, 16.22, 12, 84, 10.20, 11.03, 11.03]

moyennes = [note for note in moyennes if 0 <= note <= 20]

moyennes.sort()

print(f'Les 3 meilleurs moyennes : {moyennes[-3:]}')
print(f'Les 3 moins bonnes moyennes : {moyennes[:3]}')
