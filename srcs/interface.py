# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    interface.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cdric.b <cdric.b@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/12 08:44:34 by cdric.b           #+#    #+#              #
#    Updated: 2026/03/12 09:30:42 by cdric.b          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

class Token:
    value: str
    args: list[str]
    left: "Token | None"
    right:"Token | None"
    def __init__(self, value, args: "list[str] | None"):
        self.value = value
        self.args = self.expend_variable(args)
        self.left = None
        self.right = None
    def expend_variable(self, args: "list[str] | None"):
        i = 0
        while (i < len(args)):
            if (args[i][0] == '$'):
                env = list(os.environ.items())
                j = 0
                found = 0
                while (j < len(env)):
                    if (env[j][0] == args[i][1:]):
                        args[i] = env[j][1]
                        found = 1
                    j += 1
                if found == 0:
                    args.remove(args[i])
            i += 1
        return args
    