# TPC6: Analisador Sintático

## Identificação
**Autor:** Rafael Pereira  
**Nº:** 104095  
**Foto**: ![Rafael Pereira](../rafael.jpeg)  

## Propósito
Esta pasta serve para armazenar o TPC6, que decorreu na semana de 14 a 21 de março de 2025.

## Resumo
- O código implementa um analisador léxico e sintático simples para expressões matemáticas.
- Identifica operadores básicos de soma, subtração, multiplicação e divisão, além de números.
- O lexer converte a entrada em tokens, e o parser avalia a expressão utilizando regras gramaticais estruturadas.
- O resultado é o valor numérico da expressão dada.

## Implementação

### 1. Definição dos Tokens
O analisador léxico é construído utilizando a biblioteca `ply.lex`. Os tokens reconhecidos são:
- **NUM**: Representa números inteiros e decimais.
- **MINUS (-)**: Representa o operador de subtração.
- **ADD (+)**: Representa o operador de adição.
- **MULT (*)**: Representa o operador de multiplicação.
- **DIV (/)**: Representa o operador de divisão.

Os espaços em branco e tabulações são ignorados, e caracteres inválidos são sinalizados.

### 2. Funções do Lexer
- **`t_NUM`**: Reconhece números inteiros e decimais, convertendo-os em inteiros.
- **`t_ignore`**: Ignora espaços e tabulações.
- **`t_error`**: Imprime uma mensagem e ignora caracteres inválidos.
- **`t_newline`**: Atualiza a contagem de linhas ao encontrar quebras de linha (`\n`).

### 3. Parser e Avaliação de Expressões
A análise sintática segue a seguinte gramática:
1. **expressao** → **termo** (`+` | `-`) **termo** 
2. **termo** → **fator** (`*` | `/`) **fator** 
3. **fator** → **NUM**

- **`proximo_token`**: Obtém o próximo token da entrada.
- **`fator`**: Retorna o valor de um número e avança para o próximo token.
- **`termo`**: Avalia multiplicações e divisões antes de somas e subtrações.
- **`expressao`**: Avalia a expressão completa seguindo a precedência correta dos operadores.

### 4. Execução do Programa
O programa solicita uma expressão matemática ao usuário, a analisa e exibe o resultado no console.

## Exemplo de Entrada e Saída

### **Entrada**
```plaintext
3 + 5 * 2 - 8 / 4
```

### **Saída**
```plaintext
Resultado: 10
```

## Código
- [Código-fonte](analisador_lexico.py)