
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def add_node(root: Tree, node: Tree):
    if (root == None):
        return
    if (root.left == None):
        root.left = node
        print("noeud ajouter a gauche", end="\n")
        return
    if(root.right == None):
        root.right = node
        print("noeud ajouter a droite", end="\n")
        return
    print("les deux enfant sont pris", end="\n")
    add_node(root.left, node)
    add_node(root.right, node)

def display_tree(root:Tree):
    if(root == None):
        return
    display_tree(root.left)
    print("node: ", root.data, end="\n")
    display_tree(root.right)


def test():
    i = 0
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
                add_node(root, Tree(arr[i]))
        display_tree(root)
        

def __main__():
    test()

__main__()