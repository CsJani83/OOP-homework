from autokolcsonzo import Autokolcsonzo

def menu():
    print("\nOOP-Autókölcsönző")
    print("1. Autó bérlése")
    print("2. Bérlés lemondása")
    print("3. Bérlések listázása")
    print("4. Kilépés")

kolcsonzo = Autokolcsonzo("Gyors Autókölcsönző")

while True:
    menu()
    valasztas = input("Válassz egy lehetőséget: ")

    if valasztas == "1":
        berlo = input("Add meg a bérlő nevét: ")

        # Autók listázása árakkal együtt
        print("\nElérhető autók:")
        autok = kolcsonzo.autok
        for i, auto in enumerate(autok, 1):
            foglalt = "Nem bérelhető" if any(berles.auto.rendszam == auto.rendszam for berles in kolcsonzo.berleskezelo.berlesek) else "Bérelhető"
            print(f"{i}. {auto.marka} - {auto.rendszam} ({auto.get_auto_tipus()}) - {auto.berleti_dij} Ft/nap - {foglalt}")

        # Autó kiválasztása számmal
        try:
            valasztott_szam = int(input("Válaszd ki a kívánt autó számát: ")) - 1
            if valasztott_szam < 0 or valasztott_szam >= len(autok):
                print("Érvénytelen választás!")
                continue
            valasztott_auto = autok[valasztott_szam]
        except ValueError:
            print("Érvénytelen szám!")
            continue

        # Bérlés dátum megadása
        datum = input("Add meg a bérlés dátumát (YYYY-MM-DD): ")

        # Napok számának bekérése
        try:
            napok_szama = int(input("Bérelni kívánt napok száma: "))
            if napok_szama <= 0:
                print("Érvénytelen érték! A napok száma nem lehet nulla vagy negatív.")
                continue
        except ValueError:
            print("Érvénytelen szám!")
            continue

        # Bérlés véglegesítése
        print(kolcsonzo.berel_auto(berlo, valasztott_auto.rendszam, datum, napok_szama))

    elif valasztas == "2":
        berlo = input("Add meg a bérlő nevét, aki törölni szeretné a bérlést: ")
        print(kolcsonzo.lemond_berles(berlo))

    elif valasztas == "3":
        print(kolcsonzo.listaz_berlesek())

    elif valasztas == "4":
        print("Kilépés...")
        break

    else:
        print("Érvénytelen választás, próbáld újra!")
