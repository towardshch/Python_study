import numpy as np
import matplotlib.pyplot as plt


x1 = np.linspace(0.0, 5.0) # 取0.0至5.0的数据作为x1
x2 = np.linspace(0.0, 2.0) # 取0.0至2.0的数据作为x2

# y1=cos(2Π*x1)*e^(-1)
# y2=cos(2Π*x2)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

#绘制上表
plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'o-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')
#绘制下表
plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

plt.show()