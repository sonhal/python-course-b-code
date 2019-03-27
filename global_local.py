
my_global = "GLOBAL!"

def another_cool_function(string):
    my_global = "ENDRET GLOBAL!"
    print(string + my_global)

def cool_function(string):
    print(my_global + string)

