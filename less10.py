

def calc(a, b, *args):

    if arg == '+':
        res = a+b
    elif arg == '-':
        res = a-b
    elif arg == '/':
        res = a/b
    elif arg == '*':
        res = a*b

    else:
        print('Unknown operation')
    return res


a = int(input(f'First num: '))
b = int(input(f'Second num: '))
arg = input(f'Operation: ')
res = calc(a, b, arg)
print(f'Result: {res}')