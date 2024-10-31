# README - Cálculo de Compras no MacPRONALTS

## Descrição do Problema

Este problema consiste em criar um programa que ajude a calcular o total da compra em um restaurante (MacPRONALTS) durante uma promoção, facilitando o trabalho da atendente que está sem uma calculadora. O usuário deve fornecer a quantidade de produtos comprados, seguido dos códigos e quantidades de cada produto. O programa deve calcular e imprimir o valor total da compra com duas casas decimais.

## Cardápio

O cardápio contém os seguintes produtos e seus respectivos preços:

| Código do Produto | Preço (R$) |
|-------------------|------------|
| 1001              | 1.50       |
| 1002              | 2.50       |
| 1003              | 3.50       |
| 1004              | 4.50       |
| 1005              | 5.50       |

## Especificações

1. A primeira linha da entrada informará a quantidade de produtos comprados \( p \) (onde \( 1 \leq p \leq 5 \)).
2. Para cada produto, serão fornecidos:
   - O código do produto (um dos códigos do cardápio).
   - A quantidade comprada (onde \( 1 \leq q \leq 500 \)).
3. Não poderão ser informados números de produtos repetidos.

## Entrada

A entrada consistirá em:
- Uma linha com um inteiro \( p \).
- \( p \) linhas subsequentes, cada uma contendo:
  - Um código de produto.
  - Uma quantidade comprada.

## Saída

A saída deve consistir de uma única linha com o valor total da compra, formatado com duas casas decimais.

## Exemplos

### Exemplo 1

**Entrada:**
```
2
1001 2
1005 3
```

**Saída:**
```
19.50
```

### Exemplo 2

**Entrada:**
```
1
1003 500
```

**Saída:**
```
1750.00
```

### Exemplo 3

**Entrada:**
```
5
1001 500
1005 300
1003 23
1002 52
1004 44
```

**Saída:**
```
2808.50
```

## Implementação

Aqui está um exemplo de implementação em Python para resolver o problema:

```python
# Dicionário que contém os produtos e seus preços
precos = {
    1001: 1.50,
    1002: 2.50,
    1003: 3.50,
    1004: 4.50,
    1005: 5.50
}

# Leitura da quantidade de produtos
p = int(input())

total = 0.0

# Leitura dos produtos e suas quantidades
for _ in range(p):
    codigo, quantidade = map(int, input().split())
    total += precos[codigo] * quantidade

# Impressão do total com duas casas decimais
print(f"{total:.2f}")
```

## Considerações Finais

- O programa deve garantir que os códigos dos produtos fornecidos estão no cardápio e que as quantidades são válidas.
- A saída deve sempre ser formatada com duas casas decimais, mesmo que o valor total seja um número inteiro.
- O programa deve ser executado em um ambiente que suporte entrada e saída padrão.
