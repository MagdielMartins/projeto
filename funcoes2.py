def loginUsuario(perfil='admin'):

    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

loginUsuario(perfil='Usuário')