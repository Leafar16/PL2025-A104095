# TPC5: Máquina de Vending

## Identificação
**Autor:** Rafael Pereira  
**Nº:** 104095  
**Foto**: ![Rafael Pereira](../rafael.jpeg)  

## Propósito
Esta pasta serve para armazenar o TPC5, que decorreu na semana de 7 de fevereiro a 14 de março de 2025.

## Resumo

Este programa simula uma máquina de vending (máquina de venda automática) que interage com o utilizador através de comandos de texto. As funcionalidades principais incluem o controlo de stock de produtos, inserção de moedas, seleção de produtos e devolução de troco.

## Funcionalidades

### 1. **Carregamento e Manipulação de Stock**
   - O programa carrega o stock de produtos a partir de um ficheiro JSON (`stock.json`) que contém informações sobre os produtos disponíveis, como:
     - **Código do produto**
     - **Nome do produto**
     - **Quantidade disponível**
     - **Preço**
   - O stock é atualizado ao longo do programa e é salvo novamente no ficheiro JSON quando o programa termina.

### 2. **Leitura e Processamento de Comandos (usando PLY)**
   - O programa utiliza o módulo **PLY** (Python Lex-Yacc) para criar um analisador léxico (lexer), que reconhece comandos do utilizador, como:
     - `LISTAR`
     - `MOEDA`
     - `SELECIONAR`
     - `SAIR`
   - O lexer permite que a máquina identifique e processe comandos relacionados a:
     - **Inserção de moedas**
     - **Seleção de produtos**
     - **Controlo de saldo**

### 3. **Comandos Disponíveis**
   - **LISTAR**: Exibe todos os produtos disponíveis no stock, mostrando:
     - Código
     - Nome
     - Quantidade
     - Preço
   - **MOEDA**: Permite ao utilizador inserir moedas (como `1e`, `50c`, `20c`) e atualiza o saldo da máquina.
   - **SELECIONAR**: Permite ao utilizador selecionar um produto para compra, verificando:
     - Se há stock disponível.
     - Se o saldo é suficiente para a compra.
   - **SALDO**: Exibe o saldo atual na máquina.
   - **SAIR**: Calcula e devolve o troco (se houver), e termina o programa.


## Código
- [Código-fonte](vending_machine.py)
- [Ficheiro JSON](stock.json)