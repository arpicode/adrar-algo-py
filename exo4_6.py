# Exercice 4.6 : La Logique :

# Les élections législatives, obéissent à la règle suivante :
#  • lorsque l'un des candidats obtient plus de 50% des suffrages, il est élu dès le premier tour.
#  • en cas de deuxième tour, peuvent participer uniquement les candidats ayant obtenu au moins
#    12,5% des voix au premier tour.
#
# Vous devez écrire un script qui permette la saisie des scores de quatre candidats au premier tour.
# Ce script traitera ensuite le candidat numéro 1 (et uniquement lui) : il dira s'il est élu, battu,
# s'il se trouve en ballottage favorable (il participe au second tour en étant arrivé en tête à
# l'issue du premier tour) ou défavorable (il participe au second tour sans avoir été en tête au
# premier tour). (modifié)

print('Les scores doivent être saisis en % sans symbole (ex: 55.3 pour 55.3%)')

candidate1_score = float(input('Saisissez le score du 1er candidat : '))
candidate2_score = float(input('Saisissez le score du 2ème candidat : '))
candidate3_score = float(input('Saisissez le score du 3ème candidat : '))
candidate4_score = float(input('Saisissez le score du 4ème candidat : '))

if (candidate1_score > 50):
    print('Le candidat n°1 est élu au 1er tour ! =)')

elif (candidate1_score < 12.5 or
      candidate2_score > 50 or
      candidate3_score > 50 or
      candidate4_score > 50):
    print("Le candidat n°1 est battu... :'(")

elif (candidate1_score >= 12.5 and
      (candidate1_score >= candidate2_score and
       candidate1_score >= candidate3_score and
       candidate1_score >= candidate4_score)):
    print('Le candidat est en ballottage favorable.')

else:
    print('Le candidat est en ballottage défavorable.')

# Rq.: En cas d'ex aequo le candidat 1 sera encore considéré comme favorable
