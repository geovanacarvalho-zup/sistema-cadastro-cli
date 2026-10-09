import sqlite3    # REQUISITO : TER MODULO


# 1. CRIAR TABELA NO BANCO (CREATE)

def criar_tabela() -> None:                        # REQUSITO : TER FUNÇÕES (def)
    try:                                            # REQUISITO: TER TRATAMENTO DE ERROS (try/except)
        conexao = sqlite3.connect("cadastro.db")
        cursor = conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cadastros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
        """)

        conexao.commit()
    except sqlite3.Error as erro:
        print(f"❌ Erro ao criar tabela: {erro}")
    finally:
        conexao.close()



# 2. INSERIR COLABORADOR (CREATE)

def cadastrar_colaborador(nome: str, idade: int, email: str, telefone: str, *args, **kwargs) -> None:  # REQUISITOS: TER KWARGS , TER ARGS E NONE
    try:
        conexao = sqlite3.connect("cadastro.db")
        cursor = conexao.cursor()
        
        cursor.execute(
            "INSERT INTO cadastros (nome, idade, email, telefone) VALUES (?, ?, ?, ?)",
            (nome, idade, email, telefone)
        )
        
        conexao.commit()
        print(f"\n✅ {nome} cadastrado(a) com sucesso!")
    except sqlite3.Error as erro:
        print(f"❌ Erro ao cadastrar: {erro}")
    finally:
        conexao.close()



# 3. LISTAR COLABORADORES (READ)

def listar_colaboradores() -> None:
    try:
        conexao = sqlite3.connect("cadastro.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM cadastros")
        colaboradores = cursor.fetchall()  # REQUISITO LISTA : Retorna uma LISTA de tuplas do banco

        #  REQUISITO TER COMPREHENSION: Transforma a lista de tuplas em uma lista de DICIONÁRIOS
        colaboradores_dict = [                                                                     #REQUISITO : TER  DICT
            {
                "id": c[0], 
                "nome": c[1], 
                "idade": c[2], 
                "email": c[3], 
                "telefone": c[4]
            } 
            for c in colaboradores
        ]

        print("\n--- LISTA DE CADASTROS ---")
        if not colaboradores_dict:
            print("Nenhum cadastro encontrado.")
        else:
            for item in colaboradores_dict:
                print(
                    f"ID: {item['id']} | "
                    f"Nome: {item['nome']} | "
                    f"Idade: {item['idade']} | "
                    f"Email: {item['email']} | "
                    f"Tel: {item['telefone']}"
                    
                )
        print("--------------------------")

    except sqlite3.Error as erro:
        print(f"❌ Erro ao listar: {erro}")
    finally:
        conexao.close()


# 4. ATUALIZAR COLABORADOR (UPDATE)

def atualizar_nome(id_colaborador: int, novo_nome: str) -> None:
    try:
        conexao = sqlite3.connect("cadastro.db")
        cursor = conexao.cursor()

        cursor.execute(
            "UPDATE cadastros SET nome = ? WHERE id = ?",
            (novo_nome, id_colaborador)
        )

        conexao.commit()
        print(f"\n✅ Cadastro #{id_colaborador} alterado para '{novo_nome}'!")
    except sqlite3.Error as erro:
        print(f"❌ Erro ao atualizar: {erro}")
    finally:
        conexao.close()


# 5. EXCLUIR COLABORADOR (DELETE)

def excluir_colaborador(id_colaborador: int) -> None:
    try:
        conexao = sqlite3.connect("cadastro.db")
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM cadastros WHERE id = ?", (id_colaborador,))

        conexao.commit()
        print(f"\n✅ Cadastro #{id_colaborador} removido com sucesso!")
    except sqlite3.Error as erro:
        print(f"❌ Erro ao excluir: {erro}")
    finally:
        conexao.close()



# 6. MENU INTERATIVO (CLI)

def menu() -> None:
    # Garante que a tabela é criada ANTES de exibir o menu
    criar_tabela()
    
    while True:
        print("\n=== SISTEMA DE CADASTRO COMPLETO ===")
        print("1. Cadastrar Pessoa")
        print("2. Listar Pessoas")
        print("3. Alterar Nome de uma Pessoa")
        print("4. Excluir Cadastro")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        # TRATAMENTO DE ERROS NO INPUT DO USUÁRIO
        try:
            if opcao == "1":
                nome = input("Digite o Nome: ")
                idade = int(input("Digite a Idade: "))
                email = input("Digite o Email: ")
                telefone = input("Digite o Telefone: ")
                cadastrar_colaborador(nome, idade, email, telefone)

            elif opcao == "2":
                listar_colaboradores()

            elif opcao == "3":
                id_colab = int(input("Digite o ID de quem quer alterar: "))
                novo_nome = input("Digite o novo nome: ")
                atualizar_nome(id_colab, novo_nome)

            elif opcao == "4":
                id_colab = int(input("Digite o ID para excluir: "))
                excluir_colaborador(id_colab)

            elif opcao == "0":
                print("Saindo do sistema... Até logo!")
                break
            else:
                print("❌ Opção inválida! Tente novamente.")
        except ValueError:
            print("❌ Erro: Digite apenas números inteiros válidos para a Idade ou ID!")



# PONTO DE ENTRADA DO SCRIPT

if __name__ == "__main__":
    menu()