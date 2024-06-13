import os

class Restaurante:
    
    restaurantes=[]

    def __init__(self,nome,categoria):
        self.nome=nome
        self.categoria=categoria
        self.ativo=False

        
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def exibir_nome_do_progrma():
        print ('ＳＡＢＯＲ ＥＸＰＲＥＳＳ \n')  
    
    def definir_opcoes():
        print('1. Cadastrar restaurante')
        print('2. Listar Restaurantes')
        print('3. Alterar status do restaurante')
        print('4. Sair \n')
        
    def escolher_opcoes():
        try:  
            opc_escolhida = int(input('Escolha uma opção: '))  
            if opc_escolhida==1:
                Restaurante.cadastrar_novo_restaurante()
            elif opc_escolhida==2:
                Restaurante.listar_restaurantes()
            elif opc_escolhida==3:
                Restaurante.alterar_status_do_restaurante()
            elif opc_escolhida==4:
                Restaurante.fechar_app()
            else:
                Restaurante.opc_invalida()
    
        except:
            Restaurante.opc_invalida()

    def voltar_menu():
        input('\ndigite uma tecla para retornar ao menu')
        Restaurante.main()

    def opc_invalida():
        print('opção invalida \n')
        Restaurante.voltar_menu()  
    
    def cadastrar_novo_restaurante():
        Restaurante.exibir_subtitulo('Cadastro de novos restaurantes')
        nome_restaurante = input('Digite aqui o nome do novo restaurante: ')
        categoria_novo =input(f'Digite a categoria do restaurante {nome_restaurante}: ')
        dados_do_restaurante=Restaurante(nome_restaurante,categoria_novo)
        Restaurante.restaurantes.append(dados_do_restaurante)
        print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
        Restaurante.voltar_menu()
    
    def fechar_app():
        Restaurante.exibir_subtitulo('Finalizar app')

    def exibir_subtitulo(texto):
        os.system("cls")
        linha='*'*(len(texto))
        print(linha)
        print(texto)
        print(linha)
        print()
        
    @classmethod
    def alterar_status_do_restaurante(cls):
        Restaurante.exibir_subtitulo('Alterar status do restaurante\n')
        nome_do_restaurante=input('Digite o nome do restaurante que deseja alterar o status: ')
        restaurante_encontrado = False
        for restaurante in cls.restaurantes:
            if nome_do_restaurante==restaurante.nome:
                restaurante_encontrado=True
                restaurante.ativo=not restaurante.ativo
                if restaurante.ativo==False:
                    mensagem=f'O restaurante {nome_do_restaurante} foi desativado com sucesso'
                    print(mensagem)
                else:
                    mensagem=f'O restaurante {nome_do_restaurante} foi ativado com sucesso'
                    print(mensagem)
                
        if not restaurante_encontrado:
            print(f'O restaurante {nome_do_restaurante} não foi encontrado!')   
            
        Restaurante.voltar_menu() 
            
    
    @classmethod
    def listar_restaurantes(cls):
        Restaurante.exibir_subtitulo('Lista dos restaurantes')
        print(f'{'Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'} ')

        for restaurante in cls.restaurantes:
            if restaurante.ativo==False:
            # restaurante.ativo= 'Ativado' if restaurante.ativo['ativo'] else 'Desativado'
                print(f'- {restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | Desativado')
            else:
                print(f'- {restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | Ativado')

        Restaurante.voltar_menu()
    
            
    def main():
        os.system('cls')
        Restaurante.exibir_nome_do_progrma()
        Restaurante.definir_opcoes()
        Restaurante.escolher_opcoes()

        if __name__ == '__main__':
            Restaurante.main()
        
    
        
restaurante_01=Restaurante('Pão com Banha','gourmet') 
restaurante_02=Restaurante('Saco do Feijão','feijoada') 
restaurante_03=Restaurante('Bife Sujo','churrascaria') 

Restaurante.exibir_nome_do_progrma()
Restaurante.definir_opcoes()
Restaurante.escolher_opcoes()

