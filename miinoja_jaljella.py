def miinoja_jaljella(leveys, korkeus, kentta, miinat, miina_lkm):
    """
    Tarkistaa jokaista miinaa ympäröivien avaamattomien ruutujen määrän.
    Jos avaamattomien ruutujen määrä on nolla, on miina "löydetty".
    Ilmoittaa jäljellä olevien miinojen määrän käyttäjälle.
    Ottaa argumenteikseen kentän leveyden, korkeuden, kentän, miinakentän ja miinojen lukumäärän.
    """
    #Ei toimi kunnolla, koska jos vierekkäisissä ruuduissa on molemmissa miina, ei laskuri tajua sitä ja ilmoittaa väärän tuloksen.
    miinoja = miina_lkm
    for y in range(1, korkeus + 1):
        for x in range(1, leveys + 1):
            if miinat[y][x] == " x":
                if y == 1 and x == 1:
                    n5 = kentta[y][x + 1].count(" @")
                    n7 = kentta[y + 1][x].count(" @")
                    n8 = kentta[y + 1][x + 1].count(" @")
                    avaamattomat_ruudut = n5 + n7 + n8
                    if avaamattomat_ruudut == 0:
                        miinoja -= 1
                    else:
                        continue
                elif y == korkeus and x == leveys:
                    n1 = kentta[y - 1][x - 1].count(" @")
                    n2 = kentta[y - 1][x].count(" @")
                    n4 = kentta[y][x - 1].count(" @")
                    avaamattomat_ruudut = n1 + n2 + n4
                    if avaamattomat_ruudut == 0:
                        miinoja -= 1
                    else:
                        continue
                elif y == 1 and x == leveys:
                    n4 = kentta[y][x - 1].count(" @")
                    n6 = kentta[y + 1][x - 1].count(" @")
                    n7 = kentta[y + 1][x].count(" @")
                    avaamattomat_ruudut = n4 + n6 + n6
                    if avaamattomat_ruudut == 0:
                        miinoja -= 1
                    else:
                        continue
                elif x == 1 and y == korkeus:
                    n2 = kentta[y - 1][x].count(" @")
                    n3 = kentta[y - 1][x + 1].count(" @")
                    n5 = kentta[y][x + 1].count(" @")
                    avaamattomat_ruudut = n2 + n3 + n5
                    if avaamattomat_ruudut == 0:
                        miinoja -= 1
                    else:
                        continue
                elif y == 1:
                    n4 = kentta[y][x - 1].count(" @")
                    n5 = kentta[y][x + 1].count(" @")
                    n6 = kentta[y + 1][x - 1].count(" @")
                    n7 = kentta[y + 1][x].count(" @")
                    n8 = kentta[y + 1][x + 1].count(" @")
                    avaamattomat_ruudut = n4 + n5 + n6 + n7 + n8
                    if avaamattomat_ruudut == 0:
                        miinoja -= 1
                    else:
                        continue
                elif x == 1:
                    n2 = kentta[y - 1][x].count(" @")
                    n3 = kentta[y - 1][x + 1].count(" @")
                    n5 = kentta[y][x + 1].count(" @")
                    n7 = kentta[y + 1][x].count(" @")
                    n8 = kentta[y + 1][x + 1].count(" @")
                    avaamattomat_ruudut = n2 + n3 + n5 + n7 + n8
                    if avaamattomat_ruudut == 0:
                        miinoja -= 1
                    else:
                        continue
                elif y == korkeus:
                    n1 = kentta[y - 1][x - 1].count(" @")
                    n2 = kentta[y - 1][x].count(" @")
                    n4 = kentta[y][x - 1].count(" @")
                    n3 = kentta[y - 1][x + 1].count(" @")
                    n5 = kentta[y][x + 1].count(" @")
                    avaamattomat_ruudut = n1 + n2 + n3 + n4 + n5
                    if avaamattomat_ruudut == 0:
                        miinoja -= 1
                    else:
                        continue
                elif x == leveys:
                    n1 = kentta[y - 1][x - 1].count(" @")
                    n2 = kentta[y - 1][x].count(" @")
                    n4 = kentta[y][x - 1].count(" @")
                    n6 = kentta[y + 1][x - 1].count(" @")
                    n7 = kentta[y + 1][x].count(" @")
                    avaamattomat_ruudut = n1 + n2 + n4 + n6 + n7
                    if avaamattomat_ruudut == 0:
                        miinoja -= 1
                    else:
                        continue
                else:
                    n1 = kentta[y - 1][x - 1].count(" @")
                    n2 = kentta[y - 1][x].count(" @")
                    n3 = kentta[y - 1][x + 1].count(" @")
                    n4 = kentta[y][x - 1].count(" @")
                    n5 = kentta[y][x + 1].count(" @")
                    n6 = kentta[y + 1][x - 1].count(" @")
                    n7 = kentta[y + 1][x].count(" @")
                    n8 = kentta[y + 1][x + 1].count(" @")
                    avaamattomat_ruudut = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
                    if avaamattomat_ruudut == 0:
                        miinoja -= 1
                    else:
                        continue
            else:
                continue
    print()
    print("Miinoja jäljellä {} kpl".format(miinoja))