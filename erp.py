print("===== stock control =====")

USUARIO_CORRETO = "admin"
SENHA_CORRETA = "1234"

MAX_TENTATIVAS = 5

for tentativa in range(MAX_TENTATIVAS):
    login = input("Login: ")
    senha = input("Senha: ")

    if login == USUARIO_CORRETO and senha == SENHA_CORRETA:
        print("Acesso autorizado! Bem-vindo ao sistema de estoque.")
        break
    else:
        restantes = MAX_TENTATIVAS - tentativa - 1
        if restantes > 0:
            print(f"Login ou senha incorretos. {restantes} tentativa(s) restante(s).")
        else:
            print(" Sistema bloqueado. Número máximo de tentativas atingido.")
        
estoque =  [
    {"nome": "Smartphone", "quantidade": 15, "valor": 2500.00},
    {"nome": "Notebook", "quantidade": 8, "valor": 4500.00},
    {"nome": "Tablet", "quantidade": 10, "valor": 1800.00},
    {"nome": "Smart TV", "quantidade": 5, "valor": 3200.00},
    {"nome": "Fone de ouvido", "quantidade": 25, "valor": 150.00},
    {"nome": "Caixa de som Bluetooth", "quantidade": 12, "valor": 300.00},
    {"nome": "Mouse sem fio", "quantidade": 20, "valor": 80.00},
    {"nome": "Teclado mecânico", "quantidade": 7, "valor": 350.00},
    {"nome": "Monitor", "quantidade": 6, "valor": 1200.00},
    {"nome": "Console de video-game", "quantidade": 4, "valor": 2800.00}
]

def criar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    valor = float(input("Valor (R$): "))
    estoque.append({"nome": nome, "quantidade": quantidade, "valor": valor})
    print(f" '{nome}' adicionado ao estoque!")

def listar_produtos():
    if not estoque:
        print("Estoque vazio.")
        return
    print("\n{:<5} {:<25} {:<12} {}".format("ID", "Nome", "Quantidade", "Valor"))
    print("-" * 55)
    for i, produto in enumerate(estoque):
        print("{:<5} {:<25} {:<12} R$ {:.2f}".format(
            i, produto["nome"], produto["quantidade"], produto["valor"]
        ))

def atualizar_produto():
    listar_produtos()
    try:
        indice = int(input("Digite o ID do produto que deseja editar: "))
        produto = estoque[indice]
    except (ValueError, IndexError):
        print("ID inválido.")
        return

    nome = input(f"Novo nome ({produto['nome']}): ")
    quantidade = input(f"Nova quantidade ({produto['quantidade']}): ")
    valor = input(f"Novo valor ({produto['valor']}): ")

    if nome:
        produto["nome"] = nome
    if quantidade:
        produto["quantidade"] = int(quantidade)
    if valor:
        produto["valor"] = float(valor)

    print("Produto atualizado!")

def deletar_produto():
    listar_produtos()
    try:
        indice = int(input("Digite o ID do produto que deseja remover: "))
        removido = estoque.pop(indice)
        print(f"'{removido['nome']}' removido do estoque!")
    except (ValueError, IndexError):
        print("ID inválido.")

while True:
    print("\n===== MENU =====")
    print("1 - Listar produtos")
    print("2 - Adicionar produto")
    print("3 - Editar produto")
    print("4 - Remover produto")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_produtos()
    elif opcao == "2":
        criar_produto()
    elif opcao == "3":
        atualizar_produto()
    elif opcao == "4":
        deletar_produto()
    elif opcao == "0":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")