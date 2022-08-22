height=1.75
weight=71
bmi=weight/height**2
print("BMI指数",bmi)
if bmi<18.5:
    print("体重过轻")
elif 18.5<= bmi<25: 
    print("体重正常")
elif bmi>=25 and bmi<28:
    print("体重过重")
elif bmi>=28 and bmi<32:
    print("过于肥胖")
else:
    print("严重肥胖")
