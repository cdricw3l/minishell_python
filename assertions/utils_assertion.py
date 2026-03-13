from srcs.utils.utils import is_commande, is_builtin, ft_strncmp

def assertion_is_builtin():
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

def assertion_is_commande():
    assert is_commande("pwd") == False
    assert is_commande("cd") == False
    assert is_commande("echo") == False
    assert is_commande("export") == False
    assert is_commande("unset") == False
    assert is_commande("env") == False
    assert is_commande("ls") == True
    assert is_commande("") == False
    assert is_commande("grep") == True
    assert is_commande("cat") == True
    assert is_commande("hello_worl") == False
    assert is_commande(None) == False

def assertion_ft_strncmp():
    assert ft_strncmp("hello", "hello", 100) == 0
    assert ft_strncmp("hello", "hello", 1) == 0
    assert ft_strncmp("hello", "hello", 0) == 0
    assert ft_strncmp("ello", "hello", len("hello")) == ord('e') - ord('h')
    assert ft_strncmp("", "hello", len("hello")) == 0 - ord('h')

def assertion_utils():
    print("start assertion utils ...")
    assertion_is_builtin()
    assertion_is_commande()
    assertion_ft_strncmp()
    print("assertion utils OK")