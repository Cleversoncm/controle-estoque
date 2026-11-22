import os
import json

ARQUIVO_BANCO = "banco_estoque.json"

ESTOQUE_PADRAO = [
    ["Arroz 5kg", 12, 15],
    ["Feijão 1kg", 25, 20],
    ["Óleo de Soja", 8, 10]
]

def carregar_dados():
    if not os.path.exists(ARQUIVO_BANCO):
        salvar_dados(ESTOQUE_PADRAO)
        return list(ESTOQUE_PADRAO)
    try:
        with open(ARQUIVO_BANCO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except Exception:
        return list(ESTOQUE_PADRAO)

def salvar_dados(dados):
    with open(ARQUIVO_BANCO, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

def listar_todos(estoque_dados):
    print("\n===============================================")
    print("          TODOS OS PRODUTOS NO ESTOQUE         ")
    print("===============================================")
    print(f"{'Produto':<25} | {'Atual':<6} | {'Mínimo':<6}")
    print("-----------------------------------------------")
    for nome, atual, minimo in estoque_dados:
        print(f"{nome:<25} | {atual:<6} | {minimo:<6}")
    print("===============================================\n")

def listar_criticos(estoque_dados):
    print("\n===============================================")
    print("          RELATÓRIO DE PRODUTOS CRÍTICOS       ")
    print("===============================================")
    print(f"{'Produto':<25} | {'Atual':<6} | {'Mínimo':<6}")
    print("-----------------------------------------------")
    
    # A sua linha corrigida de alta performance:
    criticos = [item for item in estoque_dados if item[1] < item[2]]
    
    if not criticos:
        print("Nenhum produto está com estoque crítico!")
    else:
        for nome, atual, minimo in criticos:
            print(f"{nome:<25} | {atual:<6} | {minimo:<6}")
    print("===============================================\n")

def cadastrar_produto(estoque_dados):
    print("\n--- CADASTRO DE NOVO PRODUTO ---")
    nome = input("Nome do produto: ").strip()
    try:
        atual = int(input(f"Quantidade atual de '{nome}': "))
        minimo = int(input(f"Quantidade mínima de '{nome}': "))
        
        estoque_dados.append([nome, atual, minimo])
        salvar_dados(estoque_dados)
        print(f"\n[OK] '{nome}' salvo permanentemente no arquivo!")
    except ValueError:
        print("\n[Erro] Digite números válidos!")

def atualizar_estoque(estoque_dados):
    print("\n--- ATUALIZAR QUANTIDADE EM ESTOQUE ---")
    nome_busca = input("Digite o nome exato do produto que deseja atualizar: ").strip()
    
    for item in estoque_dados:
        if item[0].lower() == nome_busca.lower():
            try:
                novo_atual = int(input(f"Nova quantidade atual para '{item[0]}': "))
                item[1] = novo_atual
                salvar_dados(estoque_dados)
                print(f"\n[OK] Estoque de '{item[0]}' atualizado para {novo_atual}!")
                return
            except ValueError:
                print("\n[Erro] Digite um número inteiro válido!")
                return
                
    print("\n[Aviso] Produto não encontrado no sistema.")

def remover_produto(estoque_dados):
    print("\n--- REMOVER PRODUTO DO ESTOQUE ---")
    nome_busca = input("Digite o nome exato do produto que deseja deletar: ").strip()
    
    for item in estoque_dados:
        if item[0].lower() == nome_busca.lower():
            confirmar = input(f"Tem certeza que deseja deletar '{item[0]}'? (s/n): ").strip().lower()
            if confirmar == 's':
                estoque_dados.remove(item)
                salvar_dados(estoque_dados)
                print(f"\n[OK] '{item[0]}' foi removido com sucesso!")
            else:
                print("\nRemoção cancelada.")
            return
            
    print("\n[Aviso] Produto não encontrado no sistema.")

if __name__ == "__main__":
    while True:
        ESTOQUE = carregar_dados()
        
        print("=== SISTEMA DE ESTOQUE ===")
        print("1. Cadastrar novo produto")
        print("2. Ver TODO o estoque")
        print("3. Ver APENAS produtos críticos (Abaixo do Mínimo)")
        print("4. Atualizar quantidade de um produto")
        print("5. Remover um produto")
        print("6. Sair")
        
        opcao = input("Escolha (1-6): ").strip()
        
        if opcao == "1":
            cadastrar_produto(ESTOQUE)
        elif opcao == "2":
            listar_todos(ESTOQUE)
        elif opcao == "3":
            listar_criticos(ESTOQUE)
        elif opcao == "4":
            atualizar_estoque(ESTOQUE)
        elif opcao == "5":
            remover_produto(ESTOQUE)
        elif opcao == "6":
            print("\nSaindo...")
            break
        else:
            print("\nOpção inválida!\n")

