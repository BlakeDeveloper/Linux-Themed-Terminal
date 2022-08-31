import subprocess
import os
import getpass
import socket
import time
import psutil
import platform 

def terminal():
    cmds = ['help', 'ls', 'cd', 'clear', 'apt', 'whoami', 'pip', 'python', 'stats', 'cat', 'exit', 'bash', 'fileserver']

    print('''Welcome to SaySomePY's terminal, please use help, for a list of commands.''')

    while True:
        try:

            CURR_DIR = os.getcwd()
            
            cmd = input(f'{getpass.getuser()}@{socket.gethostname()} ({CURR_DIR}) $ ')

            if cmd not in cmds:
                print(f'{cmd}: command was not found')

            if cmd.lower() == 'help':
                print('''
help: Displays all commands.
ls: Gets all the files in the users current directory.
cd: Changes the users directory.
clear: Clears the screen of all text.       
apt: Install a APT package. [Debian based systems only]    
                ''')
            
            elif cmd == 'ls':
                if 'command' in subprocess.getoutput('ls'):
                    out = subprocess.getoutput('dir')
                else:
                    out = subprocess.getoutput('ls')
                print(f'''File(s) in dir: {CURR_DIR}
{out}''')

            elif cmd == 'cd':
                dir = input('DIR: ')

                # Check if the dir exists
                if not os.path.exists(dir):
                    print(f'{dir} does not exist')

                else:
                    os.chdir(dir)
                    CURR_DIR = dir
            
            elif cmd == 'clear':
                out = subprocess.getoutput('clear')

                # If output contains command then run cls
                if 'command' in out:
                    os.system('cls')
                else:
                    os.system('clear')
            
            elif cmd == 'apt':
                package = input('APT Package: ')
                if 'windows' in os.name:
                    return print('APT cannot be used in windows based oses.')
                os.system(f'sudo apt install {package}')

            elif cmd == 'pip':
                print('Checking if pip is installed...')
                time.sleep(3)
                if 'Commands' in subprocess.getoutput('pip'):
                    print('Pip is installed, continuing...')
                    time.sleep(3)
                else:
                    return print('Pip is not installed, please install it before using this command.')

                package = input('Pip package: ')

                os.system(f'pip install {package}')
        
            elif cmd == 'whoami':
                print(f'{getpass.getuser()}')

            elif cmd == 'python':
                for filename in os.listdir():
                    if filename.endswith('.py'):
                        print(f'{filename}')
                    else:
                        print(f'No .py file(s) found in {CURR_DIR}')
                
                file = input('\nPlease select a file from above: ')

                if file not in os.listdir():
                    print(f'The file {file} was not found in {CURR_DIR}')
                else:
                    os.system(f'python {file}')

            elif cmd == 'stats':
                print(f'''Current user: {getpass.getuser()}
Current DIR: {CURR_DIR}
OS: {platform.system()}
CPU Cores: {psutil.cpu_count()}
CPU Used: {psutil.cpu_percent()}%
RAM: {psutil.virtual_memory().total / 1024 / 1024}MB              
                ''')

            elif cmd == 'cat':
                file = input('File to view: ')

                if file not in os.listdir():
                    print(f'The file {file} was not found in {CURR_DIR}')
                else:
                    with open(file, 'r') as f:
                        lines = f.readlines()
                    
                    for line in lines:
                        time.sleep(0.2)
                        print(f'{line}')
                        
            elif cmd == 'exit':
                print('\nThanks for using my python based terminal. Goodbye!')
                exit()
            
            elif cmd == 'bash':
                print('Switching to default shell. (Modified)')
                if 'command' in subprocess.getoutput('clear'):
                    os.system('cls')
                else:
                    os.system('clear')

                while True:
                    try:
                        cmd = input(f'{getpass.getuser()}@{socket.gethostname()} ({CURR_DIR}) $ ')

                        if 'command' in subprocess.getoutput(cmd):
                            print(f'{cmd}: command not found')
                        else:
                            if 'cd' in cmd:
                                print('Since the command doesnt work automatically, please type the dir below.')
                                dir = input('DIR: ')

                                CURR_DIR = dir

                                os.chdir(dir)

                            else:
                                os.system(cmd)


                    except KeyboardInterrupt:
                        print('\nThanks for using my reskin of your systems shell. Bye!')
                        exit()
            
            elif cmd == 'fileserver':
                print('Installing needed mdoules...')
                time.sleep(1)
                os.system('pip3 install http.server')
                os.system('python3 -m http.server')

        except KeyboardInterrupt:
            print('\nThanks for using my python based terminal. Goodbye!')
            exit()

terminal()
