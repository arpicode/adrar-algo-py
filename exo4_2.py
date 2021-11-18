# Exercice 4.2

# Ce script lira au clavier l’heure et les minutes, et il affichera l’heure qu’il sera une minute
# plus tard. Par exemple, si l'utilisateur tape 21 puis 32, le script doit répondre :
# "Dans une minute, il sera 21 heure(s) 33".
#
# NB : on suppose que l'utilisateur entre une heure valide. Pas besoin donc de la vérifier.

hours = int(input('Entrez les heures : '))
minutes = int(input('Entrez les minutes : '))

next_minutes = (minutes + 1) % 60

if (next_minutes == 0):
    hours = (hours + 1) % 24

print(
    f'Dans une minute, il sera {hours:02d} heure(s) {next_minutes:02d} minute(s)')
