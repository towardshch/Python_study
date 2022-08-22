import time

print("*"*10, "time.sleep()与time.perf_counter()示例", "*"*10)
t1 = time.perf_counter() # 开始时的cpu时间
time.sleep(3) # 暂停三秒
t2 = time.perf_counter() # 结束后的cpu时间
delta = t2 - t1 # cpu时间的差值
print("刚才过去了", delta, "秒")

print("*"*10, "time.strptime()示例", "*"*10)
import time
str="2020-02-15 11:56:30" # 输入时间字符串
print(time.strptime(str,"%Y-%m-%d %H:%M:%S")) # 输出标准化的时间

print("*"*10, "time.strftime()示例", "*"*10)
t=time.gmtime()
std_time = time.strftime("%Y-%m-%d %H:%M:%S" ,t)
print(std_time)

print("*"*10, "time.gemtime()示例", "*"*10)
t = time.gmtime()
year = t.tm_year
print(t)
print(year)

print("*"*10, "time.ctime()示例", "*"*10)
today = time.ctime()
print(today)

print("*"*10, "time.time()示例", "*"*10)
print(time.time())

