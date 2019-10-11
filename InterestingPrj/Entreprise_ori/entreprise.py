import tkinter as tk
import tkinter.messagebox as messagebox

usrs_info = {"18110011001": "18110011001", "18110011002": "18110011002", "18110011003": "18110011003", "1": "1"}
# 定义用户名与密码
root = tk.Tk()
root.title("公司系统")  # 名字
root.geometry("350x300")  # 长宽
tk.Label(root, text='请输入工号：').place(x=50, y=150)  # 标签控件，显示文本和位图
tk.Label(root, text='密码：').place(x=50, y=190)
var_usr_name = tk.StringVar()
var_usr_name.set('18110011xxx')  # 提示用户输入格式
entry_usr_name = tk.Entry(root, textvariable=var_usr_name)  # 输入控件
entry_usr_name.place(x=160, y=150)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(root, textvariable=var_usr_pwd, show='*')  # 输入密码用***显示
entry_usr_pwd.place(x=160, y=190)


def generate_login_gui():  # 生成新的tk对象，登录成功时调用它生成一个新的tk对象同时摧毁旧的登录界面
    rt2 = tk.Tk(className='老板界面')
    rt2.geometry("400x400")

    tk.Label(rt2, text="今日工作计划：").place(x=50, y=50)  # 标签控件，显示提示文本内容
    var_day_plan = tk.StringVar()
    entry_day_plan = tk.Entry(rt2, textvariable=var_day_plan)
    entry_day_plan.place(x=160, y=50)
    btn_login = tk.Button(rt2, text='发布')
    btn_login.place(x=320, y=50)

    tk.Label(rt2, text="工作完成反馈：").place(x=50, y=150)  # 标签控件
    var_day_finish = tk.StringVar()
    entry_day_finish = tk.Entry(rt2, textvariable=var_day_finish)
    entry_day_finish.place(x=160, y=150)

    tk.Label(rt2, text="评分：").place(x=50, y=250)  # 标签控件
    var_stander = tk.StringVar()
    entry_stander = tk.Entry(rt2, textvariable=var_stander)
    entry_stander.place(x=160, y=250)
    btn_login = tk.Button(rt2, text='提交')
    btn_login.place(x=320, y=250)

    return rt2


def generate_login_gui3():  # 生成新的tk对象，登录成功时调用它生成一个新的tk对象同时摧毁旧的登录界面
    rt3 = tk.Tk(className='员工界面')
    rt3.geometry("400x400")
    tk.Label(rt3, text="今日工作计划：").place(x=50, y=50)  # 标签控件，显示提示文本内容
    var_day_plan = tk.StringVar()
    entry_day_plan = tk.Entry(rt3, textvariable=var_day_plan)
    entry_day_plan.place(x=160, y=50)
    tk.Label(rt3, text="完成情况：").place(x=50, y=250)  # 标签控件
    var_stander = tk.StringVar()
    entry_stander = tk.Entry(rt3, textvariable=var_stander)
    entry_stander.place(x=160, y=250)
    btn_login = tk.Button(rt3, text='提交')
    btn_login.place(x=320, y=250)

    return rt3


def generate_login_gui4():  # 生成新的tk对象，登录成功时调用它生成一个新的tk对象同时摧毁旧的登录界面
    rt4 = tk.Tk(className='人力界面')
    rt4.geometry("500x500")
    tk.Label(rt4, text="员工完成情况：").place(x=50, y=50)  # 标签控件，显示提示文本内容
    var_day_plan = tk.StringVar()
    entry_day_plan = tk.Entry(rt4, textvariable=var_day_plan)
    entry_day_plan.place(x=160, y=50)

    tk.Label(rt4, text="考核人评分：").place(x=50, y=150)  # 标签控件
    var_score = tk.StringVar()
    entry_score = tk.Entry(rt4, textvariable=var_score)
    entry_score.place(x=160, y=150)

    tk.Label(rt4, text="薪酬状况：").place(x=50, y=250)  # 标签控件
    var_money = tk.StringVar()
    entry_money = tk.Entry(rt4, textvariable=var_money)
    entry_money.place(x=160, y=250)
    btn_login = tk.Button(rt4, text='计算')
    btn_login.place(x=320, y=250)

    tk.Label(rt4, text="薪酬合理系数：").place(x=50, y=350)  # 标签控件
    var_k = tk.StringVar()
    entry_k = tk.Entry(rt4, textvariable=var_k)
    entry_k.place(x=160, y=350)
    btn_login = tk.Button(rt4, text='确认')
    btn_login.place(x=200, y=450)

    return rt4


def usr_login():  # 用户输入
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    if usr_name == '18110011001':
        if usr_pwd == usrs_info[usr_name]:  # 密码与用户名都正确
            root.destroy()
            rt2 = generate_login_gui()
            rt2.mainloop()
            # dialog.showinfo(title='Welcome', message='How are you?' + usr_name)
        else:
            messagebox.showerror(message='Error, your password is wrong, try again.')  # 密码错误
    elif usr_name == '18110011002':
        if usr_pwd == usrs_info[usr_name]:  # 密码与用户名都正确
            root.destroy()
            rt3 = generate_login_gui3()
            rt3.mainloop()
            # dialog.showinfo(title='Welcome', message='How are you?' + usr_name)
    elif usr_name == '18110011003':
        if usr_pwd == usrs_info[usr_name]:  # 密码与用户名都正确
            root.destroy()
            rt4 = generate_login_gui4()
            rt4.mainloop()
            # dialog.showinfo(title='Welcome', message='How are you?' + usr_name)
        else:
            messagebox.showerror(message='Error, your password is wrong, try again.')  # 密码错误

    else:
        messagebox.showerror(message='Error, no account found, try again.')  # 未找到该账号


btn_login = tk.Button(root, text='登录', command=usr_login)
btn_login.place(x=170, y=230)

root.mainloop()
