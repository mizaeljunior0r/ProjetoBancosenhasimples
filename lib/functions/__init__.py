from lib.arquivo import *
from lib.interface import *
import itertools
from lib.arquivo import *

# Função para gerar IDs únicos para novas entradas
def geradorId(arq):
    ultimo_id = 0  # Inicializa o último ID como 0
    if arqExiste(arq):  # Verifica se o arquivo existe
        with open(arq, 'r') as arquivo:  # Abre o arquivo no modo leitura
            for linha in arquivo:  # Itera sobre cada linha do arquivo
                dados = linha.split(';')  # Divide a linha nos pontos separados por ';'
                if dados:  # Verifica se a linha não está vazia
                    ultimo_id = int(dados[0])  # Converte o primeiro campo (ID) em inteiro
    contador = itertools.count(start=ultimo_id+1, step=1)  # Gera IDs a partir do último ID encontrado
    while True:
        yield next(contador)  # Retorna o próximo valor do contador sempre que for chamado

# Função que verifica se o arquivo existe
def arqExiste(arq):
    try:
        a = open(arq, 'rt')  # Tenta abrir o arquivo no modo texto
        a.close()  # Fecha o arquivo imediatamente após abrir
    except FileNotFoundError:
        return False  # Retorna False se o arquivo não for encontrado
    else:
        return True  # Retorna True se o arquivo existir

# Função que cria um novo arquivo se ele não existir
def criArq(cam):
    try:
        a = open(cam, 'wt+')  # Tenta abrir/criar o arquivo no modo escrita e leitura
        a.close()  # Fecha o arquivo após criar
    except:
        print('Houve um erro ao tentar criar o arquivo, no diretório informado')

# Função para cadastrar uma nova senha
def cadastraSenha(arq, site, usuario, senha, id_gerador):
    with open(arq, 'a') as a:  # Abre o arquivo no modo append (para adicionar dados)
        id_atual = next(id_gerador)  # Gera um novo ID
        a.write(f'{id_atual};{site};{usuario};{senha}\n')  # Escreve a nova senha no arquivo

# Função para ler e exibir o conteúdo do arquivo
def lerArquivo(arq):
    try:
        a = open(arq, 'rt')  # Tenta abrir o arquivo no modo leitura
        c = 1  # Inicializa um contador para controlar o número de linhas lidas
    except:
        print(f'\033[32mFalha ao tentar ler o arquivo\033[m "{arq}". ')  # Exibe uma mensagem de erro caso falhe ao abrir o arquivo
    else:
        display1('SENHAS CADASTRADAS')  # Exibe o cabeçalho
        display1(f'{"ID":<3} - {"SITE":<20}{"USUÁRIO":^20}{"SENHA":>20}')  # Exibe os títulos das colunas
        for linha in a:  # Itera sobre cada linha no arquivo
            dado = linha.split(';')  # Divide a linha nos pontos separados por ';'
            dado[1] = dado[1].replace('\n', '')  # Remove quebras de linha do segundo campo
            print(f'{dado[0]:<3} - {dado[1]:<20}{dado[2]:^20}{dado[3]:>20}')  # Exibe os dados formatados
            c += 1  # Incrementa o contador

# Função para limpar o conteúdo do arquivo
def limpaArquivo(arq):
    try:
        with open(arq, 'w') as arquivo:  # Abre o arquivo no modo de escrita, que apaga todo o conteúdo
            pass  # Não faz nada além de abrir o arquivo no modo 'w', o que já limpa seu conteúdo
    except Exception as e:
        print(f'Problema ao tentar limpar o DB: {e}')  # Exibe uma mensagem de erro caso algo falhe
    else:
        print('Banco de dados limpo com sucesso!')  # Mensagem de sucesso ao limpar o arquivo
