'''
basic operation system
'''
import os
import shutil

# Path: basicoperationalsystem.py

#constante com o caminho para users.txt
USER_FILE = 'users.txt'
ERRO_MENSAGEM = 'Erro: '
#mensagens

DIRETORIO_MENSAGEM = ' - Nome do diretório: '
ARQUIVO_MENSAGEM = ' - Nome do arquivo: '

#criar um diretório e trata se não for mandado todos os argumentos
def create_dir(dir_name):
    if not os.path.exists(dir_name):
        try:
            os.mkdir(dir_name)
        except OSError as e:
            print(ERRO_MENSAGEM + str(e))

#exclui um diretório e tratar se a pasta não estiver vazia e perguntando se deseja excluir assim mesmo, 
# trata se não for mandado todos os argumentos
def delete_dir(dir_name):
    if os.path.exists(dir_name):
        try:
            os.rmdir(dir_name)
        except OSError as e:
            print(ERRO_MENSAGEM + str(e))
            print('Deseja excluir a pasta e todos os arquivos?')
            if input('Digite s para sim e n para não: ') == 's':
                shutil.rmtree(dir_name)
    
#copia um diretório
# trata se não for mandado todos os argumentos
def copy_dir(dir_name, new_dir_name):
    if os.path.exists(dir_name):
        try:
            shutil.copytree(dir_name, new_dir_name)
        except OSError as e:
            print(ERRO_MENSAGEM + str(e))
            print('Deseja copiar a pasta e todos os arquivos?')
            if input('Digite s para sim e n para não: ') == 's':
                shutil.copytree(dir_name, new_dir_name, ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))

#muda de diretório
def change_dir(dir_name):
    if os.path.exists(dir_name):
        os.chdir(dir_name)

#exibe o conteudo do diretório
def list_dir():
    print('Diretório: ' + get_current_dir())
    for item in os.listdir('.'):
        if os.path.isdir(item):
            print(DIRETORIO_MENSAGEM + item)
        else:
            print(ARQUIVO_MENSAGEM + item)

#exibe o caminho relativo do diretório atual
def get_current_dir():
    return os.getcwd()

#exibe o caminho absoluto do diretório atual
def get_current_dir_abs():
    return os.path.abspath('.')

#criar um arquivo
def create_file(file_name):
    if not os.path.isfile(file_name):
        with open(file_name, 'w'): 
            pass #cria um arquivo vazio

#excluir um arquivo e trata a verificação se o arquivo tem o mesmo nome com extensão diferente
def delete_file(file_name):
    if os.path.isfile(file_name):
        os.remove(file_name)
    else:
        for item in os.listdir('.'):
            if os.path.isfile(item) and item.split('.')[0] == file_name:
                os.remove(item)

#move um arquivo para um diretório
def move_file_to_dir(file_name, dir_name):
    if os.path.isfile(file_name):
        shutil.move(file_name, dir_name)

#comprimir um arquivo
def compress_file(file_name, new_file_name):
    if os.path.isfile(file_name):
        shutil.make_archive(new_file_name, 'zip', './' ,file_name)

#copia um arquivo de um diretório se o diretório não existir ele pergunta se é para criar
def copy_file_from_dir(file_name, dir_name):
    if os.path.isfile(file_name):
        if os.path.isdir(dir_name):
            shutil.copy(file_name, dir_name)
        else:
            print('Diretório não existe')
            if input('Deseja criar o diretório? Digite s para sim e n para não: ') == 's':
                create_dir(dir_name)
                shutil.copy(file_name, dir_name)

#Copia o arquivo e renomeia
def copy_file(file_name, new_file_name):
    if os.path.isfile(file_name):
        shutil.copy(file_name, new_file_name)

#criar usuario com senha para o sistema e salvar em um arquivo
def create_user(user_name, password):
    if not os.path.isfile(USER_FILE):
        with open(USER_FILE, 'w') as f:
            f.write(user_name + ':' + password)
    else:
        with open(USER_FILE, 'a') as f:
            f.write('=' + user_name + ':' + password)

#login de usuario
def login(user_name, password):
    if os.path.isfile(USER_FILE):
        with open(USER_FILE, 'r') as f:
            users = f.read().split('=')
            for user in users:
                if user_name + ':' + password == user:
                    return True
    return False

#limpar a tela 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#help
def help():
    print('''
        Comandos:
        create_dir <dir_name> - cria um diretório
        list_dir - lista o conteúdo do diretório
        delete_dir <dir_name> - exclui um diretório
        copy_dir <dir_name> <new_dir_name> - copia um diretório
        change_dir <dir_name> - muda de diretório
        get_current_dir - exibe o caminho relativo do diretório atual
        get_current_dir_abs - exibe o caminho absoluto do diretório atual
        create_file <file_name> - cria um arquivo
        move_file_to_dir <file_name> <dir_name> - move um arquivo para um diretório
        delete_file <file_name> - exclui um arquivo
        compress_file <file_name> <new_file_name> - comprime um arquivo para .zip
        copy_file_to_dir <file_name> <dir_name> - copia um arquivo para outro diretório
        copy_file <file_name> <new_file_name> - copia o arquivo e renomeia
    ''')


#programa principal
if __name__ == '__main__':
    print('''
    
        ██████╗░░█████╗░░██████╗██╗░█████╗░  ░░░░░░  ░█████╗░░██████╗
        ██╔══██╗██╔══██╗██╔════╝██║██╔══██╗  ░░░░░░  ██╔══██╗██╔════╝
        ██████╦╝███████║╚█████╗░██║██║░░╚═╝  █████╗  ██║░░██║╚█████╗░
        ██╔══██╗██╔══██║░╚═══██╗██║██║░░██╗  ╚════╝  ██║░░██║░╚═══██╗
        ██████╦╝██║░░██║██████╔╝██║╚█████╔╝  ░░░░░░  ╚█████╔╝██████╔╝
        ╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░  ░░░░░░  ░╚════╝░╚═════╝░
    \n\n''')
    print(' - Para ver os comandos digite help')
    print(' - Para sair digite exit')

    #loop do SO, só sai quando o usuário digita exit
    while True:
        command = input(get_current_dir() + '$ ').split(' ')
        if command[0] == 'exit':
            break
        elif command[0] == 'help':
            help()
        elif command[0] == 'create_dir':
            create_dir(command[1])
        elif command[0] == 'delete_dir':
            delete_dir(command[1])
        elif command[0] == 'copy_dir':
            copy_dir(command[1], command[2])
        elif command[0] == 'change_dir':
            change_dir(command[1])
        elif command[0] == 'get_current_dir':
            print(get_current_dir())
        elif command[0] == 'get_current_dir_abs':
            print(get_current_dir_abs())
        elif command[0] == 'create_file':
            create_file(command[1])
        elif command[0] == 'delete_file':
            delete_file(command[1])
        elif command[0] == 'move_file_to_dir':
            move_file_to_dir(command[1], command[2])
        elif command[0] == 'compress_file':
            compress_file(command[1], command[2])
        elif command[0] == 'copy_file_from_dir':
            copy_file_from_dir(command[1], command[2])
        elif command[0] == 'copy_file':
            copy_file(command[1], command[2])
        elif command[0] == 'list_dir':
            list_dir()
        elif command[0] == 'clear':
            clear()
        else:
            print('Comando inválido')
