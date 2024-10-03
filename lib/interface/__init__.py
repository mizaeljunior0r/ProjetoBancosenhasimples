def checkint(info):
    while True:  # Inicia um loop que continuará até que um valor válido seja retornado
        try:
            num = int(input(info))  # Tenta converter a entrada do usuário em um inteiro
        except (ValueError, TypeError):  # Captura exceções se a conversão falhar
            print(f'Valor informado é inválido, tente novamente!!')  # Mensagem de erro se a conversão falhar
            continue  # Retorna ao início do loop para solicitar novamente a entrada
        except KeyboardInterrupt:  # Captura a interrupção do teclado (Ctrl + C)
            print(f'\033[31mO usuário preferiu não inserir nada.\033[m')  # Mensagem informando que o usuário cancelou a entrada
            return 0  # Retorna 0 se o usuário cancelar a entrada
        else:
            return num  # Retorna o número convertido se não houve exceções

def linha(tam=70):
    return f'\033[92m{"="*tam}\033[0m'  # Retorna uma linha de caracteres "=" com a cor verde, com comprimento especificado

def display1(txt):
    print(linha())  # Exibe a linha antes do texto
    print(txt.center(70))  # Centraliza o texto em uma largura de 70 caracteres
    print(linha())  # Exibe a linha após o texto

def menu(lista):
    display1('MENU PRINCIPAL')  # Exibe o título do menu
    c = 1  # Inicializa o contador para as opções do menu
    for x in lista:  # Itera sobre a lista de opções
        print(f'{c} - {x}')  # Exibe cada opção com seu respectivo número
        c += 1  # Incrementa o contador
    print(linha())  # Exibe uma linha após as opções
    op = int(input('ESCOLHA UMA OPÇÃO: '))  # Solicita que o usuário escolha uma opção
    return op  # Retorna a opção escolhida pelo usuário
