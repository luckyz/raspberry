# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from os import system


RPI_USER = 'pi'
RPI_IP = system("ifconfig | sed -En 's/127.0.0.1//;s/.*inet (addr:)?(([0-9]*\.){3}[0-9]*).*/\2/p'")

f = open('requirements.txt', 'r').readlines()
for line in f:
    flag = False
    command = line.split('|')
    cmd = command[0]
    app = command[1]

    if cmd == 'ppa':
        prefix = 'yes ENTER | '
        code = 'sudo add-apt-repository '
    elif cmd == 'update':
        prefix = ''
        code = 'sudo apt-get update'
    elif cmd == 'apt':
        prefix = 'yes | '
        code = 'sudo apt-get install '
    elif cmd == 'pip':
        prefix = 'yes | '
        code = 'pip install '

    # Install execution
    install = prefix + code + app
    system(install)

    # Aliases
    system('mkdir ~/Documents/py/;mkdir ~/Documents/py/src/;mkdir ~/Documents/py/projects/')
    system('sudo cp bash_profile ~/.bash_profile')
