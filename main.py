import sqlite3

conexao = sqlite3.connect('cadastro.db')

# Crie uma tabela para armazenar as informações de cadastro
conexao.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, senha TEXT)')

# Pergunte ao usuário se ele já tem um cadastro
sistema_nome = "ThurTz" # caso precise , altere o nome do sistema para o seu!!     <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- 
cadastro = input(f"Você já tem cadastro no sistema {sistema_nome}? ").lower()

# Se o usuário não tem cadastro, pergunte se ele deseja se cadastrar
if cadastro in ["n", "não", "nao", "negativo"]:
    cadastrar = input("Você deseja realizar seu cadastro? ").lower()
    if cadastrar in ["s", "sim", "positivo"]:
        print("Vamos iniciar seu cadastro agora \n")
        nome_usuario = input("Informe o seu nome de usuário: ")
        senha_usuario = input("Informe a sua senha: ")

        #informações de cadastro na tabela de usuários
        conexao.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (nome_usuario, senha_usuario))
        conexao.commit()

        print("Cadastro finalizado, agora faça seu login normalmente ")
else:
    print("Tudo bem, faça seu login normalmente ")

# Peça ao usuário para fazer o login
nome_usuario = input("Informe o seu nome de usuário: ")
senha_usuario = input("Informe a sua senha: ")

# Verifique se as informações de login correspondem às informações de cadastro armazenadas no banco de dados
resultado = conexao.execute("SELECT * FROM usuarios WHERE nome = ? AND senha = ?", (nome_usuario, senha_usuario)).fetchone()

if resultado:
    print("Login bem sucedido ✅")
else:
    print("Usuário ou senha incorretos 🚫")

# Feche a conexão com o banco de dados
conexao.close()

        
