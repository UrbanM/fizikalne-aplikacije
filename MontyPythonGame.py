import random

iterations = 10

doors = ["koza"] * 2 + ["avto"]

i=0
for i in range(iterations):
    random.shuffle(doors)
    n = (int(input("Izberi vrata 1, 2 ali 3! ")) - 1)
    print("")

    sequence = [0, 1, 2]
    # random.shuffle(sequence)

    for k in sequence:
        if doors[k]!="avto" and n != k:
            print ("Avto ni za vrati %s" %(k+1))
            print("")
            sequence.remove(k)
            break

    chang = input("Ali si premislis in zamenjas vrata (y or n)?")
    print("")

    if chang == "y":
        for k in sequence:
            if n != k:
                n = k
                break

    if doors[n] == "avto":
        print ("Zmaga, čestitam.")
        print("")
    else:
        print ("Poraz! Haha, zguba ena.")
        print("")
