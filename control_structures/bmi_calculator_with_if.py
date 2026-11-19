person = ('Rainer', 75.7, 183)
bmi = person[1]/(person[2]*person[2])*10000

bmi_category = "obese"
if bmi < 18:
    bmi_category = 'underweight' 
elif bmi < 25:
    bmi_category = 'normalweight' 
elif bmi < 30:
    bmi_category = 'overweight' 
print(f'{person[0]} has a body mass index of {bmi:.2f} and therefor is {bmi_category}')
