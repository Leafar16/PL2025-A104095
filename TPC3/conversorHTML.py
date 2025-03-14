import re

texto="**negrito** *italico* [link](http://www.google.com) ![imagem](http://www.google.com)"
#cabecalho
def sub_cabecalho(texto):
    pattern=r"^# (?P<conteudo>[\d\w ]+)"
    return re.sub(pattern,r"<h1>\g<conteudo></h1>",texto)

#bold
def sub_bold(texto): #usar bold primeiro
    pattern=r"\*\*(?P<conteudo>[^\s]*[\d\w ]+[^\s]*)\*\*"
    return re.sub(pattern,r"<b>\g<conteudo></b>",texto)

#italico
def sub_italico(texto):
    pattern=r"\*(?P<conteudo>[^\s]*[\d\w ]+[^\s]*)\*"
    return re.sub(pattern,r"<i>\g<conteudo></i>",texto)

#link
def sub_link(texto):
    pattern=r"\[(?P<texto>[^\]]+)\]\((?P<link>[^\)]+)\)"
    return re.sub(pattern,r"<a href='\g<link>'>\g<texto></a>",texto)

#imagem
def sub_imagem(texto): #antes do link
    pattern=r"\!\[(?P<texto>[^\]]+)\]\((?P<link>[^\)]+)\)"
    return re.sub(pattern,r"<img src='\g<link>' alt='\g<texto>'>",texto)

#lista
def sub_lista(texto):
    undefined = True


def aplicar_formatacao(texto):
    texto = sub_cabecalho(texto)
    texto = sub_bold(texto)
    texto = sub_italico(texto)
    texto = sub_imagem(texto)
    texto = sub_link(texto)
    #texto = sub_lista(texto)
    return texto

print(aplicar_formatacao(texto))