
def count(string, lett):
    if len(string) == 0:
        return 0
    return (1 if string[0] == lett else 0) + count(string[1:], lett)

in_str = input('type text: ')
in_lett = input('type letter: ')
res = count(in_str, in_lett)
print(f'in text: {in_str} letter {in_lett} occurs {res} times')