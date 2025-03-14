import json
import ply.lex as lex

stock={}
# FICHEIRO JSON
with open("stock.json","r") as f:
    produtos=json.load(f)

    l_p=produtos["stock"]
    for p in l_p:
        stock[p["cod"]]=p

def salvar_stock():
    with open("stock.json","w") as f:
        json.dump({"stock": list(stock.values())},f,indent=4,ensure_ascii=False)

#LEXICO    
states=(
    ("moedas","exclusive"),
    ("selecionar","exclusive"),
)

current_money=0
current_selection=""

tokens=["SELECIONAR",
        "SAIR",
        "MOEDA",
        "NUMERO",
        "ARTIGO",
        "VIRGULA"]

def t_ANY_SELECIONAR(t):
    r'(?i)SELECIONAR'
    t.lexer.begin("selecionar")
    return t

def t_selecionar_ARTIGO(t):
    r'(?i)(?P<codigo>A\d+)'
    global current_selection
    current_selection=t.lexer.lexmatch.group("codigo")
    return t

def t_ANY_MOEDA(t):
    r'(?i)MOEDA'
    t.lexer.begin("moedas")
    return t

def t_moedas_NUMERO(t):
    r'(?P<valor_c>50|20|10|5|2|1)c|(?P<valor_e>2|1)e'    
    global current_money
    if(t.lexer.lexmatch.group("valor_c")):
        current_money+=float(t.lexer.lexmatch.group("valor_c"))*0.01
    else:
        current_money+=int(t.lexer.lexmatch.group("valor_e"))

    return t

def t_ANY_SAIR(t):
    r'(?i)SAIR'
    return t


t_ANY_ignore=r' +'

t_ANY_VIRGULA=r'\,'

def t_ANY_newline(t):
    r'\n'
    t.lineno+=1
    pass

def t_ANY_error(t):
    print("Caractere ilegal na linha: " + str(t.lineno) + " ,"+t.value[0])
    t.lexer.skip(1)
    pass

lexer=lex.lex()

def calcula_moeda(frase):
    lexer.input(frase)

    while r:=lexer.token():
        pass
        

def escolhe_artigo(frase):
    lexer.input(frase)

    while r:=lexer.token():
        pass
        
def devolve_dinheiro(dinheiro):
    moedas = {"2e": 0, "1e": 0, "50c": 0, "20c": 0, "10c": 0, "5c": 0, "2c": 0, "1c": 0}
    while dinheiro != 0:
        if dinheiro >= 2:
            moedas["2e"] += 1
            dinheiro -= 2
        elif dinheiro >= 1:
            moedas["1e"] += 1
            dinheiro -= 1
        elif dinheiro >= 0.5:
            moedas["50c"] += 1
            dinheiro -= 0.5
        elif dinheiro >= 0.2:
            moedas["20c"] += 1
            dinheiro -= 0.2
        elif dinheiro >= 0.1:
            moedas["10c"] += 1
            dinheiro -= 0.1
        elif dinheiro >= 0.05:
            moedas["5c"] += 1
            dinheiro -= 0.05
        elif dinheiro >= 0.02:
            moedas["2c"] += 1
            dinheiro -= 0.02
        elif dinheiro >= 0.01:
            moedas["1c"] += 1
            dinheiro -= 0.01
        dinheiro = round(dinheiro, 2)  
    return moedas



#MAIN LOOP

loop=True

while(loop):
    frase=input()
    print()
    comando=frase.split(" ")[0]
    if comando=="LISTAR" or comando=="listar":
        print(f"{'cod':^5} | {'nome':^20} | {'quantidade':^10} | {'preço':^5}")
        print("---------------------------------")
        for key, value in stock.items():
            print(f"{value['cod']:^5} | {value['nome']:^20} | {value['quant']:^10} | {value['preco']:^5}")

    elif comando=="moeda" or comando=="MOEDA":
        calcula_moeda(frase)
        print("Saldo Atual: "+ str(current_money))

    elif comando=="saldo" or comando=="SALDO":
        print("Saldo Atual: "+str(current_money))

    elif ((comando=="selecionar" or comando=="SELECIONAR") and len(frase.split(" "))==2):
        current_selection=""
        escolhe_artigo(frase)
        if(current_selection == ""):
           print("Artigo inválido")
           continue
        current_selection=(current_selection).upper()
        if(current_selection in stock.keys()):
            if stock[current_selection]["quant"]!=0:
                if stock[current_selection]["preco"]<=current_money:
                    print("Pode retirar o produto dispensado: " +stock[current_selection]["nome"] )
                    current_money-=stock[current_selection]["preco"]
                    current_money=round(current_money,2)
                    stock[current_selection]["quant"]-=1
                    salvar_stock()
                else:
                    print("Saldo insuficiente para satisfazer o pedido")
                    print(f"Saldo = {str(current_money)}; Pedido = "+str(stock[current_selection]["preco"]))
            else:
                print("Artigo "+  stock[current_selection]['nome']+" sem stock")
                    

    elif (comando==r"sair" or comando=="SAIR"):
        troco=devolve_dinheiro(current_money)
        string=""

        for key,value in troco.items():
            if value!=0:
                string+=f"{value}x {key}, "
        string = string[:-2] + "."

        print("Pode retirar o troco: "+string)
        print("Até à próxima")
        loop=False
    else:
        print("Escolhe outra ação")
        