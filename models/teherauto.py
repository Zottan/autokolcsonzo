from .auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, teherbiras):
        super().__init__(rendszam, tipus, berleti_dij)
        self.teherbiras = teherbiras

    def __str__(self):
        return f"Teherautó [{self.rendszam}] - {self.tipus}, {self.teherbiras} kg, {self.berleti_dij} Ft/nap"
