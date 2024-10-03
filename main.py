import getpass  # Importa o módulo getpass para esconder a entrada da senha
from lib.functions import *  # Importa todas as funções do módulo functions
from lib.interface import *  # Importa todas as funções do módulo interface
from lib.arquivo import *  # Importa todas as funções do módulo arquivo
from lib.login import *  # Importa todas as funções do módulo login

# Configuração do arquivo onde serão guardados os dados:
# arq = r'C:\Users\mizael\OneDrive\Área de Trabalho\python - projeto banco de senhas\lib\arquivo\db.txt'

# Condição de verificação se o arquivo existe.
if not arqExiste(arq):  # Se o arquivo não existir
    print(f'\033[31mArquivo DB Não encontrado\033[m')  # Mensagem de erro se o arquivo não foi encontrado
    criArq(arq)  # Cria um novo arquivo
    print(f'\033[32mFoi criado um novo arquivo!\033[m')  # Mensagem de sucesso ao criar o arquivo

id_gerador = geradorId(arq)  # Cria um gerador de IDs baseado no arquivo

# Menu do programa
op_menu = ['SENHAS CADASTRADAS', 'CADASTRAR UMA NOVA SENHA', 'DELETAR UM CADASTRO', 'SAIR DO SISTEMA']

# Mensagem inicial
display1('SEJA BEM VINDO AO GERENCIADOR DE SENHAS')  # Exibe uma mensagem de boas-vindas

# Área de login
while True:
    usuario_input = input('Digite seu usuário: ')  # Solicita ao usuário que digite o nome de usuário
    senha_input = getpass.getpass('Digite sua senha: ')  # Solicita a senha, sem exibir os caracteres

    # Verifica se o nome de usuário está correto
    if not usuario(usuario_input):
        print(f'\033[31mUsuário incorreto!\033[m')  # Mensagem de erro se o usuário estiver incorreto
        # Verifica se a senha está correta
        if not senha(senha_input):
            print(f'\033[31mSenha incorreta!\033[m')  # Mensagem de erro se a senha estiver incorreta

    # Verifica se o nome de usuário e a senha estão corretos
    elif not senha(senha_input):
        print(f'\033[31mSenha incorreta!\033[m')  # Mensagem de erro se a senha estiver incorreta
    
    # Se tanto o usuário quanto a senha estiverem corretos
    if usuario(usuario_input) and senha(senha_input):
        print(f'\033[32mAcesso concedido\033[m')  # Mensagem de acesso concedido
        break  # Sai do loop de login

# Menu de opções
while True:
    resposta = menu(op_menu)  # Exibe o menu e aguarda a resposta do usuário

    # Lê o arquivo
    if resposta == 1:
        lerArquivo(arq)  # Chama a função para ler o arquivo e exibir as senhas cadastradas

    # Cadastro da nova senha
    elif resposta == 2:
        display1(f'CADASTRAR NOVA SENHA')  # Exibe mensagem para cadastrar uma nova senha
        site = str(input('INSIRA O ENDEREÇO DO SITE: '))  # Solicita o endereço do site
        usuario = str(input('INFOME SEU NOME DE USUÁRIO: '))  # Solicita o nome de usuário
        senha = str(input('INFORME SUA SENHA: '))  # Solicita a senha
        cadastraSenha(arq, site, usuario, senha, id_gerador)  # Chama a função para cadastrar a senha
        print(f'\033[32mSenha cadastrada com sucesso!\033[m')  # Mensagem de sucesso ao cadastrar a senha

    # Limpa o banco de dados
    elif resposta == 3:
        limpaArquivo(arq)  # Chama a função para limpar o arquivo de senhas

    # Fecha o programa
    elif resposta == 4:
        print('Fechando o programa')  
        break  # Sai do loop do menu

    else:
        print(f'Opção inválida')  
