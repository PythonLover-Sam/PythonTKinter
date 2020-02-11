from tkinter import *


class Application(Frame):
    # Application构造函数，master为窗口的父控件
    def get_x_size(self):
        global x_size
        x_size = self.e1.get()
        var = self.e1.get()
    def get_y_size(self):
        global y_size
        y_size = self.e2.get()
        var = self.e2.get()
    def get_a_size(self):
        global a_size
        a_size = self.e3.get()
        var = self.e3.get()
    def get_d_size(self):
        global d_size
        d_size = self.e4.get()
        var = self.e4.get()
    def get_w_size(self):
        global w_size
        w_size = self.e5.get()
        var = self.e5.get()
    def get_s_size(self):
        global s_size
        s_size = self.e6.get()
        var = self.e6.get()
    def __init__(self, master=None):
        # 初始化Application的Frame部分
        Frame.__init__(self, master)
        # 显示窗口，并使用grid布局
        self.grid()
        # 创建控件
        self.createWidgets()

    def caculate(self):
        global x_size, y_size, a_size, d_size, w_size, s_size
        a = int(x_size)
        b = int(y_size)

        point_list = [[0] * 2 for i in range(a * b)]

        generation = (a - 2) * 100
        for i in range(a * b):
            if i%a == 0:
                point_list[i][0] = float(a_size)
                point_list[i][1] = point_list[i][0]
            if i <= a-1:
                point_list[i][0] = float(w_size)
                point_list[i][1] = point_list[i][0]
            if i >= a*(b-1):
                point_list[i][0] = float(s_size)
                point_list[i][1] = point_list[i][0]
            if (i+1)%a == 0:
                point_list[i][0] = float(d_size)
                point_list[i][1] = point_list[i][0]
        while generation > 0:
            generation -= 1
            cal_x = 1
            cal_y = 1
            for i in range((a - 2) * (b - 2)):
                if cal_x > a - 2 and cal_y < b - 2:
                    cal_y += 1
                    cal_x = 1
                point_list[cal_x + a * cal_y][1] = point_list[cal_x + a * cal_y][0]
                point_list[cal_x + a * cal_y][0] = (point_list[cal_x + a * cal_y - 1][0] +
                                                    point_list[cal_x + a * cal_y + a][0] +
                                                    point_list[cal_x + a * cal_y + 1][1] +
                                                    point_list[cal_x + a * cal_y - a][1]) * 0.25
                cal_x += 1

        show_x = 1
        show_y = 1
        for i in range((a - 2) * (b - 2)):

            if show_x > a - 2 and show_y < b - 2:
                show_y += 1
                show_x = 1
            self.t1.insert("insert", str(point_list[show_x + a * show_y][0]))
            self.t1.insert("insert", '   ')
            show_x += 1
    # 创建控件
    def createWidgets(self):
        # 创建一个文字为'Quit'，点击会退出的按钮
        self.e1 = Entry(self, width=5)
        self.e2 = Entry(self, width=5)
        self.e3 = Entry(self, width=7)
        self.e4 = Entry(self, width=7)
        self.e5 = Entry(self, width=7)
        self.e6 = Entry(self, width=7)
        self.t1 = Text(self, height=15)
        self.b1 = Button(self, text='确定矩阵宽度', command = self.get_x_size)
        self.b2 = Button(self, text='确定矩阵高度', command = self.get_y_size)
        self.b3 = Button(self, text='左侧边界值', command=self.get_a_size)
        self.b4 = Button(self, text='右侧边界值', command=self.get_d_size)
        self.b5 = Button(self, text='上侧边界值', command=self.get_w_size)
        self.b6 = Button(self, text='下侧边界值', command=self.get_s_size)
        self.b7 = Button(self, text='计算', width=10, height=4, command=self.caculate)
        # 显示按钮，并使用grid布局
        self.e1.grid(row=0, column=0)
        self.e2.grid(row=1, column=0)
        self.e3.grid(row=0, column=2)
        self.e4.grid(row=0, column=4)
        self.e5.grid(row=1, column=2)
        self.e6.grid(row=1, column=4)
        self.b1.grid(row=0, column=1)
        self.b2.grid(row=1, column=1)
        self.b3.grid(row=0, column=3)
        self.b4.grid(row=0, column=5)
        self.b5.grid(row=1, column=3)
        self.b6.grid(row=1, column=5)
        self.b7.grid(row=2, column=2)
        self.t1.grid(row=3, column=0, columnspan=6)



# 创建一个Application对象app
app = Application()
# 设置窗口标题为'First Tkinter'
app.master.title('有限差分计算')
# 主循环开始
app.mainloop()



