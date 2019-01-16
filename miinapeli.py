"""
Miinantallaaja-pelin pyörittämiseen tarvittavat funktiot.
"""

import random
import miinadata as mida
import time
    
def kysy_koordinaatit(kentta):
    """
    Kysyy ja tarkistaa käyttäjän koordinaatit sekä palauttaa ne.
    Ottaa argumentikseen pelikentän, jotta voi tarkistaa ovatko annetut koordinaatit sen sisällä.
    """
    while True:
        try:
            print()
            koordinaatit = input("Anna avattavan ruudun koordinaatit (x y) tai lopeta kirjoittamalla \"quit\": ")
            if koordinaatit == "quit":
                return None, None
            else:
                koordinaatit = koordinaatit.split(" ")
        except EOFError:
            print("Voit keskeyttää ohjelman suorituksen painamalla ctrl + c")
        except ValueError:
            print()
            print("Anna koordinaatit kokonaislukuina muodossa (x y). Jos haluat lopettaa pelin kesken, kirjoita \"quit\".")
        else:
            if len(koordinaatit) > 2:
                print()
                print("Anna koordinaatit kokonaislukuina muodossa (x y). Jos haluat lopettaa pelin kesken, kirjoita \"quit\".")
                continue
            try:
                x = int(koordinaatit[0])
                y = int(koordinaatit[1])
            except (ValueError, IndexError):
                print()
                print("Anna koordinaatit kokonaislukuina muodossa (x y). Jos haluat lopettaa pelin kesken, kirjoita \"quit\".")
            else:
                if x < 1 or y < 1:
                    print()
                    print("Koordinaatit ovat kentän ulkopuolella!")
                elif x >= len(kentta[0]) or y >= len(kentta):
                    print()
                    print("Koordinaatit ovat kentän ulkopuolella!")
                else:
                    return x, y
                    
def kysy_miinat(leveys, korkeus):
    """
    Kysyy käyttäjältä kentälle haluttujen miinojen määrän ja tarkistaa ettei niitä ole liikaa tai liian vähän.
    Ottaa argumenteikseen kentän leveyden ja korkeuden. Palauttaa miinojen määrän.
    """
    maksimi = round(0.2 * leveys * korkeus)
    print()
    print("Valitse miinojen lukumäärä {}x{} kokoiselle kentälle välillä [5 - {}] kpl.".format(leveys, korkeus, maksimi))
    while True:
        try:
            print()
            miina_lkm = int(input("Anna miinojen lukumäärä: "))
        except ValueError:
            print()
            print("Anna miinojen lukumäärä positiivisena kokonaislukuna!")
        except EOFError:
            print("Voit keskeyttää ohjelman suorituksen painamalla ctrl + c")
        else:
            if miina_lkm < 5:
                print()
                print("Miinoja tulee olla vähintään 5!")
                continue
            elif miina_lkm > maksimi:
                print()
                print("Miinoja on liikaa alueen kokoon nähden! {}x{} kokoiselle alueelle maksimi on {} miinaa.".format(leveys, korkeus, maksimi))
            else:
                return miina_lkm
                
def kysy_nimi():
    """
    Kysyy käyttäjän nimen huipputuloksia varten ja tarkistaa, että se on sopivan mittainen.
    Palauttaa nimen.
    """
    while True:
        try:
            print()
            nimi = input("Anna nimesi (max 20 merkkiä): ").strip()
        except EOFError:
            print()
            print("Voit keskeyttää ohjelman suorituksen painamalla ctrl + c")
        else:
            if not nimi:
                print()
                print("Et antanut nimeä!")
            elif len(nimi) > 20:
                print()
                print("Annoit liian pitkän nimen!")
            else:
                return nimi
    
