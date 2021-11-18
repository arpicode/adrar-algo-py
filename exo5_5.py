# Exercice 5.5 :

# Ecrire un script qui demande un nombre de départ, et qui ensuite écrit la table de multiplication
# de ce nombre, présentée comme suit (cas où l'utilisateur entre le nombre 7) :
#
# Table de 7 :
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# …
# 7 x 10 = 70

times_table = int(input('Entrer la table de multiplication : '))

print(f'Table de {times_table} :')

for i in range(1, 10 + 1):
    print(f'{times_table} x {i} = {times_table * i}')
