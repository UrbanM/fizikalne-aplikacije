import random

iterations = 1000

doors = ["koza"] * 2 + ["avto"]

zmaga = 0
poraz = 0

zamenjava_zmaga = 0
zamenjava_poraz = 0


for i in range(iterations):
    random.shuffle(doors)
    n = random.randrange(3)

    # now if you change, you lose iff doors[n]=="car"
    if doors[n] == "avto":
        zmaga += 1
    else:
        poraz += 1

i=0
for i in range(iterations):
    random.shuffle(doors)
    n = random.randrange(3)

    sequence = [0, 1, 2]
    random.shuffle(sequence)

    for k in sequence:
        if doors[k]!="avto" and n != k:
            sequence.remove(k)
            break

    #print sequence, n

    for k in sequence:
        if n != k:
            n = k
            break

    #print sequence, n

    # now if you change, you lose iff doors[n]=="car"
    if doors[n] == "avto":
        zamenjava_zmaga += 1
    else:
        zamenjava_poraz += 1


print ("Brez zamenjave imamo %s zmag in %s porazov" % (zmaga, poraz))
perc = (100.0 * zmaga) / (zmaga + poraz)
print ("Zmaga je %.1f%% procentna" % perc)

print ("Z zamenjavo imamo %s zmag in %s porazov" % (zamenjava_zmaga, zamenjava_poraz))
perc = (100.0 * zamenjava_zmaga) / (zamenjava_zmaga + zamenjava_poraz)
print ("Zmaga je %.1f%% procentna" % perc)