def laske_miinat(leveys, korkeus, miinat):
    """
    Laskee jokaista koordinaattia ympäröivissä ruuduissa olevien miinojen määrän ja lisää ne miinalistaan.
    Ottaa argumenteikseen kentän leveyden ja korkeuden sekä miinakentän.
    """
    for y in range(1, korkeus + 1):
        for x in range(1, leveys + 1):
            if miinat[y][x] == " x":
                continue
            elif y == 1 and x == 1:
                n5 = miinat[y][x + 1].count(" x")
                n7 = miinat[y + 1][x].count(" x")
                n8 = miinat[y + 1][x + 1].count(" x")
                miina_nro = n5 + n7 + n8
                if miina_nro == 0:
                    continue
                else:
                    miinat[y][x] = " {}".format(str(miina_nro))
            elif y == korkeus and x == leveys:
                n1 = miinat[y - 1][x - 1].count(" x")
                n2 = miinat[y - 1][x].count(" x")
                n4 = miinat[y][x - 1].count(" x")
                miina_nro = n1 + n2 + n4
                if miina_nro == 0:
                    continue
                else:
                    miinat[y][x] = " {}".format(str(miina_nro))
            elif y == 1 and x == leveys:
                n4 = miinat[y][x - 1].count(" x")
                n6 = miinat[y + 1][x - 1].count(" x")
                n7 = miinat[y + 1][x].count(" x")
                miina_nro = n4 + n6 + n7
                if miina_nro == 0:
                    continue
                else:
                    miinat[y][x] = " {}".format(str(miina_nro))
            elif x == 1 and y == korkeus:
                n2 = miinat[y - 1][x].count(" x")
                n3 = miinat[y - 1][x + 1].count(" x")
                n5 = miinat[y][x + 1].count(" x")
                miina_nro = n2 + n3 + n5
                if miina_nro == 0:
                    continue
                else:
                    miinat[y][x] = " {}".format(str(miina_nro))
            elif y == 1:
                n4 = miinat[y][x - 1].count(" x")
                n5 = miinat[y][x + 1].count(" x")
                n6 = miinat[y + 1][x - 1].count(" x")
                n7 = miinat[y + 1][x].count(" x")
                n8 = miinat[y + 1][x + 1].count(" x")
                miina_nro = n4 + n5 + n6 + n7 + n8
                if miina_nro == 0:
                    continue
                else:
                    miinat[y][x] = " {}".format(str(miina_nro))
            elif x == 1:
                n2 = miinat[y - 1][x].count(" x")
                n3 = miinat[y - 1][x + 1].count(" x")
                n5 = miinat[y][x + 1].count(" x")
                n7 = miinat[y + 1][x].count(" x")
                n8 = miinat[y + 1][x + 1].count(" x")
                miina_nro = n2 + n3 + n5 + n7 + n8
                if miina_nro == 0:
                    continue
                else:
                    miinat[y][x] = " {}".format(str(miina_nro))
            elif y == korkeus:
                n1 = miinat[y - 1][x - 1].count(" x")
                n2 = miinat[y - 1][x].count(" x")
                n4 = miinat[y][x - 1].count(" x")
                n3 = miinat[y - 1][x + 1].count(" x")
                n5 = miinat[y][x + 1].count(" x")
                miina_nro = n1 + n2 + n3 + n4 + n5
                if miina_nro == 0:
                    continue
                else:
                    miinat[y][x] = " {}".format(str(miina_nro))
            elif x == leveys:
                n1 = miinat[y - 1][x - 1].count(" x")
                n2 = miinat[y - 1][x].count(" x")
                n4 = miinat[y][x - 1].count(" x")
                n6 = miinat[y + 1][x - 1].count(" x")
                n7 = miinat[y + 1][x].count(" x")
                miina_nro = n1 + n2 + n4 + n6 + n7
                if miina_nro == 0:
                    continue
                else:
                    miinat[y][x] = " {}".format(str(miina_nro))
            else:
                n1 = miinat[y - 1][x - 1].count(" x")
                n2 = miinat[y - 1][x].count(" x")
                n3 = miinat[y - 1][x + 1].count(" x")
                n4 = miinat[y][x - 1].count(" x")
                n5 = miinat[y][x + 1].count(" x")
                n6 = miinat[y + 1][x - 1].count(" x")
                n7 = miinat[y + 1][x].count(" x")
                n8 = miinat[y + 1][x + 1].count(" x")
                miina_nro = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
                if miina_nro == 0:
                    continue
                else:
                    miinat[y][x] = " {}".format(str(miina_nro))
        
