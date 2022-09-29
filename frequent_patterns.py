import count_pattern
import read_it


def frequent_pattern(nazwa_pliku,k):
    NaszeSlowa=set() #ustalam pusty zbiór
    licz=[] #ustalam pustą liste
    Pattern=[] #ustalam pustą liste_2
    Text = read_it.read_DNA(nazwa_pliku) #wczytuje do zmiennej plik przy użyciu funkcji zimportowanej z modułu read_it
    for i in range(0,len(Text)-k): #pętla for iterowana od zera do wartosci długosci zmiennej Text minus dlugosci k-mera
        Pattern=Text[i:i+k] 
        licz.insert(count_pattern.licz_wzory_do_frequent(Text,Pattern),i) #wstawienie do listy licz zliczenie podanego wzorca i wartosci i(dlugosci k-meru)
        for j in range(0,i-1): #pętla for iterowana od 0 do wartosci i minus 1
            max=0
            if licz[j]>licz[j+1] and licz[j]>max:
                max=licz[j]
            elif licz[j]<licz[j+1] and licz[j+1]>max:
                max=licz[j+1]
    for i in range(0,len(Text)-k):
        if licz[i]==max:
            NaszeSlowa.add(Text[i:i+k]) #dodanie do zbioru wartosci o indeksie i - i+k ze zmiennej Text
    for i in range(len(NaszeSlowa)-1):
        if NaszeSlowa[i]==NaszeSlowa[i+1]:
            NaszeSlowa.remove(NaszeSlowa[i+1])
    return list(NaszeSlowa)


#test
if __name__ == '__main__':
    test_dna = read_it.read_DNA("oriC.txt")
    print(test_dna)
    for i in range(1,10):
        print(frequent_pattern("oriC.txt",i))