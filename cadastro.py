
import modulo
import time
import json


def salvar_cadastro(lista):
    with open('cadastro.json', 'w') as arquivo:
        json.dump(lista, arquivo, indent=4)    
          

def carregar_dados():
    """
    Carrega os dados das pessoas a partir do arquivo 'cadastro.json'.
    
    Se o arquivo não existir ou ocorrer um erro ao abrir o arquivo,
    retorna uma lista vazia.
    
    Returns:
        list: Lista de pessoas cadastradas.
    """
    try:
        with open('cadastro.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []    

#carrega a lista de pessoas ao iniciar o programa, vai ser inicado com os dados salvos no json ou caso nao tenha nada, uma lista vazia
lista_pessoas = carregar_dados()

while True:
    # Exibe o menu de opções
    modulo.exibir_menu()
    opcao = (input('Sua opção: '))
    
    try:
        # Converte a opção do usuário para um inteiro
        opcao_usuario = int(opcao)
    except ValueError:
         print("\033[31mVocê não digitou um número válido.\033[0m")
         continue  
    
    if opcao_usuario == 1:  # ver pessoas cadastradas
        modulo.mostrarPessoas(lista_pessoas)

    elif opcao_usuario == 2:  # Adicionar nova pessoa
        modulo.adicionar_Nova_pessoa(lista_pessoas)
        salvar_cadastro(lista_pessoas)

    elif opcao_usuario == 3:  # Remover cadastro
        modulo.remover_pessoa(lista_pessoas)
        salvar_cadastro(lista_pessoas) # Atualiza o arquivo JSON
        #vai salvar a lista com a pessoa removida no arquivo json
    
    elif opcao_usuario == 4:
        modulo.exibirLinha('Encontrar Pessoa')
        nome_procurado = input('Qual o nome da pessoa que voce gostaria de ver os dados?: ').lower().strip()
        try:     
            nome_procurado_str = str(nome_procurado).lower().strip()
            modulo.encontrar_pessoa(lista_pessoas, nome_procurado_str)
        except (ValueError, TypeError):
            print('Digite apenas caracteres')
            
    elif opcao_usuario == 5:
        modulo.limpar_terminal()                    

    elif opcao_usuario == 6:
        break
    else:
        print("\033[31m Opcao invalida \033[0m")


modulo.exibirLinha('Saindo do sistema...')
time.sleep(2)
modulo.exibirLinha('Até logo!')
