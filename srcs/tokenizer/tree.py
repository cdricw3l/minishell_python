# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tree.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cdric.b <cdric.b@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/12 06:12:10 by cdric.b           #+#    #+#              #
#    Updated: 2026/03/12 06:12:40 by cdric.b          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def add_node(root: Tree, node: Tree):
    if root is None:
        print("return", end="")
        return False
    if root.left is None:
        root.left = node
        print("noeud ajouter a gauche", node.data, end="\n")
        return True
    if root.right is None:
        root.right = node
        print("noeud ajouter a droite",node.data, end="\n")
        return True
    print("les deux enfant sont pris", end="\n")
    if add_node(root.left, node):
        return True
    return add_node(root.right, node)

def display_tree(root:Tree):
    if(root == None):
        return False

    display_tree(root.left)
    display_tree(root.right)
    print("node: ", root.data, end="\n")
    return True