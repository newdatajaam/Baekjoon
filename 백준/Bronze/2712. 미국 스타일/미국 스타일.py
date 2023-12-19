time = int(input())

def change_measure(unit):
  number, measure = unit.split()
  number = float(number)

  if measure == 'g':
    number = number*3.7854, 
    measure = 'l'
  elif measure == 'kg':
    number = number*2.2046, 
    measure = 'lb'
  elif measure == 'l':
    number = number*0.2642, 
    measure = 'g'
  elif measure == 'lb':
    number = number*0.4536, 
    measure = 'kg'

  print('%0.4f' % number, measure)

for i in range(time):
  change_measure(input())