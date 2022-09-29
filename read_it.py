def read_lines(nazwa_pliku):
    try:
        plik = open(nazwa_pliku, 'r')
        zawartosc=plik.readlines()
    except IOError:
        print ("\n\nBłąd dostępu do pliku. STOP?")
        zawartosc=[]
    return zawartosc


def read_signs(nazwa_pliku):
    try:
        plik = open(nazwa_pliku, 'r')
        zawartosc = plik.read()
    except IOError:
        print("\n\nBłąd dostepu do pliku.STOP")
        zawartosc=[]
    return zawartosc

def read_DNA(nazwa_pliku):
    try:
        plik = open(nazwa_pliku, 'r')
        rob = plik.read()
        rob = rob.split()
        zawartosc = rob[0]
        for i in range(1, len(rob)):
            zawartosc += rob[i]
    except IOError:
        print ("\n\nBłąd dostępu do pliku. STOP?")
        zawartosc=[]
    return zawartosc


if __name__ == '__main__':
    print("testy funkcji czytajacych z pliku")
    nazwa_pliku = 'oriC.txt'
    tekst = read_lines(nazwa_pliku)
    print("\n\n analiza wczytanej informacji z pliku")
    ile = len(tekst)
    rozmiar = tekst.__sizeof__()
    if ile > 0:
        print("\n rozmiar wczytanej informacji", rozmiar)
        print("\nilosc wczytanych elementow",ile)
        print("\npierwsze 10 elementow:\n", tekst[0:10])
        print("\nostatnie 10 elementow:\n", tekst[-10:])
    tekst = read_DNA(nazwa_pliku)
    print("\nanaliza czytanej liniami informacji z pliku")
    ile = len(tekst)
    rozmiar = tekst.__sizeof__()
    if ile > 0:
        print("\n rozmiar wczytanej informacji", rozmiar)
        print("\nilosc wczytanych elementow",ile)
        print("\npierwsze 10 elementow:\n", tekst[0:10])
        print("\nostatnie 10 elementow:\n", tekst[-10:])
        