def calcular_total(produtos):
    total = 0.0

    while True:
        # Solicita o código do produto e a quantidade
        entrada = input("Digite o código do produto e a quantidade (ou 'sair' para finalizar): ")
        
        if entrada.lower() == 'sair':
            break
        
        try:
            # Divide a entrada em código e quantidade
            codigo, quantidade = map(int, entrada.split())
            if codigo in produtos:
                nome, preco = produtos[codigo]
                # Exibe o nome do produto e o preço
                print(f"Produto: {nome} (R$ {preco:.2f})")
                # Solicita confirmação do nome do produto
                confirmacao_nome = input("Deseja confirmar o nome do produto? (s/n): ")
                if confirmacao_nome.lower() == 's':
                    total += preco * quantidade
                    print(f"{quantidade} unidade(s) de {nome} adicionadas ao total.")
                else:
                    print(f"Nome do produto não confirmado. Ignorando a entrada.")
            else:
                print(f"Código de produto {codigo} não encontrado.")
        except ValueError:
            print("Por favor, insira códigos e quantidades válidos no formato 'código quantidade'.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    # Impressão do total com duas casas decimais
    print(f"Total: R$ {total:.2f}")

# Dicionário que contém os produtos e seus preços
produtos = {
    1001: ("Produto A", 1.50),
    1002: ("Produto B", 2.50),
    1003: ("Produto C", 3.50),
    1004: ("Produto D", 4.50),
    1005: ("Produto E", 5.50)
}

calcular_total(produtos)
