# Exercice 2

# Même exercice, mais en incluant l'ajout de la TVA. Cette fois le script demande à l'utilisateur le
# nombre de boites de chocolats, le prix unitaire, et le taux de TVA.

chocolate_box_price = float(input('Prix de la boîte de chocolat ? '))
box_num = float(input('Combien de boîte désires-tu ? '))
vat_rate = float(input('% TVA : ')) / 100 + 1

print(f'Prix total : { round(chocolate_box_price * box_num * vat_rate, 2) } €')
