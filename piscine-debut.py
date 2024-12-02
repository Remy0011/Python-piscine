liste = [("Pierre","Dos",10),("Paul","Brasse",13),("Léa","Crawl",6), ("Léa","Brasse",8) ]
commande = ''

def cmd_ajout(liste):
    """Ajoute un évènement à la liste"""
    a = input("Qui nage?")
    b = input("quelle nage ?")
    c = input("combien de longueur ?")
    liste.append ((a,b,c))

def cmd_liste(liste):
    """Affiche toutes les performances des nageurs"""
    print("Prénom   |   nage    |   longueur")
    print("---------------------------------")
    for elt in liste:
            print(f" {elt[0]:11}| {elt[1]:8}|   {elt[2]}")

def cmd_nageur(liste):
    """"Affiche toutes les performances d'un nageur"""
    tmp = input("Quel nageur?")
    print("Performance de ",tmp)
    print("nage |   longueur")
    print("-------------------")
    for elt in liste:
        if elt[0]== tmp:
            print(f"{elt[1]:8} | {elt[2]}")

def cmd_nage(liste):
    """Affiche toutes les performances suivant une nage donnée"""
    tmp = input("Quelle nage ?")
    print("nage",tmp)
    print("nageur | longueur")
    print("----------------")
    for elt in liste:
        if elt[1]== tmp:
            print(f"{elt[0]:11} | {elt[2]}")

def cmd_sauvegarde(liste):
    """Sauvegarde la BDD"""
    fichier = open('save.csv', 'w')
    for elt in liste:
        fichier.write(elt[0]+','+elt[1]+','+str(elt[2])+"\n")
    fichier.close()

def cmd_charger(liste):
    """charger la BDD"""
    fichier = open('save.csv', 'r')
    for line in fichier:
        line.strip()
        if line[-1] == '\n':
            line = line[:-1]
        if line[0]=='#':
            continue
        tmp = line.split(',')
        liste.append(tuple(tmp))
    fichier.close()    

def cmd_exit():
    tmp = input ("En êtres-vous sûr ? (o)ui/(n)on")
    if tmp == 'o':
        return False
    else:
        return True

isAlive = True
while isAlive:
    commande = input("Que faut-il faire ? ")

    if commande == 'ajout':
        cmd_ajout(liste)
        continue
   
    if commande == 'liste':
        cmd_liste(liste)
        continue

    if commande == 'nageur':
        cmd_nageur(liste)
        continue

    if commande == 'nage':
        cmd_nage(liste)
        continue

    if commande == "sauvegarde":
        cmd_sauvegarde(liste)
        continue

    if commande == "charger":
        cmd_charger(liste)
        continue

    if commande == 'exit':
        isAlive = cmd_exit()
        continue

    print(f"Commande{commande}inconnue")