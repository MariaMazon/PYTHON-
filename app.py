import os 

# restaurantes = ['Funeraria e Pizzaria Dona Lucia','Tokomia','Saburov']
# dicionario
restaurantes=[{'nome':'Pão com Banha','categoria':'gourmet','ativo':False},
              {'nome':'Saco do Feijão','categoria':'feijoada','ativo':True},
              {'nome':'Bife Sujo','categoria':'churrascaria','ativo':False}]


def exibir_nome_do_progrma():
    print ('ＳＡＢＯＲ ＥＸＰＲＥＳＳ \n')

def definir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar Restaurantes')
    print('3. Alterar status do restaurante')
    print('4. Sair \n')

def voltar_menu():
    input('\ndigite uma tecla para retornar ao menu')
    main()

def opc_invalida():
    print('opção invalida \n')
    voltar_menu()

def cadastrar_novo_restaurante():
    ''' DOCSTRINGS
            Essa função é responsável por cadastrar um novo restaurante 

            Inputs:
                -Nome dorestaurante
                -Categoria
        
            Outputs:
                - Adicionar um novo restaurante o dicionário restaurantes    
    
    '''
    
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite aqui o nome do novo restaurante: ')
    categoria =input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante ={'nome':nome_restaurante,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_menu()

def listar_restaurantes():
    exibir_subtitulo('Lista dos restaurantes')
    
    for restaurante in restaurantes:
        nome_restaurante=restaurante['nome']
        categoria=restaurante['categoria']
        ativo= 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(15)} | {categoria.ljust(15)} | {ativo}')
        # ljust delimita a quantidade de caracteres que cada elemento tem

    voltar_menu()
    
def alterar_status_do_restaurante():
    exibir_subtitulo('Alterar status do restaurante\n')
    nome_do_restaurante=input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_do_restaurante==restaurante['nome']:
            restaurante_encontrado=True
            restaurante['ativo']=not restaurante['ativo']
            mensagem=f'O restaurante {nome_do_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_do_restaurante} não foi encontrado!')   
        
    voltar_menu() 
        
def fechar_app():
    exibir_subtitulo('Finalizar app')

def exibir_subtitulo(texto):
    os.system("cls")
    linha='*'*(len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
    
def escolher_opcoes():
    try:
        opc_escolhida = int(input('Escolha uma opção: '))

        if opc_escolhida==1:
            cadastrar_novo_restaurante()
        elif opc_escolhida==2:
            listar_restaurantes()
        elif opc_escolhida==3:
            print('Ativar Restaurante')
            alterar_status_do_restaurante()
        else:
            fechar_app()
    except:
        opc_invalida()

def main():
    os.system('cls')
    exibir_nome_do_progrma()
    definir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()