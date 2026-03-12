# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    assertion.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cdric.b <cdric.b@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/12 06:15:48 by cdric.b           #+#    #+#              #
#    Updated: 2026/03/12 23:03:28 by cdric.b          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from srcs.main import *

from srcs.tokenizer.tree import display_tree, add_node, Tree
from srcs.builtin.env import ft_env
from srcs.builtin.echo import ft_echo
from srcs.interfaces.interface import Token, TokenType

def assertion_is_builtin(void):
    assert is_builtin("pwd") == True
    assert is_builtin("cd") == True
    assert is_builtin("echo") == True
    assert is_builtin("export") == True
    assert is_builtin("unset") == True
    assert is_builtin("env") == True
    assert is_builtin("ls") == False
    assert is_builtin("") == False
    assert is_builtin("grep") == False
    assert is_builtin("cat") == False
    assert is_builtin("hello_worl") == False
    assert is_builtin(None) == False

def assertions(void):
    assertion_is_builtin()