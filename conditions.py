#Cs104
#jalen Smith 
#Conditions py 

gg = int(input('enter the amount of times you want the program to run: '))
print(' ')
for i in range(gg):
  
  temp = int(input('Please Enter the current temparature: '))
  print(' ')
  if temp > 90:
    print('Wear shorts')
    print(' ')
  elif temp > 70:
    print('short sleeves are fine')
    print(' ')
  elif temp > 50:
    print('wear a jacket')
    print(' ')
  elif temp > 32:
    print('Wear a heavy coat')
    print(' ')

  elif i == gg:
    print('hh')
    
  else:
    print('Stay inside')
    print(' ')
  gg +=1

print('The program has ended..., please run again')
for i in range(1):
    x = input('do u wanna run the program again?: ')
    if x == 'yes' or 'yes':
      print(' ')
      print('haha gotcha, program done')
