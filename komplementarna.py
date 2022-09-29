def nic_komplementarna(dna):
    at=dna.replace('A','t') #zmiana A na t
    ta=at.replace('T','a') #zmiana T na a
    cg=ta.replace('C','g') #zmiana C na g
    gc=cg.replace('G','c') #zmiana G na c
    return gc.upper() #zamiana ciągu małych liter na ciąg dużych liter

def odwrotnosc_komplementarna(dna):
    kompl = nic_komplementarna(dna) #najpierw tworzę nic komplementarną jeszcze nie odwróconą
    kompl_odwrotna = kompl[::-1] #czytanie nici komplementarnej od tyłu i przypisane do nowej zmiennej 
    return kompl_odwrotna


#test
if __name__ == '__main__':
    import read_it
    dna = read_it.read_DNA ('oriC.txt')
    kompl = nic_komplementarna(dna)
    print(kompl)
    print(odwrotnosc_komplementarna(dna))