def miinoittaja(leveys, korkeus, miina_lkm, miinat, x_aloitus, y_aloitus):
    """
    Asettaa pelialueelle satunnaisesti miinoja.
    Ottaa argumenteikseen pelialueen leveyden ja korkeuden, miinojen määrän, miinakentän sekä ensimmäiset xy-koordinaatit.
    """
    for rivi in range(korkeus + 1):
        miinat.append([])
        for sarake in range(leveys + 1):
            miinat[-1].append("  ")
    
    jaljella = mida.alusta()
    for rivi in range(1, korkeus + 1):
        for sarake in range(1, leveys + 1):
            if miinat[rivi][sarake] != " x":
                jaljella.append((sarake, rivi))
                
    jaljella.remove((x_aloitus, y_aloitus))
    if x_aloitus < leveys:
        jaljella.remove((x_aloitus + 1, y_aloitus))
    if y_aloitus < korkeus:
        jaljella.remove((x_aloitus, y_aloitus + 1))
    if x_aloitus > 1:
        jaljella.remove((x_aloitus - 1, y_aloitus))
    if y_aloitus > 1:
        jaljella.remove((x_aloitus, y_aloitus - 1))
    if x_aloitus > 1 and y_aloitus > 1:
        jaljella.remove((x_aloitus - 1, y_aloitus - 1))
    if x_aloitus < leveys and y_aloitus > 1:
        jaljella.remove((x_aloitus + 1, y_aloitus - 1))
    if x_aloitus > 1 and y_aloitus < korkeus:
        jaljella.remove((x_aloitus - 1, y_aloitus + 1))
    if x_aloitus < leveys and y_aloitus < korkeus:
        jaljella.remove((x_aloitus + 1, y_aloitus + 1))
    
    luku = 0
    for toisto in range(1000):
        if luku == miina_lkm:
             break
        kantama = len(jaljella)
        koordinaatti = random.randrange(kantama)
        arvo = jaljella[koordinaatti]
        x, y = arvo
        miinat[y][x] = " x"
        jaljella.remove(arvo)
        luku += 1
        
    for x_numero in range(1, leveys + 1):
        x_num = str(x_numero)
        if len(x_num) < 2:
            x_num = " {}".format(x_num)
        miinat[0][x_numero] = x_num
    for y_numero in range(1, korkeus + 1):
        y_num = str(y_numero)
        if len(y_num) < 2:
            y_num = " {}".format(y_num)
        miinat[y_numero][0] = y_num
        
    laske_miinat(leveys, korkeus, miinat)

def luo_kentta(leveys, korkeus, kentta):
    """
    Luo halutun kokoisen kentän
    Ottaa argumenteikseen kentän leveyden ja korkeuden sekä tyhjän kentän. Palauttaa kentän.
    """
    for rivi in range(korkeus + 1):
        kentta.append([])
        for sarake in range(leveys + 1):
            kentta[-1].append(" @")
    kentta[0][0] = "  "
    for x_numero in range(1, leveys + 1):
        x_num = str(x_numero)
        if len(x_num) < 2:
            x_num = " {}".format(x_num)
        kentta[0][x_numero] = x_num
    for y_numero in range(1, korkeus + 1):
        y_num = str(y_numero)
        if len(y_num) < 2:
            y_num = " {}".format(y_num)
        kentta[y_numero][0] = y_num
                    
def kentan_dimensiot():
    """
    Kysyy käyttäjältä kentän leveyden ja korkeuden sekä tarkistaa ovatko ne sallittujen rajojen sisällä
    Palautaa kentän leveyden ja korkeuden
    """
    while True:
        try:
            print()
            leveys = int(input("Anna kentän leveys välillä [5, 30]: "))
            if leveys < 5 or leveys > 30:
                print()
                print("Anna kentän leveys ja korkeus positiivisina kokonaislukuina välillä [5, 30]")
                continue
            print()
            korkeus = int(input("Anna kentän korkeus välillä [5, 30]: "))
            if korkeus < 5 or korkeus > 30:
                print()
                print("VIRHE: anna kentän leveys ja korkeus positiivisina kokonaislukuina välillä [5, 30]")
                continue
        except ValueError:
            print()
            print("Anna kentän leveys ja korkeus positiivisina kokonaislukuina välillä [5, 30]")
        except EOFError:
            print()
            print("Voit keskeyttää ohjelman suorituksen painamalla ctrl + c")
        else:
            return leveys, korkeus

