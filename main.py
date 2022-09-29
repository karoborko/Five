import read_it
import count_pattern
import frequent_patterns
import komplementarna 

wzorzec = 'ATGATCAAG' 
dna_Vibrio = read_it.read_signs('Vibrio.txt')
oriC = read_it.read_signs("oriC.txt")

print("najczestsze wzorce \n")
for i in range(1,21):
    print(i, frequent_patterns.frequent_pattern("oriC.txt",i)) #wyszukiwanie najczęstszych wzorców w oriC o długosci 1-20
    
#################################################################

nic_komp = komplementarna.nic_komplementarna(oriC) #tworzenie nici komplementarnej
nic_komp_odwr = komplementarna.odwrotnosc_komplementarna(oriC) #tworzenie nici komplementranie odwróconej
print("nic DNA\n",oriC,"\n")
print("nic komplementarna \n",nic_komp,"\n")
print("nic komplementarnie odwrocona \n",nic_komp_odwr,"\n")



################################################################
print("szukamy: ", wzorzec)
print("ile razy i gdzie występuje wystepuje: ", count_pattern.count_patterns(oriC, wzorzec)) #zliczenie ile razy wzorzec występuje w sekwencji (pierwsza liczba) i na jakich pozycjach

############################################################
print('\nszukamy wzorca w sekwencji Vibrio: ', wzorzec)
ile, lista_gdzie = count_pattern.count_patterns(dna_Vibrio, wzorzec)
print('znaleziono', ile, 'wystapien', wzorzec)
for i in range(ile):
    a = lista_gdzie[i]
    b = dna_Vibrio[lista_gdzie[i]:lista_gdzie[i]]
    print("Miejsce, w ktorym wystepuje wzorzec:",a,b) 
for i in range(2,ile):
    if lista_gdzie[i] - lista_gdzie[i-2] < 500:
        print('\n oriC jest w otoczeniu od', lista_gdzie[i-2], 'do', lista_gdzie[i])

