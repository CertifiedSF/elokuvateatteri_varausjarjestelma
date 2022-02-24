# Elokuvateatterin varausjärjestelmä
# Python perusteet kurssin lopputyö (Perusteiden testi)

def lisaaElokuva(elokuva: str):
    with open("elokuvat.txt","a") as elokuvat:
        elokuvat.write(elokuva+"\n")

def lisaaNaytos(elokuva: str, sali: str, aika: str):
    with open("naytokset.txt","a") as naytokset:
        naytokset.write(elokuva+","+sali+","+aika+"\n")

def riviMaara(tiedosto: str):
    return sum(1 for line in open(tiedosto+".txt"))

def tallennaVaraus(sali: str, data: list, koko: int):
    if riviMaara(sali) < koko:
        with open(sali+".txt","a") as varaukset:
            varaukset.write(data[2].strip()+", "+data[0]+", "+data[1]+"\n")
            print("Varaus lisätty.")
    else:
        print(f"Varausta ei voitu tehdä, {sali} on täynnä.")

def teeVaraus():

    listaaNaytokset()

    valinta = int(input("Valitse näytös (numero):\n> "))-1
    with open("naytokset.txt") as naytokset:
        for i, line in enumerate(naytokset):
            if i == valinta:
                rivi = line

    data = rivi.split(",")
    if data[1] == "Sali 1":
        tallennaVaraus(data[1], data, 5)


    elif data[1] == "Sali 2":
        tallennaVaraus(data[1], data, 8)

    elif data[1] == "Sali 3":
        tallennaVaraus(data[1], data, 10)
    print("")

def selaaVarauksia():
    with open("Sali 1.txt") as varaukset:
        for i in varaukset:
            print(i.strip())

    with open("Sali 2.txt") as varaukset:
        for i in varaukset:
            print(i.strip())

    with open("Sali 3.txt") as varaukset:
        for i in varaukset:
            print(i.strip())
    print("")

def listaaElokuvat():
    print("Lista elokuvista:")
    with open("elokuvat.txt") as elokuvat:  #   Vaatii, että tiedostot ovat olemassa ennestään
        for i in elokuvat:
            print("- "+i.strip())
    print("")

def listaaNaytokset():
    print("Lista näytöksistä:")
    nro = 1
    with open("naytokset.txt") as naytokset:
        for i in naytokset:
            print(str(nro)+". "+i.strip())
            nro += 1
    print("")

kayttaja = input("Asiakas vai ylläpitäjä? (A/Y): ")

if kayttaja == "Y" or kayttaja == "y":
    while True:
        print("0. Lopeta")
        print("1. Lisää elokuva")
        print("2. Lisää näytös")
        print("3. Listaa elokuvat")
        print("4. Listaa näytökset")
        print("5. Selaa varauksia")
        print("")
        syote = input("Mitä haluat tehdä? (Anna numero)\n> ")
        if syote == "0":
            print("Ohjelma suljetaan.")
            break
        elif syote == "1":
            elokuva = input("Anna lisättävän elokuvan nimi:\n> ")
            lisaaElokuva(elokuva)
        elif syote == "2":
            syote = input("Anna elokuvan nimi, Sali ja ajankohta (erota pilkulla):\n> ")
            data = syote.split(",")
            lisaaNaytos(data[0],data[1],data[2])
        elif syote == "3":
            listaaElokuvat()
        elif syote == "4":
            listaaNaytokset()
        elif syote == "5":
            selaaVarauksia() 
        else:
            print("Virheellinen syöte, yritä uudelleen.")

elif kayttaja == "A" or kayttaja == "a":
    while True:
        print("0. Lopeta")
        print("1. Varaa paikka")
        print("2. Listaa elokuvat")
        print("3. Listaa näytökset")
        print("")
        syote = input("Mitä haluat tehdä? (Anna numero)\n> ")
        if syote == "0":
            print("Ohjelma suljetaan.")
            break
        elif syote == "1":
            teeVaraus()
        elif syote == "2":
            listaaElokuvat()
        elif syote == "3":
            listaaNaytokset()
        else:
            print("Virheellinen syöte, yritä uudelleen.")
else:
    print("Virheellinen syöte, ohjelma suljetaan.")
