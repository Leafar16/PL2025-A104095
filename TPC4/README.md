# TPC4: Analisador Léxico

## Identificação
**Autor:** Rafael Pereira  
**Nº:** 104095  
**Foto**: ![Rafael Pereira](../rafael.jpeg)  

## Propósito
Esta pasta serve para armazenar o TPC4, que decorreu na semana de 28 de fevereiro a 7 de março de 2025.

## Resumo
- O código realiza a tokenização de uma certa linguagem, identificando diferentes tipos de componentes sintáticos.
- Ele lida com comentários, palavras-chave, variáveis, números, literais, delimitadores e operadores.
- A saída é uma lista de tokens reconhecidos, com seus respectivos valores.

## Implementação
### Explicação Detalhada

1. **Definição dos Tokens:**
   - O código define uma lista de **tokens** que o lexer reconhecerá.
   - Exemplos de tokens:
     - **COMMENT**: Representa comentários no código (começam com `#`).
     - **NUMBER**: Captura números inteiros.
     - **NAME**: Captura strings com tags de idioma, como `"Chuck Berry"@en`.
     - **OPENBR / CLOSEBR**: Representam chaves `{}` usadas na estrutura SPARQL.
     - **DF**: Identifica prefixos como `dbo:` ou `foaf:`.
     - **PF**: Representa um ponto final (`.`), comum em declarações SPARQL.
     - **VAR**: Captura variáveis precedidas por `?`, como `?nome`.
     - **SELECT, WHERE, LIMIT**: Reconhece palavras-chave essenciais para consultas SPARQL.
     - **OPT**: Representa uma palavra qualquer (atualmente com regex `\w`).

2. **Funções de Tratamento:**
   - **`t_NUMBER`**: Converte números extraídos para inteiros.
   - **`t_ignore`**: Define espaços e tabulações como ignoráveis.
   - **`t_error`**: Garante que caracteres ilegais sejam ignorados, imprimindo um aviso.
   - **`t_newline`**: Atualiza a contagem de linhas ao encontrar quebras de linha (`\n`).

3. **Execução do Lexer:**
   - O lexer é criado usando `lex.lex()`.
   - A consulta SPARQL de exemplo é fornecida como entrada ao lexer.
   - O código itera sobre os tokens gerados e os imprime no console.

## Exemplo de Entrada e Saída

### **Entrada**
```sparql
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
```

### **Saída**
```
LexToken(COMMENT,'# DBPedia: obras de Chuck Berry',1,0)
LexToken(SELECT,'select',2,32)
LexToken(VAR,'?nome',2,39)
LexToken(VAR,'?desc',2,45)
LexToken(WHERE,'where',2,51)
LexToken(OPENBR,'{',2,57)
LexToken(VAR,'?s',3,59)
LexToken(OPT,'a',3,62)
LexToken(DF,'dbo:MusicalArtist',3,64)
LexToken(PF,'.',3,81)
LexToken(VAR,'?s',4,83)
LexToken(DF,'foaf:name',4,86)
LexToken(NAME,'"Chuck Berry"@en',4,96)
LexToken(PF,'.',4,113)
LexToken(VAR,'?w',5,115)
LexToken(DF,'dbo:artist',5,118)
LexToken(VAR,'?s',5,129)
LexToken(PF,'.',5,131)
LexToken(VAR,'?w',6,133)
LexToken(DF,'foaf:name',6,136)
LexToken(VAR,'?nome',6,146)
LexToken(PF,'.',6,151)
LexToken(VAR,'?w',7,153)
LexToken(DF,'dbo:abstract',7,156)
LexToken(VAR,'?desc',7,169)
LexToken(CLOSEBR,'}',8,175)
LexToken(LIMIT,'LIMIT',8,177)
LexToken(NUMBER,1000,8,183)
```


## Código
- [Código-fonte](analisador_lexico.py)
