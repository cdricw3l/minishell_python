
from utils import *
from tree import *
from builtin.env import *

def pynishell():
    while(1):
        str = input("minishell: ")
        if (str == 'q'):
            exit(1)
        arr = str.split(" ")
        print("arr: ", arr)
        for i in range(len(arr)):
            if(i == 0):
                root = Tree(arr[i])
            else:
                node = Tree(arr[i])
                add_node(root, node)
        display_tree(root)



def __main__():
        ft_env()

__main__()