import os 

# restaurantes = ['Funeraria e Pizzaria Dona Lucia','Tokomia','Saburov']
# dicionario
restaurantes=[{'nome':'Pão com Banha','categoria':'gourmet','ativo':False},
              {'nome':'Saco do Feijão','categoria':'feijoada','ativo':True},
              {'nome':'Bife Sujo','categoria':'churrascaria','ativo':False}]


def exibir_nome_do_progrma():
    print ("ＳＡＢＯＲ ＥＸＰＲＥＳＳ \n")

def definir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair \n')

def voltar_menu():
    input('\ndigite uma tecla para retornar ao menu')
    main()

def opc_invalida():
    print('opção invalida \n')
    voltar_menu()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite aqui o nome do novo restaurante: ')
    categoria =input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante ={'nome':nome_restaurante,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_menu()

def listar_restaurantes():
    exibir_subtitulo('Lista dos restaurantes\n')
    
    for restaurante in restaurantes:
        nome_restaurante=restaurante['nome']
        categoria=restaurante['categoria']
        ativo= 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante} | {categoria} | {ativo}')

    voltar_menu()
        
def fechar_app():
    exibir_subtitulo('Finalizar app')

def exibir_subtitulo(texto):
    os.system("cls")
    print(texto)
    print()
    
def escolher_opcoes():
    try:
        opc_escolhida = int(input("Escolha uma opção: "))

        if opc_escolhida==1:
            cadastrar_novo_restaurante()
        elif opc_escolhida==2:
            listar_restaurantes()
        elif opc_escolhida==3:
            print('Ativar Restaurante')
            opc_invalida()
        else:
            fechar_app()
    except:
        opc_invalida()

def main():
    os.system("cls")
    exibir_nome_do_progrma()
    definir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()