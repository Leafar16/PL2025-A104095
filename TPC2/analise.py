import re

#estruturas de dados para guardar resultados
compositores=[]
periodo_nome={}
periodo_obras={}

#abrir o ficheiro
with open("obras.csv", "r") as f:
    content = f.read()

#normalização dos nomes
def normaliza_nomes(compositor):
        r=r'([\S]*), *([\S ]*)'
        m=re.match(r, compositor)
        if(m):
            return m.group(2) + " " + m.group(1)
        else:
            return compositor

#parsing dos dados
pattern=r'^([^;]*);"(?:([^"]|"")*|[^;]+)";([^;]*);([^;]*);([^;]*);([^;]*);([^\s]*)'

resultados=re.findall(pattern, content, re.MULTILINE)

for resultado in resultados:
    nome=resultado[0]
    desc=resultado[1]
    anoCriacao=resultado[2]
    periodo=resultado[3]
    compositor=normaliza_nomes(resultado[4])
    duracao=resultado[5]
    _id=resultado[6]
    compositores.append(compositor)
    if periodo in periodo_nome:
        periodo_nome[periodo]=periodo_nome[periodo]+1
    else:
        periodo_nome[periodo]=1

    if periodo in periodo_obras:
        periodo_obras[periodo].append(nome)
    else:
        periodo_obras[periodo]=[nome]

def query1():
    return sorted(compositores)

def query2():
    for periodo in periodo_nome:
        print(periodo, periodo_nome[periodo])

def query3():
    for periodo in periodo_obras:
        print(periodo+" :")
        print(sorted(periodo_obras[periodo]))
        print()


if __name__== "__main__":
    input=input("Qual query queres executar? (1,2 ou 3) \n")
    input=int(input)
    if (input==1):
        print(query1())
    elif(input==2):
        query2()
    elif(input==3):
        query3()
    else:
        print("Input inválido")