import os

def check_variable(*var: str):
    if (len(var) == 0):
        return (0)
    if var.find('=') == -1 :
        print("env: " + str(var)+ ": No such file or directory")
        return (127)
    return (0)

def ft_env(*var:str):
    if (check_variable(var) == 127):
        return
    env = list(os.environ.items())
    env.sort()
    i = 0
    while i < len(env):
        print(env[i][0]+"="+env[i][1])
        i += 1
    print(var)
    return 0