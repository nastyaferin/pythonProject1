def three_args(*, var1, var2=None, var3=None):
    arguments = ', '.join([f'{arg[0]} = {str(arg[1])}' for arg in locals().items() if arg[1] is not None])
    print(f'Arguments: {arguments}')

three_args(var1=2, var2='Hello', var3=10)
