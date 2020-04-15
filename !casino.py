#Zcasino
import random

print("Bienvenue au casino de Max Barbe, ici, devenez des parieurs tel Grekoir")
casejoueur = int(input("Donnez votre mise, entre 0 et 49"         ))
#mise du joueur entre 0 et 49 

if casejoueur % 2 == 0:
    pair = True
    print("chiffre pair, vous avez choisi la couleur rouge")
else:
    pair = False
    print("chiffre impair, vous avez choisi la couleur noire")
# don de la couleur au joueur

misejoueur = int(input("De combien voulez vous miser ?"        ))
# choix de la mise

print("La roulette est lancée")
print("La bille est lancée et continue de tourner")

casegagnante = random.randint(0,49)
print("La case gagnante est le : ",casegagnante)
#le numéro de la case gagnante

if casegagnante % 2 == 0:
    paircase = True
else:
    paircase = False
# le type de la case gagnante, pair ou impair

if casejoueur == casegagnante:
    gain = int(misejoueur) * 3
    #gain de 3x sa mise car bonne case
    print("Vous avez gagné car c'est la bonne case! récupération de ",gain,"€")
    
elif pair == paircase:
    gain = int(misejoueur) * 1.5
    print("Vous avez gagné car les deux sont impair, récupération de ",gain,"€")
# si num joueur = famille du num gagnant = mise joueur = mj + mj/2

else:
    print("Vous avez perdu")
# si rien, perte de mj
