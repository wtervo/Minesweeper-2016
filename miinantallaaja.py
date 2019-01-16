"""
Miinantallaaja-pelin pääohjelma ja -valikko.
"""

import miinapeli as mipe
import miinadata as mida

if __name__ == "__main__":
    print()
    print()
    print(mida.LOGO)
    print()
    print()
    print()
    while True:
        print()
        print("Päävalikko")
        print("==========")
        print()
        print("1 - Uusi peli")
        print("2 - Peliohjeet")
        print("3 - Huipputulokset")
        print("4 - Lopeta peli")
        try:
            print()
            valinta = str(input("Valitse toiminto numeronäppäimellä (1-4): ").strip())
        except EOFError:
            print()
            print("Voit lopettaa pelin valitsemalla numeron 4 tai keskeyttää ohjelman painamalla ctrl+c")
        except ValueError:
            print()
            print("VIRHE: valitsemaasi toimintoa ei ole olemassa")
        else:
            if valinta == "1":
                mipe.uusi_peli()
            elif valinta == "2":
                mida.peliohje()
            elif valinta == "3":
                mipe.kirjaa_huipputulokset("luo tuloslistat", "miinantallaaja_tulokset_pieni.txt")
                mipe.kirjaa_huipputulokset("luo tuloslistat", "miinantallaaja_tulokset_iso.txt")
                print()
                print("Huipputulokset")
                print("==============")
                print()
                print("     Pieni haastekenttä (15x15), 30 miinaa")
                print(mida.BANNERI)
                print("     PÄIVÄMÄÄRÄ           NIMI                              AIKA  ")
                print()
                mipe.tulosta_huipputulokset("miinantallaaja_tulokset_pieni.txt")
                print(mida.BANNERI)
                print()
                print()
                print("     Iso haastekenttä (20x30), 90 miinaa")
                print(mida.BANNERI)
                print("     PÄIVÄMÄÄRÄ           NIMI                              AIKA  ")
                print()
                mipe.tulosta_huipputulokset("miinantallaaja_tulokset_iso.txt")
                print(mida.BANNERI)
                print()
            elif valinta == "4":
                print()
                print("Haluatko varmasti lopettaa pelin? Lopeta peli valitsemalla \"k\".")
                lopetus = input("[k]yllä: ").lower().strip()
                if lopetus == "k":
                    break
            else:
                print()
                print("VIRHE: valitsemaasi toimintoa ei ole olemassa")    