DataBase=[['zhao',1234],['qian',2234],['sun',3234],['Li',4234]]
usr=input('Enter your name:')
pwd=int(input("Enter your password:"))
if [usr,pwd] in DataBase: # 检查账号密码对是否在DataBase中
    print("Welcome to you!")
else:
    print ("Access denied!")
