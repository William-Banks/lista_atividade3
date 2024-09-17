
lista_usuario = []

while True:

    
    print()
    print(30*'*', 'Menu', 30*'*')
    print('1. Cadastrar o usuario. ')
    print('2. Listar usuario. ')
    print('3. Excluir usuario. ')
    print('4. Buscar pelo nome')
    print('5. Inserir em uma posição.')
    print('6. Sair.')
    print(30*'=', 'Menu', 30*'=')
    print(5)
    
    opcao = input('Digite a opção desejada: ')
    
    #Cadastrar usuario
    if opcao =='1':
        nome = input('Digite o nome que deseja cadastrar: ')

        if nome != '':
            lista_usuario.append(nome)
        else:
            print('Digite algum valor!')
    
    #lista o usuario
    elif opcao =='2':
        for i, n in enumerate(lista_usuario):
            print(f'{i + 1}: {n}')
    
    #sair do sistema
    elif opcao =='4':
        nome_buscar = input('Digite o nome que deseja buscar na lista: ').upper()

        if nome_buscar != '':
            for i in lista_usuario:
                if i == nome_buscar:
                    print(i)
                else:
                    print('Usuario não encontrado')
        else:
            print('Digite algo!')
    
    #excluir usuario
    elif opcao =='3':
        nome = input('Digite o nome que deseja excluir: ')

        for i in lista_usuario:
            if nome == i:
                lista_usuario.remove(i)
                print(f'O usuario removido com sucesso: ')

    #inserir em uma posicao
    elif opcao == '5':
        novo_nome = input('Digite o nome que deseja inserir: ').upper
        posicao_nome = int(input('Digite a posição que deseja inserir: '))
        
        posicao_nome -=1
        if posicao_nome >=0 and posicao_nome <= len(lista_usuario):
            lista_usuario.insert()


    elif opcao == '6':
        print('Saindo do sistema')
        break        


        