# Exercice 1

# Au supermarché il y a une promotion sur les pommes, 1,20€ la pomme seulement !
# Ecrire un script qui demande à l'utilisateur combien de pommes il désire et qui lui donne le prix
# total.

apple_price = 1.2
num_apple = float(input('Combien de pommes désires-tu ? '))
print(f'Prix total : { round(apple_price * num_apple, 2) } €')
