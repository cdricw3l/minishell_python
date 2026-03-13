# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cdric.b <cdric.b@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/12 06:12:16 by cdric.b           #+#    #+#              #
#    Updated: 2026/03/13 01:18:25 by cdric.b          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

def is_commande(s: str):
    if  (s == None or len(s) == 0):
            return (False)
    split_path = os.environ["PATH"].split(":")
    for i in split_path:
        if (is_builtin(s) == False) and os.access(i + "/" + s, os.X_OK):
            return (True)
    return (False)


def is_builtin(s: str):
    if  (s == None or len(s) == 0):
        return (False)
    if(s == "echo" or s == "cd" or s == "pwd" or s == "export"
        or s == "unset" or s == "env" or s == "exit"):
        return True
    return False


def ft_strncmp(s1: str, s2: str, size) :
    i = 0

    if (len(s1) == 0 and len(s2) > 0):
        return (0 - ord(s2[0]))
    elif(len(s1) > 0 and len(s2) == 0):
        return (ord(s1[0]) - 0)
    while (i < len(s1) and i < len(s2) and i < size):
        if(ord(s1[i]) != ord(s2[i])):
            return (ord(s1[i]) - ord(s2[i]))
        i += 1
    return (0)
