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
    def __init__(self):
        self.berlesek = []  # Minden bérlés egy listában tárolódik

    def uj_berles(self, berlo, auto, datum, napok_szama):
        # Ellenőrzés: Van-e már foglalás ezen a napon erre az autóra?
        for berles in self.berlesek:
            if berles.auto.rendszam == auto.rendszam and berles.datum == datum:
                return "Az autó már foglalt ezen a napon!"

        # Új bérlés hozzáadása
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
