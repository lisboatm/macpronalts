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
