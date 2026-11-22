# Estoque inicial: [Quantidade, Preço Unitário]
estoque = {
    "Notebook": [5, 3500.00],
    "Mouse": [15, 50.00],
    "Teclado": [10, 90.00]
}

faturamento_total = 0.0

while True:
    print("\n📦 === SISTEMA DE ESTOQUE, VENDAS E CAIXA ===")
    print("1. Visualizar Estoque")
    print("2. Adicionar/Atualizar Produto")
    print("3. Registrar uma VENDA")
    print("4. Remover Produto do Sistema")
    print("5. Ver Faturamento do Dia")
    print("6. Sair")
    
    opcao = input("\nEscolha uma opção (1-6): ")
    
    if opcao == "1":
        print("\n📋 --- ESTOQUE ATUAL ---")
        if not estoque:
            print("O estoque está vazio!")
        for produto, dados in estoque.items():
            print(f"• {produto}: {dados} unidades | Preço: R$ {dados:.2f}")
            
    elif opcao == "2":
        produto = input("Nome do produto: ").strip().capitalize()
        if produto in estoque:
            print(f"Produto já existe. Estoque: {estoque[produto]} | Preço: R$ {estoque[produto]:.2f}")
        
        try:
            qtd = int(input(f"Quantidade para adicionar: "))
            preco = float(input(f"Preço unitário de {produto}: R$ "))
            
            if qtd < 0 or preco < 0:
                print("❌ Quantidade e preço não podem ser negativos!")
            else:
                if produto in estoque:
                    estoque[produto] += qtd
                    estoque[produto] = preco
                else:
                    estoque[produto] = [qtd, preco]
                print(f"✅ {produto} atualizado com sucesso!")
        except ValueError:
            print("❌ Erro: Digite números válidos.")
            
    elif opcao == "3":
        print("\n🛒 --- REGISTRAR VENDA ---")
        produto = input("Nome do produto que deseja vender: ").strip().capitalize()
        
        if produto in estoque:
            qtd_atual = estoque[produto]
            preco_unitario = estoque[produto]
            
            print(f"Disponível no estoque: {qtd_atual} unidades")
            try:
                qtd_venda = int(input(f"Quantas unidades de {produto} deseja vender? "))
                
                if qtd_venda <= 0:
                    print("❌ Quantidade inválida para venda.")
                elif qtd_venda > qtd_atual:
                    print(f"❌ Venda cancelada! Estoque insuficiente.")
                else:
                    estoque[produto] -= qtd_venda
                    total_pago = qtd_venda * preco_unitario
                    faturamento_total += total_pago
                    
                    # --- AQUI ESTÁ A GRAVAÇÃO PERMANENTE NO ARQUIVO ---
                    # O modo 'a' (append) adiciona o texto no final do arquivo sem apagar o que já existia
                    linha_venda = f"Venda: {qtd_venda}x {produto} - Total: R$ {total_pago:.2f}\n"
                    with open("historico_vendas.txt", "a", encoding="utf-8") as arquivo:
                        arquivo.write(linha_venda)
                    
                    print(f"\n🎉 VENDA REALIZADA COM SUCESSO!")
                    print(f"Item: {produto} x{qtd_venda}")
                    print(f"Total a pagar: R$ {total_pago:.2f}")
                    print("💾 Venda gravada em 'historico_vendas.txt'!")
            except ValueError:
                print("❌ Erro: Digite um número inteiro.")
        else:
            print("❌ Produto não encontrado.")
            
    elif opcao == "4":
        produto = input("Nome do produto para remover: ").strip().capitalize()
        if produto in estoque:
            del estoque[produto]
            print(f"🗑️ {produto} removido.")
            
    elif opcao == "5":
        print("\n💰 --- RELATÓRIO DE FATURAMENTO ---")
        print(f"Faturamento desta sessão: R$ {faturamento_total:.2f}")
        print("Para ver todas as vendas já salvas na história, abra o arquivo 'historico_vendas.txt' no terminal.")
                
    elif opcao == "6":
        print("Saindo do sistema... 👋")
        break

