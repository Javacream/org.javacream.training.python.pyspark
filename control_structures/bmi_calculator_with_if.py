name = 'Rainer'
weight = 75.7
height = 183
bmi = weight/(height*height)*10000
print(f'{name} has a body mass index of {bmi:.2f}')

if bmi < 25:
    print('normal') 
else:
    print('obese')
    print('not good')