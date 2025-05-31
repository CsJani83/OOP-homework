from szemelyauto import Szemelyauto
from teherauto import Teherauto


class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = [
            Szemelyauto("SZA-001", "Opel", 10000),
            Szemelyauto("SZA-002", "VW", 10000),
            Teherauto("TEA-001", "Iveco", 15000)
        ]

        # **Előzetes bérlések LISTÁBAN**
        self.berlesek = {
            "SZA-001": [("Kiss Ádám", "2025-07-01", 1)],
            "SZA-002": [("Nagy Éva", "2025-07-02", 2), ("Ádám Éva", "2025-07-04", 1)],
            "TEA-001": [("Gipsz Jakab", "2025-07-01", 1)]
        }

    def berel_auto(self, berlo, rendszam, datum, napok_szama):
        """
        Autó bérlése adott bérlőnek, dátumra és napok számával.
        """
        if rendszam in self.berlesek:
            for foglalas in self.berlesek[rendszam]:
                if foglalas[1] == datum:
                    return "Az autó már foglalt ezen a napon!"

        auto = next((a for a in self.autok if a.rendszam == rendszam), None)
        if not auto:
            return "Érvénytelen autórendszám!"

        teljes_ar = auto.berleti_dij * napok_szama
        if rendszam not in self.berlesek:
            self.berlesek[rendszam] = []
        self.berlesek[rendszam].append((berlo, datum, napok_szama))

        return f"Sikeres foglalás! {berlo} bérelte a(z) {rendszam} rendszámú {auto.get_auto_tipus()} {napok_szama} napra. Ár: {teljes_ar} Ft"

    def lemond_berles(self, berlo):
        """
        Bérlés törlése adott bérlő esetén.
        """
        for rendszam, foglalasok in list(self.berlesek.items()):
            for foglalas in foglalasok:
                if foglalas[0] == berlo:
                    foglalasok.remove(foglalas)
                    return f"{berlo} sikeresen lemondta a bérlést."
        return "Nincs ilyen bérlés!"

    def listaz_berlesek(self):
        """
        Az összes aktuális bérlés kiírása.
        """
        if not self.berlesek:
            return "Jelenleg nincs aktív bérlés."

        kiiras = "\nAktuális bérlések:"
        for rendszam, foglalasok in self.berlesek.items():
            auto = next((a for a in self.autok if a.rendszam == rendszam), None)
            for berlo, datum, napok_szama in foglalasok:
                teljes_ar = auto.berleti_dij * napok_szama
                kiiras += f"\n{berlo} bérelte: {rendszam} ({auto.get_auto_tipus()}) - {datum} ({napok_szama} nap) - Ár: {teljes_ar} Ft"
        return kiiras
