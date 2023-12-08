a = 0
if a <= 10:
    res = a + 1
else:
    res = a+5

print(res)

a = 12
res = a+1 if a <= 10 else a+5
print(res)

l = [1, 2, 3]

try:
    print(l[5])
#except Exception:
 #   print('out of range')

except IndexError as e:
    print(f'Error: {e}')