def tulvataytto(x_aloitus, y_aloitus, kentta, miinat):
    """
    Siivoaa pelialueen tyhjiä ruutuja
    Ottaa argumenteikseen xy-koordinaatit, kentän ja miinakentän.
    """
    xy_parit = []
    xy_parit.append((x_aloitus, y_aloitus))
    while xy_parit:
        arvo = xy_parit[0]
        x, y = arvo
        xy_parit.remove(arvo)
        if miinat[y][x] == "  ":
            kentta[y][x] = miinat[y][x]
            miinat[y][x] = " ."
            if x > 1:
                xy_parit.append((x - 1, y))
            if x < len(kentta[0]) - 1:
                xy_parit.append((x + 1, y))
            if y > 1:
                xy_parit.append((x, y - 1))
            if y < len(kentta) - 1:
                xy_parit.append((x, y + 1))
            if x > 1 and y > 1:
                xy_parit.append((x - 1, y - 1))
            if x > 1 and y < len(kentta) - 1:
                xy_parit.append((x - 1, y + 1))
            if y > 1 and x < len(kentta[0]) - 1:
                xy_parit.append((x + 1, y - 1))
            if y < len(kentta) - 1 and x < len(kentta[0]) - 1:
                xy_parit.append((x + 1, y + 1))
        elif miinat[y][x] == " .":
            continue
        else:
            kentta[y][x] = miinat[y][x]

def tulosta_pelialue(kentta):
    """
    Tulostaa käyttäjälle näkymän pelialueesta.
    Ottaa argumentikseen tulostettavan kentän.
    """
    print()
    for rivi in kentta:
        liitos = " ".join(rivi)
        print(liitos)
        
