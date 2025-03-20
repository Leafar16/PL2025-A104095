# TPC3: Conversor de Markdown para HTML

## Identificação
**Autor:** Rafael Pereira  
**Nº:** 104095  
**Foto**: ![Rafael Pereira](../rafael.jpeg)  

## Propósito
Esta pasta serve para armazenar o TPC3, que consiste na implementação de um conversor de Markdown para HTML. O código permite converter elementos básicos de Markdown em suas versões equivalentes em HTML.

## Resumo
- O código implementa funções que utilizam expressões regulares para converter elementos Markdown para HTML.
- Converte cabeçalhos, negrito, itálico, links e imagens.
- O processamento é feito em etapas para garantir a correta conversão.
- No final, retorna o HTML correspondente ao texto de entrada.
- **O projeto está incompleto**, pois ainda falta a implementação da conversão de listas.

## Implementação

### 1. Elementos Suportados
O conversor atualmente suporta os seguintes elementos:
- **Negrito (`**texto**`)** → `<b>texto</b>`
- **Itálico (`*texto*`)** → `<i>texto</i>`
- **Links (`[texto](URL)`)** → `<a href='URL'>texto</a>`
- **Imagens (`![alt](URL)`)** → `<img src='URL' alt='alt'>`
- **Cabeçalhos (`# texto`)** → `<h1>texto</h1>`

### 2. Funções de Substituição
O código usa expressões regulares para identificar e substituir os elementos Markdown:
- **`sub_cabecalho(texto)`**: Converte `# título` em `<h1>título</h1>`.
- **`sub_bold(texto)`**: Converte `**negrito**` em `<b>negrito</b>`.
- **`sub_italico(texto)`**: Converte `*itálico*` em `<i>itálico</i>`.
- **`sub_link(texto)`**: Converte `[texto](URL)` em `<a href='URL'>texto</a>`.
- **`sub_imagem(texto)`**: Converte `![alt](URL)` em `<img src='URL' alt='alt'>`.

### 3. Aplicação das Substituições
A função principal `aplicar_formatacao(texto)` executa as substituições na seguinte ordem:
1. `sub_cabecalho(texto)`
2. `sub_bold(texto)`
3. `sub_italico(texto)`
4. `sub_imagem(texto)`
5. `sub_link(texto)`

Essa ordem garante que imagens sejam processadas antes de links e que negrito seja processado antes de itálico para evitar sobreposição de marcações.

### 4. Execução do Programa
O código contém um exemplo de texto Markdown e exibe a saída HTML correspondente.

### 5. Implementação Incompleta
Atualmente, o código **não** possui suporte para listas em Markdown (`- item` ou `1. item`). Esse recurso ainda precisa ser desenvolvido para converter listas em elementos `<ul>` e `<li>`.

## Exemplo de Entrada e Saída

### **Entrada**
```markdown
**negrito** *itálico* [link](http://www.google.com) ![imagem](http://www.google.com)
```

### **Saída**
```html
<b>negrito</b> <i>itálico</i> <a href='http://www.google.com'>link</a> <img src='http://www.google.com' alt='imagem'>
```

## Código
- [Código-fonte](conversorHTML.py)

