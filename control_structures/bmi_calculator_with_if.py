name = 'Rainer'
weight = 75.7
height = 183
bmi = weight/(height*height)*10000

bmi_category = "obese"
if bmi < 18:
    bmi_category = 'underweight' 
elif bmi < 25:
    bmi_category = 'normalweight' 
elif bmi < 30:
    bmi_category = 'overweight' 
print(f'{name} has a body mass index of {bmi:.2f} and therefor is {bmi_category}')
