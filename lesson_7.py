import pyinputplus as pyip
    
height = pyip.inputNum('身高:')
weight = pyip.inputNum('體重:')
bmi = weight/((height/100)**2)
print(f'您的BMI是:{bmi:.1f}')
if  bmi >=35:
    print('您的體重:重度肥胖')
elif bmi >=30:
    print('您的體重:中度肥胖')
elif bmi >=27:
    print('您的體重:輕度肥胖')
elif bmi >=24:
    print('您的體重:過重')
elif bmi >=18.5:
    print('您的體重:正常範圍')
else:
    print('您的體重:過輕')