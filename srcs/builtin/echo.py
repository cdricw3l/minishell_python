from interface import *

def ft_echo(token:Token):
    i = 0
    while (i < len(token.args)):
        if (i < len(token.args) - 1):
            print(token.args[i], end=" ")
        else:
            print(token.args[i], end="\n")
        i += 1
    return (0)