def zad41():
    with open('Dane_PR2/sygnaly.txt','r') as plik1:
        
        i=1
        for linia in plik1:
            
            if i%40==0:
                print(linia[9],end='')
            i+=1
        
def zad42():
    with open('Dane_PR2/sygnaly.txt','r') as plik2:
    #Ilosc - zmienna odpowiadajaca za ilosc lini do wczytania
        ilosc=1000
        maks=0
        slowo=""
    
        for i in range(ilosc):
            znaki=[]
            linia = plik2.readline()
            #wpisywanie znakow z lini do listy
            for znak in linia:
                if not znak in znaki:
                    znaki.append(znak)
                if '\n' in znaki:
                    znaki.remove('\n')
            znaki.sort()
            if len(znaki)>maks:
                maks=len(znaki)
                slowo=linia
            
    
    print(slowo + str(maks))

def zad43():
    with open('Dane_PR2/sygnaly.txt','r') as plik3:
    #Ilosc - zmienna odpowiadajaca za ilosc lini do wczytania
        ilosc=1000
        for i in range(ilosc):
            linia=plik3.readline().rstrip()
            maks=0
            mini=10000
            
            for znak in linia:
                if ord(znak)>maks: #zmiana na unikod w celu łatwiejszego porównania liter
                    maks=ord(znak)
                if ord(znak)<mini:
                    mini=ord(znak)
                delta=maks-mini
            if delta<=10:
                print(linia) 
          
#USER INTERFACE
print('*********************************')

wybor = int(input('WYBIERZ PODPUNKT ZADANIA OD 1 do 3: '))
print('*********************************')
print('WYJŚCIE:')
print()
if wybor == 1:
    zad41()
elif wybor == 2:
    zad42()
elif wybor == 3:
    zad43()




