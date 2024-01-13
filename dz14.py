
def season(m):

   if m>12 or m<1:
       s='unknown'

   elif m%12<3:
       s='Winter'

   elif m<6:
       s='Spring'

   elif m<9:
       s='Summer'

   else:
       s='Autumn'

   return s

print(season(int(input('month: '))))
