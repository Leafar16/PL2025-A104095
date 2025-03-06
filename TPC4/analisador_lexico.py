import re
import ply.lex as lex

frase_exemplo="""# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000"""

tokens=("COMMENT", #comentario
        "NUMBER",  #numero
        "NAME", 
        "OPENBR",
        "CLOSEBR",
        "DF",
        "PF",
        "VAR",
        "SELECT",
        "LIMIT",
        "WHERE",
        "OPT")

def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t

t_ignore=" \t"

def t_error(t):
    print(f"Caractere ilegal {t.value[0]}")
    t.lexer.skip(1)
    pass

def t_newline(t):
    r"\n+"
    t.lexer.lineno +=1

t_COMMENT = r"\#.*"
t_OPENBR = r"\{"
t_CLOSEBR = r"\}"
t_DF = r"(dbo|foaf):\w+"
t_PF = r"\."
t_VAR = r"\?\w+"
t_NAME = r"\"[^\"]+\"\@\w+"
t_SELECT = r"select"
t_LIMIT = r"LIMIT"
t_WHERE = r"where"
t_OPT= r"\w"

lexer=lex.lex()

lexer.input(frase_exemplo)

while r:=lexer.token():
    print(r)
