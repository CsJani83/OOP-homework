class Berles:
    def __init__(self, berlo, auto, datum, napok_szama):
        self.berlo = berlo
        self.auto = auto
        self.datum = datum
        self.napok_szama = napok_szama
        self.ar = auto.berleti_dij * napok_szama

    def __str__(self):
        return f"{self.berlo} bérelte: {self.auto.rendszam} ({self.auto.get_auto_tipus()}) - {self.datum} ({self.napok_szama} nap) - Ár: {self.ar} Ft"
