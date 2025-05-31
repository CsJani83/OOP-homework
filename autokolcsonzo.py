from szemelyauto import Szemelyauto
from teherauto import Teherauto

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = [
            Szemelyauto("SZA-001", "Opel", 5000),
            Szemelyauto("SZA-002", "VW", 5500),
            Teherauto("TEA-001", "Iveco", 8000)
        ]
        self.berlesek = {}

    def berel_auto(self, berlo, rendszam):
        for auto in self.autok:
            if auto.rendszam == rendszam and rendszam not in self.berlesek:
                self.berlesek[rendszam] = berlo
                return f"{berlo} sikeresen bérelte a(z) {rendszam} rendszámú autót."
        return "Nem elérhető vagy már bérelt."

    def listaz_berlesek(self):
        return self.berlesek

    def lemond_berles(self, berlo):
        for rendszam, b in list(self.berlesek.items()):
            if b == berlo:
                del self.berlesek[rendszam]
                return f"{berlo} lemondta a bérlést."
        return "Nincs ilyen bérlés."
