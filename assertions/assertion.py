# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    assertion.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cdric.b <cdric.b@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/12 06:15:48 by cdric.b           #+#    #+#              #
#    Updated: 2026/03/13 02:32:48 by cdric.b          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from srcs.tokenizer.tree import display_tree, add_node, Tree
from srcs.builtin.env import ft_env
from srcs.builtin.echo import ft_echo
from srcs.builtin.pwd import ft_pwd
from srcs.interfaces.interface import Token, TokenType
from assertions.utils_assertion import assertion_utils


def assertions():
    ft_echo(Token("echo", ["$PATH", "hello", "world"]))
    #assertion_utils()


assertions()