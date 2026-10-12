dogum_ili=int(input("Dogum ilinizi qeyd edin"))
burcler={0: "Meymun", 1: "Xoruz", 2: "İt", 3: "Donuz", 4: "Siçan", 5: "Öküz", 6: "Pələng", 7: "Dovşan", 8: "Əjdaha", 9: "İlan",10: "At", 11: "Qoyun"}
a=dogum_ili%12
print(burcler[a])