# Exercice 4.3

# De même que le précédent, ce script doit demander une heure et en afficher une autre. Mais cette
# fois, il doit gérer également les secondes, et afficher l'heure qu'il sera une seconde plus tard.
# Par exemple, si l'utilisateur tape 21, puis 32, puis 8, le script doit répondre :
# "Dans une seconde, il sera 21 heure(s), 32 minute(s) et 9 seconde(s)".
#
# NB : là encore, on suppose que l'utilisateur entre une date valide.

hours = int(input('Entrez les heures : '))
minutes = int(input('Entrez les minutes : '))
seconds = int(input('Entrez les secondes : '))

next_seconds = (seconds + 1) % 60

if (next_seconds == 0):
    minutes = (minutes + 1) % 60
    if (minutes == 0):
        hours = (hours + 1) % 24

print(
    f'Dans une seconde, il sera {hours} heure(s) {minutes} minute(s) {next_seconds} seconde(s)')
