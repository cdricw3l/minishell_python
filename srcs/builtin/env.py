import os
from interfaces.interface import *

def check_variable(vars: list[str]):
    if (len(vars) == 0):
        return (0)
    i = 0
    while i < len(vars):
        if vars[i] != None and vars[i].find('=') == -1 :
            print("env: " + vars[i]+ ": No such file or directory")
            return (127)
        i += 1
    return (0)

def ft_env(token:Token):
    if (check_variable(token.args) == 127):
        return
    env = list(os.environ.items())
    env.sort()
    i = 0
    while i < len(env):
        print(env[i][0]+"="+env[i][1])
        i += 1
    i = 0
    while i < len(token.args):
        print(token.args[i])
        i += 1
    return 0