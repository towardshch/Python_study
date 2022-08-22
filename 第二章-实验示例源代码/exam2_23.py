import time
wait_list = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
print(wait_list)
for i in range(len(wait_list)):
    for j in range(0, len(wait_list) - i - 1):
        if wait_list[j] > wait_list[j + 1]:
            t = wait_list[j]
            wait_list[j] = wait_list[j + 1]
            wait_list[j + 1] = t
            print(wait_list)
time.sleep(200000)
