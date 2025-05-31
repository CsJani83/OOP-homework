from szemelyauto import Szemelyauto
from teherauto import Teherauto
from berles import Berles  # Most már a Berles osztályt is importáljuk

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = [
            Szemelyauto("SZA-001", "Opel", 10000),
            Szemelyauto("SZA-002", "VW", 10000),
            Teherauto("TEA-001", "Iveco", 15000)
        ]
        
        # **Előre betöltött bérlések, most már Berles objektumokkal**
        self.berlesek = {
            "SZA-001": [Berles("Kiss Ádám", self.autok[0], "2025-07-01", 1)],
            "SZA-002": [Berles("Nagy Éva", self.autok[1], "2025-07-02", 2), Berles("Ádám Éva", self.autok[1], "2025-07-04", 1)],
            "TEA-001": [Berles("Gipsz Jakab", self.autok[2], "2025-07-01", 1)]
        }

    def berel_auto(self, berlo, rendszam, datum, napok_szama):
        """
        Autó bérlése adott bérlőnek, dátumra és napok számával.
        """
        if rendszam in self.berlesek:
            for foglalas in self.berlesek[rendszam]:
                if foglalas.datum == datum:
                    return "Az autó már foglalt ezen a napon!"

        auto = next((a for a in self.autok if a.rendszam == rendszam), None)
        if not auto:
            return "Érvénytelen autórendszám!"

        uj_berles = Berles(berlo, auto, datum, napok_szama)
        if rendszam not in self.berlesek:
            self.berlesek[rendszam] = []
        self.berlesek[rendszam].append(uj_berles)

        return f"Sikeres foglalás! {berlo} bérelte a(z) {rendszam} rendszámú {auto.get_auto_tipus()} {napok_szama} napra. Ár: {uj_berles.ar} Ft"

    def lemond_berles(self, berlo):
        """
        Bérlés törlése adott bérlő esetén.
        """
        for rendszam, foglalasok in list(self.berlesek.items()):
            for foglalas in foglalasok:
                if foglalas.berlo == berlo:
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
            for foglalas in foglalasok:
                kiiras += f"\n{foglalas}"
        return kiiras
