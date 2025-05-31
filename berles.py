from szemelyauto import Szemelyauto
from teherauto import Teherauto

class Berles:
    def __init__(self, berlo, auto, datum, napok_szama):
        self.berlo = berlo
        self.auto = auto
        self.datum = datum
        self.napok_szama = napok_szama
        self.ar = auto.berleti_dij * napok_szama

    def __str__(self):
        return f"{self.berlo} bérelte: {self.auto.rendszam} ({self.auto.get_auto_tipus()}) - {self.datum} ({self.napok_szama} nap) - Ár: {self.ar} Ft"

class BerlesKezelo:
    def __init__(self, autok):
        self.berlesek = [] 
        self.betolt_indulo_berlesek(autok)

    def betolt_indulo_berlesek(self, autok):
        """
        Előre meghatározott bérlések betöltése.
        """
        auto_sza001 = next((a for a in autok if a.rendszam == "SZA-001"), None)
        auto_sza002 = next((a for a in autok if a.rendszam == "SZA-002"), None)
        auto_tea001 = next((a for a in autok if a.rendszam == "TEA-001"), None)

        if auto_sza001 and auto_sza002 and auto_tea001:
            self.berlesek.extend([
                Berles("Kiss Ádám", auto_sza001, "2025-07-01", 1),
                Berles("Nagy Éva", auto_sza002, "2025-07-02", 2),
                Berles("Ádám Éva", auto_sza002, "2025-07-04", 1),
                Berles("Gipsz Jakab", auto_tea001, "2025-07-01", 1)
            ])

    def uj_berles(self, berlo, auto, datum, napok_szama):
        for berles in self.berlesek:
            if berles.auto.rendszam == auto.rendszam and berles.datum == datum:
                return "Az autó már foglalt ezen a napon!"

        uj_berles = Berles(berlo, auto, datum, napok_szama)
        self.berlesek.append(uj_berles)
        return f"Sikeres foglalás! {uj_berles}"

    def lemond_berles(self, berlo):
        for berles in self.berlesek:
            if berles.berlo == berlo:
                self.berlesek.remove(berles)
                return f"{berlo} sikeresen lemondta a bérlést."
        return "Nincs ilyen bérlés!"

    def listaz_berlesek(self):
        if not self.berlesek:
            return "Jelenleg nincs aktív bérlés."
        return "\n".join(str(berles) for berles in self.berlesek)
