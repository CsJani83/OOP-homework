from szemelyauto import Szemelyauto
from teherauto import Teherauto
from berles import BerlesKezelo  # Importáljuk az új BerlesKezelo osztályt

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = [
            Szemelyauto("SZA-001", "Opel", 10000),
            Szemelyauto("SZA-002", "VW", 10000),
            Teherauto("TEA-001", "Iveco", 15000)
        ]
        self.berleskezelo = BerlesKezelo()  # Most már az új osztály tárolja a bérléseket

    def berel_auto(self, berlo, rendszam, datum, napok_szama):
        auto = next((a for a in self.autok if a.rendszam == rendszam), None)
        if not auto:
            return "Érvénytelen autórendszám!"
        return self.berleskezelo.uj_berles(berlo, auto, datum, napok_szama)

    def lemond_berles(self, berlo):
        return self.berleskezelo.lemond_berles(berlo)

    def listaz_berlesek(self):
        return self.berleskezelo.listaz_berlesek()
