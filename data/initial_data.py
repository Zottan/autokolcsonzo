from datetime import date, timedelta
from models.kolcsonzo import Autokolcsonzo
from models.szemelyauto import Szemelyauto
from models.teherauto import Teherauto
from models.berles import Berles

kolcsonzo = Autokolcsonzo("CityRent")
kolcsonzo.hozzaad_auto(Szemelyauto("ABC123", "Toyota Corolla", 10000, 5))
kolcsonzo.hozzaad_auto(Szemelyauto("DEF456", "Ford Focus", 12000, 5))
kolcsonzo.hozzaad_auto(Teherauto("GHI789", "Mercedes Sprinter", 20000, 1500))

kolcsonzo.berlesek = [
    Berles(kolcsonzo.autok[0], date.today()),
    Berles(kolcsonzo.autok[1], date.today()),
    Berles(kolcsonzo.autok[2], date.today()),
    Berles(kolcsonzo.autok[0], date.today() + timedelta(days=1))
]
