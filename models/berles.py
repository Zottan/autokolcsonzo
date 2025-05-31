class Berles:
    def __init__(self, auto, datum):
        self.auto = auto
        self.datum = datum

    def __str__(self):
        return f"{self.auto.rendszam} bérlése {self.datum} napra - Ár: {self.auto.berleti_dij} Ft"
