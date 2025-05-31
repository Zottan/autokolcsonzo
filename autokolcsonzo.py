from abc import ABC, abstractmethod
from datetime import date

class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij

    @abstractmethod
    def __str__(self):
        pass

class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, utasszam):
        super().__init__(rendszam, tipus, berleti_dij)
        self.utasszam = utasszam

    def __str__(self):
        return f"Személyautó [{self.rendszam}] - {self.tipus}, {self.utasszam} fő, {self.berleti_dij} Ft/nap"

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, teherbiras):
        super().__init__(rendszam, tipus, berleti_dij)
        self.teherbiras = teherbiras

    def __str__(self):
        return f"Teherautó [{self.rendszam}] - {self.tipus}, {self.teherbiras} kg, {self.berleti_dij} Ft/nap"

class Berles:
    def __init__(self, auto, datum):
        self.auto = auto
        self.datum = datum

    def __str__(self):
        return f"{self.auto.rendszam} bérlése {self.datum} napra - Ár: {self.auto.berleti_dij} Ft"

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

# Előkészített adatok
kolcsonzo = Autokolcsonzo("CityRent")
kolcsonzo.hozzaad_auto(Szemelyauto("ABC123", "Toyota Corolla", 10000, 5))
kolcsonzo.hozzaad_auto(Szemelyauto("DEF456", "Ford Focus", 12000, 5))
kolcsonzo.hozzaad_auto(Teherauto("GHI789", "Mercedes Sprinter", 20000, 1500))

kolcsonzo.berlesek = [
    Berles(kolcsonzo.autok[0], date.today()),
    Berles(kolcsonzo.autok[1], date.today()),
    Berles(kolcsonzo.autok[2], date.today()),
    Berles(kolcsonzo.autok[0], date.today().replace(day=date.today().day + 1))
]

# Felhasználói felület
def menu():
    while True:
        print("\n--- Autókölcsönző ---")
        print("1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Bérlések listázása")
        print("0. Kilépés")

        valasztas = input("Választás: ")
        if valasztas == "1":
            rendszam = input("Adja meg a rendszámot: ")
            datum_str = input("Adja meg a dátumot (ÉÉÉÉ-HH-NN): ")
            try:
                datum = date.fromisoformat(datum_str)
                print(kolcsonzo.berel_auto(rendszam, datum))
            except ValueError:
                print("Érvénytelen dátumformátum.")
        elif valasztas == "2":
            rendszam = input("Adja meg a rendszámot: ")
            datum_str = input("Adja meg a dátumot (ÉÉÉÉ-HH-NN): ")
            try:
                datum = date.fromisoformat(datum_str)
                print(kolcsonzo.lemond_berles(rendszam, datum))
            except ValueError:
                print("Érvénytelen dátumformátum.")
        elif valasztas == "3":
            print("\nAktív bérlések:")
            print(kolcsonzo.listaz_berlesek())
        elif valasztas == "0":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás.")

# Program indítása
if __name__ == "__main__":
    menu()
