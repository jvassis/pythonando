from controllers import CadastroController, LoginController


while True:
    print('============== MENU ==============')
    opcao = int(input('digite 1 para cadastrar\n'
                      'digite 2 para logar\n'
                      'digite 3 para sair\n'))
    if opcao == 1:
        user = input('digite o usuario: ')
        email = input('digite o email: ')
        password = input('digite a senha: ')
        res = CadastroController.cadastrar(user, email, password)
        if res == 2:
            print('tamanho de senha invalido')
        elif res == 3:
            print('email maior que 100 caracteres')
        elif res == 4:
            print('tamanho de senha invalido')
        elif res == 5:
            print('email ja cadastrado')
        elif res == 6:
            print('erro interno do sistema')
        else:
            print('cadastro efetuado com sucesso!')
    elif opcao == 2:
        email = input('digite o email: ')
        password = input('digite a senha: ')
        user = LoginController.login(email, password)
        if not user:
            print('email ou senha invalidos')
        else:
            print(user)
    else:
        break