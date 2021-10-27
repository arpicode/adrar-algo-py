# Exercice 4.4 : La Logique :

# Un magasin de reprographie facture 0,10 € les dix premières photocopies, 0,09 € les vingt
# suivantes et 0,08€ au-delà.
# Ecrivez un script qui demande à l’utilisateur le nombre de photocopies effectuées et qui affiche
# la facture correspondante.

num_copies = int(input('Nombre de photocopie(s) à effectuer ? '))

HIGH_PRICE = .1
MEDIUM_PRICE = .09
LOW_PRICE = .08

if (num_copies <= 10):
    total_price = num_copies * HIGH_PRICE
elif (num_copies <= 30):
    total_price = 10 * HIGH_PRICE + (num_copies - 10) * MEDIUM_PRICE
else:
    total_price = 10 * HIGH_PRICE + \
        (30 - 10) * MEDIUM_PRICE + (num_copies - 30) * LOW_PRICE

print(f'Prix à payer : {round(total_price, 2)} €')
