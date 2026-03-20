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

def is_on(char:str, charset:str) -> int:
    i = 0
    while (i < len(charset)):
        if(char[0] == charset[i]):
            return (1)
        i += 1
    return (0)



def count_word(s:str, charset:str):
    counter = 0
    i = 0
    while (i < len(s)):
        while (i < len(s) and is_on(s[i], charset) == True):
            i += 1
        if (is_on(s[i], charset) == False):
            counter += 1
        while (i < len(s) and is_on(s[i], charset) == False):
            i += 1
    return (counter)

def ft_split(s:str, charset:str) -> list[str]:
    split = []
    i = 0
    end = 0
    while (i < len(s)):
        while (i < len(s) and is_on(s[i], charset) == True):
            i += 1
        if (is_on(s[i], charset) == False):
            start = i
        while (i < len(s) and is_on(s[i], charset) == False):
            end += 1
            i   += 1
        new_str = s[start:end]
        split.append(new_str)
    return (split)

def here_doc(eof: str):
    here: list[str] = []
    last_word: str = ""
    while (eof != last_word):
        i = input("heredoc> ")
        split = i.split(" ")
        last_word = split[len(split) - 1]
        here.append(i)
    for x in here:
            print(x)

def __main__():
    str = "hello comment ca va?"
    s = ft_split(str, " ")
    print(f"voici count {s}")
    #pynishell("minishell: ")


__main__()
