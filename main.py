from autokolcsonzo import Autokolcsonzo

def menu():
    print("\nAutókölcsönző Rendszer")
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
        rendszam = input("Add meg a bérelni kívánt autó rendszámát: ")
        print(kolcsonzo.berel_auto(berlo, rendszam))

    elif valasztas == "2":
        berlo = input("Add meg a bérlő nevét, aki törölni szeretné a bérlést: ")
        print(kolcsonzo.lemond_berles(berlo))

    elif valasztas == "3":
        print("\nAktuális bérlések:")
        berlesek = kolcsonzo.listaz_berlesek()
        for rendszam, berlo in berlesek.items():
            print(f"{berlo} bérelte: {rendszam}")

    elif valasztas == "4":
        print("Kilépés...")
        break

    else:
        print("Érvénytelen választás, próbáld újra!")
