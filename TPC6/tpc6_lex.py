import ply.lex as lex

tokens=["NUM","MINUS","ADD","MULT","DIV"]

def t_NUM(t):
    r"\d+(\.\d+)?"
    t.value = int(t.value)
    return t

t_MINUS=r'\-'
t_ADD=r'\+'
t_MULT=r'\*'
t_DIV=r'\/'

t_ignore=" \t"

def t_error(t):
    print(f"Caractere ilegal {t.value[0]}")
    t.lexer.skip(1)
    pass

def t_newline(t):
    r"\n+"
    t.lexer.lineno +=1

lexer=lex.lex()
prox_simb = None


def proximo_token(): #serve para ler o proximo simbolo
    global prox_simb
    prox_simb=lexer.token()

    
def fator():#Lê o valor dos números retorna-o e lê o próximo token
    global prox_simb
    if prox_simb and prox_simb.type=="NUM":
        valor=prox_simb.value
        proximo_token()
        return valor

def termo():
    global prox_simb
    resultado=fator() #É esperado um numero antes da operação

    while prox_simb and prox_simb.type in ("DIV","MULT"):
        if prox_simb.type=="DIV":
            proximo_token()
            resultado/=fator()
        if prox_simb.type=="MULT":
            proximo_token()
            resultado*=fator()
    
    return resultado

def expressao():
    global prox_simb
    resultado=termo()

    while prox_simb and prox_simb.type in ("ADD","MINUS" ):
        if prox_simb.type=="ADD":
            proximo_token()
            resultado+=termo()
        elif prox_simb.type=="MINUS":
            proximo_token()
            resultado-=termo()

    return resultado



def analisar(frase):
    global prox_simb
    lexer.input(frase)
    proximo_token() #primeiro token
    return expressao()


while (True):
    frase=input("Dá-me a frase: ")
    print("Resultado: " + str(analisar(frase)))
