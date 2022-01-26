def args_function(*args):
    for i in range(len(args)):
        print(args[i])


def args_function2(*args):
    print("Type of the argument(**kwargs) is:", type(args))
    print(args)


args_lst = [1, 20, 30]
args_function(*args_lst)
args_function(args_lst)
args_function2(args_lst)
args_function2(*args_lst)

# KWARGS:
def kwargs_function(**kwargs):
    print("Type of the argument(**kwargs) is:", type(kwargs))
    print(kwargs)


def kwargs_function2(**kwargs):
    for key, value in kwargs.items():
        print(key, " --> ", value)


kwargs_dict = {
    "key1": "val1",
    "key2": "val2",
    "key3": "val3",
    "key4": "val4"
}

kwargs_function(**kwargs_dict)
kwargs_function2(**kwargs_dict)
