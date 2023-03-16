import random as ran

"""Loto"""
counting1 = [0, 0, 0, 0, 0, 0, 0, 0]
counting11 = [0, 0, 0, 0, 0, 0, 0, 0]

"""Obkrožena števila"""
chosnum = [3, 4, 23, 21, 11, 39, 31]

c = int(input("Koliko ponovitev želite: "))

for j in range(0, c):
    # Izžrebana števila
    picked = ran.sample(range(1, 40), 7)

    # Dodatna številka
    extra = range(1, 40)
    # izbriše že izrbana števila
    extra = [x for x in extra if x not in picked]
    # izbere dodatno številko
    extra = ran.sample(extra, 1)

    n = []
    n1 = []
    j1 = 0
    for a in chosnum:
        # prešteje ali je bila izbrana številka dodatna
        j1 = extra.count(a)
        # prešteje ali je bila izbrana številka ibrana številka
        i = picked.count(a)
        n1.append(j1)
        n.append(i)
    # sešteje
    chosen = sum(n)
    exchosen = sum(n1)

    if (exchosen > 0):
        counting11[chosen] = counting11[chosen] + 1
    else:
        counting1[chosen] = counting1[chosen] + 1

print('-> Vaše izbrana števila so:')
print(chosnum)
print('-> Vrednosti brez ujemanj je bilo %d krat' % (counting1[0]))
print('-> Vrednosti z enim ujemanjem je bilo %d krat' % (counting1[1]))
print('-> Vrednosti z dvema ujemanja je bilo %d krat' % (counting1[2]))
print('-> Vrednosti z tremi ujemanji je bilo %d krat' % (counting1[3]))
print('-> Vrednosti z tremi + 1 ujemanji je bilo %d krat' % (counting11[3]))
print('-> Vrednosti z štirimi ujemanji je bilo %d krat' % (counting1[4]))
print('-> Vrednosti z štirimi + 1 ujemanji je bilo %d krat' % (counting11[4]))
print('-> Vrednosti z petimi ujemanji je bilo %d krat' % (counting1[5]))
print('-> Vrednosti z petimi + 1 ujemanji je bilo %d krat' % (counting11[5]))
print('-> Vrednosti z šestimi ujemanji je bilo %d krat' % (counting1[6]))
print('-> Vrednosti z šestimi + 1 ujemanji je bilo %d krat' % (counting11[6]))
print('-> SEDMICO ste zadeli %d krat' % (counting1[7]))

vlozek = 0.60 * c
izkupicek = counting11[3] * 4.16 + counting1[4] * 5.26 + counting11[4] * 10.76 + counting1[5] * 63.53 \
            + counting11[5] * 168.28 + counting1[6] * 2625.17 + counting11[6] * 15332.94 + counting1[7] * 1598126.80

print('-> Vložili ste: %lf€' % (vlozek))
print('-> Končni izkupi   ček znaša: %lf€' % (izkupicek))

# print chosnum
# print dinam
# print picked
# print chosen
# print counting1
