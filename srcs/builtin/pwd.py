from srcs.interfaces.interface import Token
import os

def ft_pwd(token: Token) -> int:
    if(len(token.args) > 0):
        print(token.value, ": too many arguments")
        return (1)
    path: str = os.getcwd()
    print(path)
    return (0)