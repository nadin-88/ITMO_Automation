a : int = 5
b: str ='строка'
c:list = [1, 2]

def indet(s: str, width:int)->str:
    return " "* (max(0, width-len(s))) +s

print(indet('58', 58))


def string_length(s: str ='') -> int:
 return len(s)


def min_list (a: list, b:list) -> int:
    return max(len(a), len(b))


def append_list (my_list :list):
    my_list.append('test')
    return my_list
print(append_list([1, 2, 3]))

def sum_list (my_list:list) -> int:
    result = 0
    for elem in my_list:
        result = result + elem
        return result
    print (sum_list([1, 2 ,3]))


def task_1() -> None:

    '''return: None'''

    var_int = 35
    var_float = 5.14
    var_str = "panda"
    var_list = [1, 2, 3, 4, 5]
    var_bool = True

    print(f"Тип переменной var_int: {type(var_int)}")
    print(f"Тип переменной var_float: {type(var_float)}")
    print(f"Тип переменной var_str: {type(var_str)}")
    print(f"Тип переменной var_list: {type(var_list)}")
    print(f"Тип переменной var_bool: {type(var_bool)}")

task_1()