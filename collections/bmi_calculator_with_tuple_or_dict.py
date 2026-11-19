person = {'id': 42, 'name': 'Rainer', 'weight': 75.7, 'height': 183}
bmi = person['weight']/(person['height']*person['height'])*10000

bmi_category = "obese"
if bmi < 18:
    bmi_category = 'underweight' 
elif bmi < 25:
    bmi_category = 'normalweight' 
elif bmi < 30:
    bmi_category = 'overweight' 
print(f'{person['name']} has a body mass index of {bmi:.2f} and therefor is {bmi_category}')
