liste = [("Pierre","Dos",10),("Paul","Brasse",13),("Léa","Crawl",6), ("Léa","Brasse",8) ]
commande = ''

def cmd_ajout(liste):
    """Ajoute un évènement à la liste"""
    a = input("Qui nage?")
    b = input("quelle nage ?")
    c = input("combien de longueur ?")
    liste.append ((a,b,c))

isAlive = True
while isAlive:
    commande = input("Que faut-il faire ? ")

    if commande == 'ajout':
        cmd_ajout(liste)
        continue
   
    if commande == 'liste':
        for elt in liste:
            print(f"Prénom {elt[0]}, nage {elt[1]}, longueur {elt[2]}")
        continue

    if commande == 'exit':
        tmp = input ("En êtes-vous sûr ? (o)ui:(n)on")
        if tmp == 'o':
            isAlive = False
        continue

    print(f"Commande{commande}inconnue")