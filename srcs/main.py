from utils.utils import is_builtin, ft_strncmp, is_commande
from tokenizer.tree import display_tree, add_node, Tree
# from builtin.env import ft_env
# from builtin.echo import ft_echo
# from interfaces.interface import Token, TokenType


def pynishell(prompt: str):

    while (1):
        str = input(prompt)
        if (str == 'q'):
            exit(1)
        arr = str.split(" ")
        print("arr: ", arr)

def __main__():
    pynishell("minishell: ")


__main__()
