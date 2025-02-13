#ler o ficheiro
def adiciona_numero(ficheiro_nome):
    with open(ficheiro_nome,'r') as ficheiro:
        multiplicador=1
        acumulador=0
        while True:
            linha=ficheiro.readline();
            i=0
            if not (linha):
                break
            while i in range(len(linha)):
                caracter=linha[i]
                if not (caracter):
                    break
                if caracter.isalpha():
                    caracter.lower()
                    if caracter=='o':
                        if linha[i:i+2]=='on':
                         multiplicador=1
                        if linha[i:i+3]=='off':
                         multiplicador=0

                elif caracter.isdigit():
                    seguidos=0
                    j=i
                    while j+1<len(linha) and linha[j+1].isdigit():
                        seguidos+=1
                        j+=1
                        
                    acumulador+=(int(caracter)*10**seguidos*multiplicador)
                    
                elif (caracter=='='):
                    print(acumulador)
                i+=1


ficheiro=input("Introduza o nome do ficheiro: ")
adiciona_numero(ficheiro)
