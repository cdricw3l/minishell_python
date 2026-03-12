# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    assertion.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cdric.b <cdric.b@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/12 06:15:48 by cdric.b           #+#    #+#              #
#    Updated: 2026/03/12 06:21:42 by cdric.b          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from srcs.tree import *
from srcs.utils import *

def assertion_test():
    assert is_commande("ls")
    assert is_commande("lss") == False
    assert is_buildin("pwd")
    assert is_buildin("ls") == False