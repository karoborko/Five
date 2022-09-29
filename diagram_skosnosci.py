import matplotlib.pyplot as plt 
import read_it

def sekw(genome):
    x=[i for i in range(len(genome)+1)]
    y=[]
    for i in range(len(genome)):
        if genome[i] == 'C':
            y.append(-1)
        elif genome[i] == 'G':
            y.append(1)
        else:
            y.append(0)
    z=[]
    z.append(0)
    for i in range(1,len(y)+1):
        z.append(z[i-1]+y[i-1])
    return x, z
#test i rysowanie diagramów
if __name__ == '__main__':
    
    txt = read_it.read_signs("Vibrio.txt")
    x,z=sekw(txt)
    y = txt
    plt.figure(figsize=(7,2))
    plt.plot(x,z)
    ticks = []
    ticks.append('0')
    for i in range(1,len(y)+1):
        ticks.append(txt[i-1]) 
    plt.title('Diagram skosnosci dla genomu Cholery')
    plt.xlim([0,len(txt)+1])
    plt.xlabel('position')
    plt.ylabel('sekw')
    plt.show()
    ##############################
    print("\n\n")
    e_cola = read_it.read_signs("Escherichia_coli.txt")
    x,z=sekw(e_cola)
    y = e_cola
    plt.figure(figsize=(7,2))
    plt.plot(x,z)
    ticks = []
    ticks.append('0')
    for i in range(1,len(y)+1):
        ticks.append(e_cola[i-1]) 
    plt.title('Diagram skosnosci dla genomu E.coli')
    plt.xlim([0,len(e_cola)+1])
    plt.xlabel('position')
    plt.ylabel('sekw')
    plt.show()
    
    """
    Na podstawie utworzonych diagramów, miejsce oriC jest minimum wykresu
    """
    