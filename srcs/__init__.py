
# from utils.utils import is_builtin, ft_strncmp, is_commande
from tree import display_tree, add_node, Tree
# from builtin.env import ft_env
# from builtin.echo import ft_echo
# from interfaces.interface import Token, TokenType


def pynishell():

    while (1):
        str = input("minishell: ")
        if (str == 'q'):
            exit(1)
        arr = str.split(" ")
        print("arr: ", arr)
        for i in range(len(arr)):
            if (i == 0):
                root = Tree(arr[i])
            else:
                node = Tree(arr[i])
                add_node(root, node)
        display_tree(root)


def __main__():
    s = "hello"
    i = 0
    while (i < 6):
        print(ord(s[i]))
        i += 1


__main__()
