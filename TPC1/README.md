# Somador On/Off

## Identificação
**Autor:** Rafael Pereira
**Nº:** 104095  
**Foto**:![Rafael Pereira](../rafael.jpeg)

## Propósito 
Esta pasta serve para armazenar o TPC1, que decorreu na semana de 7 a 14 de fevereiro de 2025.

## Resumo
- Este trabalho consiste na implementação de um programa que processa um texto e soma todas as sequências de dígitos encontradas.
- O comportamento de soma pode ser desativado ao encontrar a string "Off"  e reativado ao encontrar "On".
- Sempre que o caractere "=" for encontrado, o resultado parcial da soma é exibido.

## Implementação
### Explicação Detalhada

1. **Leitura do Ficheiro:**
   - O ficheiro é aberto e lido linha por linha até o final.
   - As linhas são convertidas para minúsculas para tratamento uniforme de "On" e "Off".

2. **Processamento dos Caracteres:**
   - O programa percorre a linha caractere por caractere.
   - Se for uma letra, verifica-se se faz parte das palavras "On" ou "Off".
     - "On" ativa a soma de números encontrados a seguir.
     - "Off" desativa a soma, ignorando números subsequentes.
     - Para fazermos isto temos um multipolicador que é posto a 0 quando encontramos "off" e a 1 quando encontramos 1.
   - Se for um número, o programa identifica sequências de dígitos completas.
     - Os números consecutivos são unidos para formar um único valor.
     - O número é multiplicado pelo multiplicador definido pelo estado atual de soma.
   - Se encontrar "=", imprime a soma acumulada até aquele ponto.

3. **Cálculo da Soma:**
   - Os números extraídos são convertidos de string para inteiro.
   - A posição e sequência dos números são analisadas para garantir a soma correta.
   - O valor identificado é somado ao acumulador global, caso a soma esteja ativada.



## Resultados
- [Código-fonte](tpc1.py)
- [Exemplo de entrada](ficheiro.txt)
- [Exemplo de saída](resultados.txt)