def tulosta_huipputulokset(tiedosto):
    """
    Lukee huipputulokset tiedostosta ja tulostaa ne nopeimmasta ajasta hitaimpaan.
    Ottaa argumentikseen luettavan tiedoston.
    """
    with open(tiedosto, "r") as tulokset:
        jarjestys = sorted(tulokset, key=lambda data: float(data.split("$")[2]))
        for tulos in jarjestys:
            pvm, nimi, aika = tulos.split("$")
            aika = float(aika.strip("\n"))
            minuutit = aika // 60
            sekunnit = aika % 60
            if minuutit == 0:
                sekunnit = str(round(aika % 60, 2))
                print("     {} {} {}s".format(pvm.ljust(20, " "), nimi.ljust(25, " "), sekunnit.rjust(13, " ")))
            else:
                minuutit = str(round(aika // 60))
                sekunnit = str(round(aika % 60, 2))
                print("     {} {} {}min {}s".format(pvm.ljust(20, " "), nimi.ljust(25, " "), minuutit.rjust(4, " "), sekunnit))
          
def kirjaa_huipputulokset(aika, tiedosto):
    """
    Avaa huipputulostiedoston tai luo sen, jos sitä ei ennestään ole.
    Tarkistaa onko käyttäjä ansainnut paikan huipputuloksissa.
    Kirjaa nimen, ajan ja tuloksen tiedostoon.
    Ottaa ottaa argumentikseen peliin kuluneen ajan ja tiedoston.
    """
    pvm = time.strftime("%d/%m/%Y")
    try:
        with open(tiedosto, "r") as tulokset:
            rivi_lkm = sum(1 for line in tulokset)
    except IOError:
        uusi_tiedosto = open(tiedosto, "a")
        uusi_tiedosto.close()
        rivi_lkm = 0
    if aika == "luo tuloslistat":
        return
    tuloslista = mida.alusta()
    if rivi_lkm == 5:
        with open(tiedosto, "r") as tulokset:
            tiedot = tulokset.readlines()
            tuloslista.append(float(aika))
            for rivi in tiedot:
                a, b, c = rivi.split("$")
                tulos = float(c.rstrip("\n"))
                tuloslista.append(tulos)
            maksimi = max(tuloslista)
        if maksimi == float(aika):
            print()
            print("Aikasi ei tällä kertaa riittänyt viiden parhaan joukkoon. Parempi onni ensi kerralla!")
            with open(tiedosto, "w") as tulokset:
                for rivi in tiedot:
                    pvm, nimi, aika = rivi.split("$")
                    if aika != str(maksimi) + "\n":
                        tulokset.write(rivi)
            print()
            print(mida.BANNERI)
            print("     PÄIVÄMÄÄRÄ           NIMI                              AIKA  ")
            tulosta_huipputulokset(tiedosto)
            print(mida.BANNERI)
        else:
            print()
            print("Olet ansainnut paikan huipputuloksissa! Mahtavaa!")
            nimi = kysy_nimi()
            with open(tiedosto, "a") as tulokset:
                tulokset.write("{}${}${}\n".format(pvm, nimi, aika))
            with open(tiedosto, "r") as tulokset:
                tiedot = tulokset.readlines()
            with open(tiedosto, "w") as tulokset:
                for rivi in tiedot:
                    pvm, nimi, aika = rivi.split("$")
                    if aika != str(maksimi) + "\n":
                        tulokset.write(rivi)
            print()
            print(mida.BANNERI)
            print("     PÄIVÄMÄÄRÄ           NIMI                              AIKA  ")
            tulosta_huipputulokset(tiedosto)
            print(mida.BANNERI)
    else:
        print()
        print("Olet ansainnut paikan huipputuloksissa! Mahtavaa!")
        nimi = kysy_nimi()
        with open(tiedosto, "a") as tulokset:
            tulokset.write("{}${}${}\n".format(pvm, nimi, aika))
        print()
        print(mida.BANNERI)
        print("     PÄIVÄMÄÄRÄ           NIMI                              AIKA  ")
        tulosta_huipputulokset(tiedosto)
        print(mida.BANNERI)
            
def kerro_aika(aika, tulos):
    """
    Kertoo käyttäjälle kauanko pelin läpäisemiseen tai epäonnistumiseen kului aikaa.
    Ottaa argumentikseen peliin kuluneen ajan sekä True/False-arvon.
    """
    minuutit = aika // 60
    sekunnit = aika % 60
    if tulos == True:
        if minuutit == 0:
            print("Onneksi olkoon, voitit pelin ajassa {:.2f} sekuntia!".format(sekunnit))
        else:
            print("Onneksi olkoon, voitit pelin ajassa {:.0f} minuuttia {:.2f} sekuntia!".format(minuutit, sekunnit))
    elif tulos == False:
        if minuutit == 0:
            print("Peli on päättynyt. Kestit tällä kertaa {:.2f} sekuntia.".format(sekunnit))
        else:
            print("Peli on päättynyt. Kestit tällä kertaa {:.0f} minuuttia {:.2f} sekuntia!".format(minuutit, sekunnit))       
          
def pelisilmukka(leveys, korkeus, miina_lkm, kentta, miinat):
    """
    Pyörittää peliä.
    Ottaa argumenteikseen kentän leveyden ja korkeuden, miinojen lukumäärän, kentän ja miinakentän.
    Palauttaa True or False riippuen siitä voittaako vai häviääkö pelaaja pelin sekä peliin kuluneen ajan.
    """
    luo_kentta(leveys, korkeus, kentta)
    tulosta_pelialue(kentta)
    print()
    x, y = kysy_koordinaatit(kentta)
    if x == None and y == None:
        print()
        print("Keskeytit pelin")
        return False, 0
    miinat = mida.alusta()
    miinoittaja(leveys, korkeus, miina_lkm, miinat, x, y)
    tulvataytto(x, y, kentta, miinat)
    tulosta_pelialue(kentta)
    alku = time.time()

    while True:
        ruudut = leveys * korkeus
        for rivi in range(1, korkeus + 1):
            for sarake in range(1, leveys + 1):
                if kentta[rivi][sarake] != " @":
                    ruudut -= 1
        if ruudut == miina_lkm:
            loppu = time.time()
            aika = loppu - alku
            print()
            print(mida.TEIT_SEN)
            return True, aika
        x, y = kysy_koordinaatit(kentta)
        if x == None and y == None:
            loppu = time.time()
            aika = loppu - alku
            print()
            print("Keskeytit pelin")
            return False, aika
        if miinat[y][x] == " x":
            loppu = time.time()
            aika = loppu - alku
            tulosta_pelialue(miinat)
            print()
            print(mida.PUM)
            print()
            print("Hävisit pelin!")
            return False, aika
        
        tulvataytto(x, y, kentta, miinat)
        tulosta_pelialue(kentta)
       
def uusi_peli():
    """
    Kysyy käyttäjältä pelivalintoihin liittyvät tiedot ja aloittaa niiden perusteella uuden pelin
    """
    while True:
        print()
        print("Valittavissa olevat pelimoodit: ")
        print("==============================")
        print()
        print("1 - Vapaa valinta")
        print("Tässä pelimoodissa voit itse valita miinojen määrän ja kentän koon.")
        print("Kiireetöntä hupia haluamallasi tavalla!")
        print()
        print("2 - Haastemoodi")
        print("Haastemoodissa kentän koko ja miinojen määrä on ennalta määritelty.")
        print("Peli ottaa aikaa suorituksestasi, joten nopeus on kaikki kaikessa!")
        print("Kilpaile itseäsi tai ystäviäsi vastaan ja ansaitse paikka huipputuloksissa!")
        print()
        print("3 - Paluu")
        try:
            print()
            valinta = str(input("Valitse pelimoodi tai palaa takaisin päävalikkoon (1-3): ").strip())
        except ValueError:
            print()
            print("VIRHE: valitsemaasi toimintoa ei ole olemassa")
        except EOFError:
            print()
            print("Voit keskeyttää ohjelman suorituksen painamalla ctrl + c")
        else:
            if valinta == "1":
                print()
                print("Vapaa valinta")
                print("=============")
                kentta = mida.alusta()
                miinat = mida.alusta()
                leveys, korkeus = kentan_dimensiot()
                miina_lkm = kysy_miinat(leveys, korkeus)
                tulos, aika = pelisilmukka(leveys, korkeus, miina_lkm, kentta, miinat)
                if tulos == False:
                    print()
                    kerro_aika(aika, tulos)
                elif tulos == True:
                    print()
                    kerro_aika(aika, tulos)
            elif valinta == "2":
                print()
                print("Haastemoodi")
                print("===========")
                while True:
                    print()
                    print("Voit valita kahden eri kokoisen kentän väliltä. Ajanotto alkaa, kun olet antanut ensimmäiset koordinaatit.")
                    print()
                    print("1 - Pieni (15x15, 30 miinaa)")
                    print()
                    print("2 - Iso (20x30, 90 miinaa)")
                    print()
                    print("3 - Paluu")
                    try:
                        print()
                        valinta = str(input("Valitse haastekenttä tai palaa takaisin (1-3): ").strip())
                    except EOFError:
                        print()
                        print("Voit keskeyttää ohjelman suorituksen painamalla ctrl + c")
                    except ValueError:
                        print()
                        print("VIRHE: valitsemaasi toimintoa ei ole olemassa")
                    else:
                        if valinta == "1":
                            kentta = mida.alusta()
                            miinat = mida.alusta()
                            tulos, aika = pelisilmukka(15, 15, 30, kentta, miinat)
                            if tulos == False:
                                print()
                                kerro_aika(aika, tulos)
                            elif tulos == True:
                                print()
                                kerro_aika(aika, tulos)
                                kirjaa_huipputulokset(aika, "miinantallaaja_tulokset_pieni.txt")
                        elif valinta == "2":
                            kentta = mida.alusta()
                            miinat = mida.alusta()
                            tulos, aika = pelisilmukka(20, 30, 90, kentta, miinat)
                            if tulos == False:
                                print()
                                kerro_aika(aika, tulos)
                            elif tulos == True:
                                print()
                                kerro_aika(aika, tulos)
                                kirjaa_huipputulokset(aika, "miinantallaaja_tulokset_iso.txt")
                        elif valinta == "3":
                            break
            elif valinta == "3":
                break
            else:
                print()
                print("VIRHE: valitsemaasi toimintoa ei ole olemassa")