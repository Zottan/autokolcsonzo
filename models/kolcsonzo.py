from datetime import date
from .berles import Berles

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def hozzaad_auto(self, auto):
        self.autok.append(auto)

    def berel_auto(self, rendszam, datum):
        auto = next((a for a in self.autok if a.rendszam == rendszam), None)
        if not auto:
            return "Nincs ilyen rendszámú autó."
        if any(b.auto.rendszam == rendszam and b.datum == datum for b in self.berlesek):
            return "Ez az autó ezen a napon már foglalt."
        if datum < date.today():
            return "A bérlés dátuma nem lehet múltbeli."
        berles = Berles(auto, datum)
        self.berlesek.append(berles)
        return f"Bérlés sikeres. Ár: {auto.berleti_dij} Ft"

    def lemond_berles(self, rendszam, datum):
        for b in self.berlesek:
            if b.auto.rendszam == rendszam and b.datum == datum:
                self.berlesek.remove(b)
                return "Bérlés lemondva."
        return "Nem található ilyen bérlés."

    def listaz_berlesek(self):
        if not self.berlesek:
            return "Nincsenek aktív bérlések."
        return "\n".join(str(b) for b in self.berlesek)
