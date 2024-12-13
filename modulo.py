import os

def mostrarPessoas(lista):
    if not lista :
        exibirLinha('PESSOAS CADASTRADAS')     
        print("\033[31mA lista está vazia.\033[0m")
    else:    
        exibirLinha('PESSOAS CADASTRADAS')  
        for indice, pessoa in enumerate(lista) : 
            print(f'\033[32m {indice} {pessoa["nome"].title():<30}\033[0m{pessoa["idade"]} anos')
        
    
def exibirLinha(msg):
    largura = 50
    print('-'*50)
    print(f'{msg}'.center(largura))
    print('-'*50)

def exibir_menu():
    exibirLinha('MENU PRINCIPAL')
    print('\033[34m 1 - Ver Pessoas Cadastradas\033[0m')
    print('\033[34m 2 - Cadastrar Nova Pessoa\033[0m')
    print('\033[34m 3 - Remover cadastro\033[0m')
    print('\033[34m 4 - Procurar Pessoa\033[0m')
    print('\033[34m 5 - Limpar terminal\033[0m')
    print('\033[34m 6 - Sair do sistema\033[0m')
    print('-'*50)

def adicionar_Nova_pessoa(lista):
    exibirLinha('NOVO CADASTRO')
    nova_pessoa = dict()
    
    while True:    
        nome = input('Nome: ').strip().lower()
        if nome.replace(" ", "").isalpha():
            nova_pessoa['nome'] = nome
            break       
        else:
            print("\033[31mDigite apenas letras para o nome.\033[0m")
            continue
             
    while True:      
        try:
            idade = input('idade: ')
            nova_pessoa['idade'] = int(idade)
            if nova_pessoa['idade'] < 0:
                print("\033[31mA idade não pode ser negativa.\033[0m")
            else:
                break   
        except ValueError:
            print("\033[31mDigite um número válido\033[0m")
            continue
        
    while True:
             nacionalidade = input('Nacionalidade: ').strip().lower()
             if nacionalidade.isalpha():
                 nova_pessoa['nacionalidade'] = nacionalidade
                 print(f'Novo registro de \033[32m{nova_pessoa["nome"]}\033[0m adicionado.')
                 lista.append(nova_pessoa)
                 break
             else:
                 print("\033[31mDigite apenas caracteres\033[0m")
                 
                 
                    
def remover_pessoa(lista):
    exibirLinha('\033[31mRemover Cadastro\033[0m') 
    if not lista:  # Se a lista de pessoas estiver vazia:
        print("\033[31mA lista está vazia, não há o que remover.\033[0m")
    else:
        mostrarPessoas(lista)
        print()
        escolha_remocao = input('Qual índice da pessoa que você gostaria de remover?: ')
        try:
                # Converte a opção do usuário para um inteiro
            indice_remocao_digitado = int(escolha_remocao)
            print(f'Cadastro de \033[31m {lista[indice_remocao_digitado]["nome"]}\033[0m removido com sucesso.')
            lista.pop(indice_remocao_digitado)
        except (ValueError, IndexError):
            print("\033[31mÍndice inválido. Tente novamente.\033[0m")
    
             
def encontrar_pessoa(lista, nome_Procurado):
    for pessoa in lista:
        if pessoa['nome'].lower() == nome_Procurado:
            exibirLinha(f'\033[32m Encontrado: {pessoa["nome"].title():<14}\033[0m')
            print(f'\033[32m Nome: {pessoa["nome"].title():<14}\033[0m')
            print(f'\033[32m idade: {pessoa["idade"]:<14}\033[0m')
            print(f'\033[32m Nacionalidade: {pessoa["nacionalidade"].title():<14}\033[0m')
            return
    exibirLinha("\033[31mPessoa nao Encontrada\033[0m")
    
def limpar_terminal():
     os.system('cls')   
    

            
   
