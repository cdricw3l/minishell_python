from srcs.interfaces.interface import *
from srcs.utils.utils import ft_strncmp


def ft_echo(token:Token):
    i = 0
    nl = 1
    if (len(token.args[0]) > 0 and ft_strncmp(token.args[0], "-n", len(token.args[0])) == 0):
        nl = 0
        i = 1
    while (i < len(token.args)):
        if (i < len(token.args) - 1):
            print(token.args[i], end=" ")
        else:
            print(token.args[i], end="")
            if (nl == 1):
                print(end="\n")
        i += 1
    return (0)