uaua = float(input("Digite a população de Uauá: "))
ny = float(input("Digite a população de NY: "))
x = float(input("Digite o crescimento de Uauá: "))
y = float(input("Digite o crescimento de NY: "))
t = 0
if uaua >= ny and y > x:
    while uaua > ny:
        ny *=(1 + (y/100))
        uaua *=(1 + (x/100))
        t += 1
    print ("Se passarão", t, "anos até que NY tenha mais gente que Uauá.")
elif uaua >= ny and y <= x:
    print("Não tem como NY ficar maior que Uauá.")
elif uaua <= ny and y < x:
    while uaua < ny:
        ny *=(1 + (y/100))
        uaua *=(1 + (x/100))
        t += 1
    print ("Se passarão", t, "anos até que Uauá tenha mais gente que NY.")
else:
    print("Não tem como Uauá ficar maior que NY.")
