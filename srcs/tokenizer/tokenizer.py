# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tokenizer.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cdric.b <cdric.b@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/12 16:07:48 by cdric.b           #+#    #+#              #
#    Updated: 2026/03/12 21:00:15 by cdric.b          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from interfaces.interface import *
from utils.utils import *

def get_token(str: str) -> int :
    if (is_builtin(str)):
        return TokenType(1)