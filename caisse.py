def monaiearendre():

    prixdelarticle = float(input("prix de l article: "))
    monaierecu = float(input("montant recu: "))
    difference = monaierecu - prixdelarticle

    billet100 = 100
    billet50 = 50
    billet20 = 20
    billet10 = 10
    billet5 = 5
    piece2 = 2
    piece1 = 1
    piece50c = 0.50
    piece20c = 0.20
    piece10c = 0.10
    piece5c = 0.05
    piece2c = 0.02
    piece1c = 0.01

    differenceENbillet100 = difference // billet100
    difference = difference % billet100

    differenceENbillet50 = difference // billet50
    difference = difference % billet50

    differenceENbillet20 = difference // billet20
    difference = difference % billet20

    differenceENbillet10 = difference // billet10
    difference = difference % billet10

    differenceENbillet5 = difference // billet5
    difference = difference % billet5

    differenceENpiece2 = difference // piece2
    difference = difference % piece2

    differenceENpiece1 = difference // piece1
    difference = difference % piece1

    differenceENpiece50c = difference // piece50c
    difference = difference % piece50c

    differenceENpiece20c = difference // piece20c
    difference = difference % piece20c

    differenceENpiece10c = difference // piece10c
    difference = difference % piece10c

    differenceENpiece5c = difference // piece5c
    difference = difference % piece5c

    differenceENpiece2c = difference // piece2c
    difference = difference % piece2c

    differenceENpiece1c = difference // piece1c

    print(f"Monnaie à rendre: {difference} soit :")
    print(f"{differenceENbillet100} billets de 100€")
    print(f"{differenceENbillet50} billets de 50€")
    print(f"{differenceENbillet20} billets de 20€")
    print(f"{differenceENbillet10} billets de 10€")
    print(f"{differenceENbillet5} billets de 5€")
    print(f"{differenceENpiece2} pièces de 2€")
    print(f"{differenceENpiece1} pièces de 1€")
    print(f"{differenceENpiece50c} pièces de 0.50€")
    print(f"{differenceENpiece20c} pièces de 0.20€")
    print(f"{differenceENpiece10c} pièces de 0.10€")
    print(f"{differenceENpiece5c} pièces de 0.05€")
    print(f"{differenceENpiece2c} pièces de 0.02€")
    print(f"{differenceENpiece1c} pièces de 0.01€")


monaiearendre()