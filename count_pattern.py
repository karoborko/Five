def count_patterns(Text, Pattern):
    zlicz = 0
    gdzie = []
    k_mer = len(Pattern)
    for i in range(len(Text)-k_mer):
        if (Text[i:(i+k_mer)] == Pattern):
            zlicz +=1
            gdzie.append(i)
    return zlicz, gdzie


def licz_wzory_do_frequent(Text,Pattern):
    licz=0
    for i in range(0,len(Text)-len(Pattern)):
        if Text[i:i+len(Pattern)]==Pattern:
            licz+=1
    return licz



#test
if __name__ == '__main__':
    import read_it
    dna = read_it.read_DNA ('oriC.txt')
    wzor = 'atgatcaag'
    wzor = wzor.upper()
    print(dna, '\nszukamy: ', wzor)
    ile, lista_gdzie= count_patterns(dna, wzor)
    print('znaleziono', ile, 'wystapien', wzor)
    for i in range(ile):
        print(lista_gdzie[i], dna[lista_gdzie[i]:lista_gdzie[i]])