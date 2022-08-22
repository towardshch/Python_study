m=25
n=20
m1=m 
n1=n
if m1<n1:
    m1,n1=n1,m1 #保证m1>n1
r=m1%n1
while r!=0:
    m1=n1
    n1=r
    r=m1%n1
print(m,n,"的最大公约数是",n1)
