"""
Miinantallaaja-pelin data (ASCII-kuvat, peliohjeet yms.).
"""

LOGO = """
 ____________________________________________________________________ 
|  ________________________________________________________________  | 
| |        _ _                   _        _ _              _       | |
| |  /\/\ (_|_)_ __   __ _ _ __ | |_ __ _| | | __ _  __ _ (_) __ _ | |
| | /    \| | | '_ \ / _` | '_ \| __/ _` | | |/ _` |/ _` || |/ _` || |
| |/ /\/\ \ | | | | | (_| | | | | || (_| | | | (_| | (_| || | (_| || |
| |\/    \/_|_|_| |_|\__,_|_| |_|\__\__,_|_|_|\__,_|\__,_|/ |\__,_|| |
| | ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|__/~~~~~~ | |
| |________________________________________________________________| |
|____________________________________________________________________|  
"""

BANNERI = """     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

PUM = """
                             ____
                     __,-~~/~    `---.
                   _/_,---(      ,    )
               __ /        <    /   )  \___
- ------===;;;'====------------------===;;;===----- -  -
                  \/  ~"~"~"~"~"~\~"~)~"/
                  (_ (   \  (     >    \)
                   \_( _ <         >_>'
                      ~ `-i' ::>|--"
                          I;|.|.|
                         <|i::|i|`.
                        (` ^'"`-' ")
                _____  _    _ __  __ _ 
                |  __ \| |  | |  \/  | |
                | |__) | |  | | \  / | |
                |  ___/| |  | | |\/| | |
                | |    | |__| | |  | |_|
                |_|     \____/|_|  |_(_)
"""

TEIT_SEN = """
                       __ooooooooo__
                  oOOOOOOOOOOOOOOOOOOOOOo
              oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
           oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
         oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
       oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
      oOOOOOOOOOOO*  *OOOOOOOOOOOOOO*  *OOOOOOOOOOOOo
     oOOOOOOOOOOO      OOOOOOOOOOOO      OOOOOOOOOOOOo
     oOOOOOOOOOOOOo  oOOOOOOOOOOOOOOo  oOOOOOOOOOOOOOo
    oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
    oOOOO     OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO     OOOOo
    oOOOOOO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO OOOOOOo
     *OOOOO  OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  OOOOO*
     *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*
      *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*
       *OOOOOOo  *OOOOOOOOOOOOOOOOOOOOOOO*  oOOOOOO*
         *OOOOOOOo  *OOOOOOOOOOOOOOOOO*  oOOOOOOO*
           *OOOOOOOOo  *OOOOOOOOOOO*  oOOOOOOOO*      
              *OOOOOOOOo           oOOOOOOOO*      
                  *OOOOOOOOOOOOOOOOOOOOO*          
                       ""ooooooooo"

  _______ ______ _____ _______    _____ ______ _   _ _ 
 |__   __|  ____|_   _|__   __|  / ____|  ____| \ | | |
    | |  | |__    | |    | |    | (___ | |__  |  \| | |
    | |  |  __|   | |    | |     \___ \|  __| | . ` | |
    | |  | |____ _| |_   | |     ____) | |____| |\  |_|
    |_|  |______|_____|  |_|    |_____/|______|_| \_(_)
"""

def alusta():
    """
    Alustaa uuden kentän
    """  
    KENTTA = []
    KENTTA[:] = []

    return KENTTA
    
def peliohje():
    """
    Tulostaa käyttäjälle peliohjeet ja tekijän tiedot
    """
    print()
    print("Peliohjeet")
    print("==========")
    print()
    print("Tervetuloa pelaamaan Miinantallaajaa!")
    print()
    print("Pelin tarkoituksena avata satunnaisesti luodulta miinakentältä kaikki ruudut, mutta samalla välttää niitä, joiden alla on miina.")
    print("Pelaaja voi navigoida piilotettujen miinojen ympäri päättelemällä niiden sijainnit numeroruutujen avulla.")
    print("Numeroruutu kertoo kuinka monta miinaa sitä ympäröivissä kahdeksassa ruudussa on.")
    print()
    input("    --- Paina enter jatkaaksesi ---")
    print()
    print("    1  2  3  4  5")
    print(" 1  @  @  2  @  1")
    print(" 2  @  @  1  1  1")
    print(" 3  1  1  1      ")
    print(" 4        1  2  2")
    print(" 5        1  @  @")
    print()
    print("Yllä olevassa kentässä on esimerkki tyypillisestä pelitilanteesta.")
    print("Ylin rivi ja vasemmanpuolimmaisin sarake edustavat koordinaattiakseleita. Vaaka-akseli on x-koordinaateille, pystyakseli y-koordinaateille.")
    print("Ne eivät kerro miinojen sijainneista mitään, vaan ovat pelaajan apuna ruutujen koordinaattien paikannuksessa.")
    print("@-merkit edustavat avaamattomia ruutuja. Kun avaat kaikki ruudut, paitsi ne joiden alla on miina, voitat pelin.")
    print("Jos avaat ruudun jonka alla on miina (x-merkki), häviät pelin välittömästi ja joudut aloittamaan alusta.")
    print("Jos avaat ruudun jonka alla on tyhjää, aukeavat kaikki siihen yhteydessä olevat tyhjät ruudut.")
    print()
    input("    --- Paina enter jatkaaksesi ---")
    print()
    print("Esimerkkikentästä voidaan numeroruutujen avulla päätellä miinojen sijainnit: ")
    print("Avaamattomista ruuduista koordinaateissa (2 2), (4 1), (4 5) ja (5 5) on miina.")
    print("Koordinaatit (2 1) ja (1 2) voitaisiin siis avata turvallisesti.")
    print("Peli kysyy jokaisen siirron jälkeen avattavan ruudun koordinaattiparin, niin kauan kunnes kaikki miinattomat ruudut on avattu, tai pelaaja osuu miinaan.")
    print("Koordinaatit annetaan välilyönneillä erotettuna muodossa (\"x-koordinaatti\" \"y-koordinaatti\").")
    print("Voit lopettaa pelin kesken kirjoittamalla \"quit\".")
    print()
    input("    --- Paina enter jatkaaksesi ---")
    print()
    print("Pelissä on valittavissa kaksi erilaista pelimoodia:")
    print("Vapaa valinta -moodissa voit itse valita pelialueen koon ja miinojen määrän.")
    print("Haastemoodissa kentän koko sekä miinojen määrä on ennalta määritelty. Tällöin peli ottaa aikaa siitä kuinka kauan kentän läpäisyyn menee.")
    print("5 nopeinta aikaa ansaitsevat kunniapaikan huipputuloksissa, jonka voit nähdä päävalikosta.")
    print("Haastemoodissa on valittavissa kaksi eri kokoista kenttää, joille molemmille on omat huipputuloslistat.")
    print()
    print("Ohjelman suorituksen voi keskeyttää milloin tahansa painamalla ctrl+c.")
    print()
    print("Pidä hauskaa!")
    print()
    input("    --- Paina enter jatkaaksesi ---")
    print()
    print("Tekijä: Oskari Tervo")
    print("Oulun yliopisto, Ohjelmoinnin alkeet -kurssin lopputyö vuonna 2016")
    print("Sähköposti: tervo.oskari@gmail.com")
    print()
    input("    --- Paina enter palataksesi päävalikkoon ---")