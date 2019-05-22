def zad41():
    with open('Dane_PR2/sygnaly.txt','r') as plik1:
        
        i=1
        for linia in plik1:
            
            if i%40==0:
                print(linia[9],end='')
            i+=1
        

zad41()