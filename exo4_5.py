# Exercice 4.5

# Les habitants paient l’impôt selon les règles suivantes :
#  • les hommes de plus de 20 ans paient l’impôt
#  • les femmes paient l’impôt si elles ont entre 18 et 35 ans
#  • les autres ne paient pas d’impôt
# Le programme demandera donc l’âge et le sexe, et se prononcera donc ensuite sur le fait que
# l’habitant est imposable.

age = int(input('Donnez votre âge : '))
sex = input('Sexe (H/F) ? ').upper()

is_taxable = False

if (sex == 'H' and age > 20) or (sex == 'F' and (age >= 18 and age <= 35)):
    is_taxable = True

print(f"L'habitant est {'imposable' if is_taxable else 'non-imposable'}.")
