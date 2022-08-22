import tkinter as tk
root_window =tk.Tk()
# 设置窗口title
root_window.title('测试title')
# 设置窗口大小
root_window.geometry('450x300')
# 左上角窗口的的icon图标
root_window.iconbitmap('./src/astronauthelmet_96198.ico')
# 设置主窗口的背景颜色
root_window["background"] = "#C9C9C9"
# 添加文本内,设置字体的前景色和背景色，和字体类型、大小
text=tk.Label(root_window,text="python真有趣",bg="yellow",\
    fg="red",font=('Times', 20, 'bold italic'))
# 将文本内容放置在主窗口内
text.pack()
# 添加按钮，以及按钮的文本
button=tk.Button(root_window,text="关闭",command=root_window.quit)
# 将按钮放置在主窗口内
button.pack(side="bottom")
#进入主循环，显示主窗口
root_window.mainloop()