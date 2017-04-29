#!/usr/bin/python
# coding=utf-8
from os import system, getcwd


data = '''alias rpi="ssh pi@192.168.1.123"
alias pydir="cd ~/Documents/py/src"
newpy(){
  file_dir=$pwd
  cp ~/Documents/py/src/raspberry/template/base.py $file_dir$1.py
}
enviar(){
	scp "$1" "$rpi_user@$rpi_ip:~/src/"
}
debug(){
	pudb "$1"
}'''

bash_file = open('.bashrc', 'w')
bash_file.write(data)
bash_file.close()
system('sudo mv bashrc ~/.bashrc')
system('source ~/.bashrc')
