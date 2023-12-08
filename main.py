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

print('Hello')

m ={'a', 'b', 'c', 1, 4.4, (1,2,3)}

print(m)

for set_el in m:
    print(set_el)

print('a' in m)

m.add('acd')
print(m)

l1 =[99, 88, 80]
m.update(l1)
print(m)

m.discard('acd')
print(m)

l = [1, 2, 3]
l1 =[]
for i in l:
    l1.append(i+1)

print(l1)

l2 = [i +1 for i in l if i < 2]
print(l2)

l3 = [x for x in range(10)]
print(l3)
d = {x: x+1 for x in range(10)}
print(d)

g = (x*3 for x in range(10))
print(type(g))

for g_el in g:
    print(g_el)


