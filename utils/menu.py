from datetime import date

def menu(kolcsonzo):
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
