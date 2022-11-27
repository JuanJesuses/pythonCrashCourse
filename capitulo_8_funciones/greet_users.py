def greet_users(names):
    """ Imprime un simple saludo a cada usuario de la lista. """
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hanna', 'ty', 'margot']
greet_users(usernames)