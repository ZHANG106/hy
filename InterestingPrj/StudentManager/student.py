stuinfo = []  # 定义列表存所有数据
account = {'root': 'root'}
main_info = """
----------主菜单---------
录入学生信息，请按1
修改学生信息，请按2
显示所有学生信息，请按3
删除学生信息，请按4
统计学生信息，请按5
输出学生信息，请按6
查询学生信息，请按7
保存学生信息，请按8
退出信息系统，请输入0
"""


def menu():  # 显示操作指南
    print(main_info)


def getinfo():  # 定义获取函数
    global newname
    global newsex
    global newmajor
    global newsubject
    global newscore
    global newnumber
    newname = input("请输入学生的姓名：")
    newsex = input("请输入学生的性别：")
    newnumber = int(input("请输入学生的学号："))
    newscore = int(input("请输入学生的分数："))
    return (newname, newsex, newnumber, newscore)  # 将以上数据存在一个元组里


def addinfo():  # 定义添加函数
    ls1 = getinfo()
    newinfo = {}  # 新的信息在一个新的字典里
    newinfo['name'] = ls1[0]
    newinfo['sex'] = ls1[1]
    newinfo['number'] = ls1[2]
    newinfo['score'] = ls1[3]
    stuinfo.append(newinfo)
    print("录入成功")


def modifyinfo():  # 定义修改函数
    num = int(input("请输入要修改的学生编号："))
    getinfo()
    stuinfo[num - 1]['name'] = newname
    stuinfo[num - 1]['sex'] = newsex
    stuinfo[num - 1]['number'] = newnumber
    stuinfo[num - 1]['score'] = newscore
    print("修改成功")


def delinfo():  # 定义删除函数
    delname = input("请输入要删除的学生姓名：")
    for delnum in range(len(stuinfo)):
        if delname == stuinfo[delnum]['name']:
            del stuinfo[delnum]
            print("删除成功")
            break
        else:
            print("未找到该学生")


def seekinfo():  # 定义查询函数
    newname = input("请输入要查询的学生姓名：")
    flag = 0
    for tempinfo in stuinfo:
        if newname == tempinfo['name']:
            flag = 1
            break
        else:
            continue
    if flag == 1:
        print("您要查找的学生信息如下：\n姓名：%s\t性别：%s\t学号：%d\t分数：%d " % (
            tempinfo['name'], tempinfo['sex'], tempinfo['number'], tempinfo['score']))
    else:
        print("很抱歉，未能找到")


def showinfo():  # 显示所有信息
    name = "%s\n学生的信息如下：\n序号\t姓名\t性别\t学号\t成绩\n" % ("=" * 30)
    i = 1
    tx = ''
    for tempinfo in stuinfo:
        tx = tx + "%d\t%s\t%s\t%s\t%d\n" % (
            i, tempinfo['name'], tempinfo['sex'], tempinfo['number'], tempinfo['score'])
        i += 1
    export = name + tx
    print(export)


def saveinfo():  # 保存所有信息
    f = open('data.txt', 'w')
    f.write(str(stuinfo))
    f.close()
    print("保存成功")


def anainfo():
    eachscore = [i.get('score') for i in stuinfo]
    if not eachscore:
        return "无学生信息"
    boy_score = [i.get('score') for i in stuinfo if i.get('sex') == '男']
    maxscore = max(eachscore)
    minscore = min(eachscore)
    sumscore, sum_boy = 0, 0,
    for i in eachscore:
        sumscore += i
    for i in boy_score:
        sum_boy += i
    classaverage = sumscore / len(eachscore)
    if not boy_score:
        boyaverage = "无男生"
    else:
        boyaverage = sum_boy / len(boy_score)
    if (len(eachscore) - len(boy_score)) > 0:
        girlaverage = (sumscore - sum_boy) / (len(eachscore) - len(boy_score))
    else:
        girlaverage = "无女生"
    scoredistribution = {}
    for i in range(10):
        scoredistribution[str(i * 10)] = len([j.get('score') for j in stuinfo if
                                              (float(j.get('score')) < (i + 1) * 10 and float(
                                                  j.get('score')) >= i * 10)])
    fenbuword = '\n'.join(['%s到%s的人数为:\t%s' % (i, int(i) + 10, j) for i, j in scoredistribution.items()])
    badscore_name = ','.join([i.get('name') for i in stuinfo if float(i.get('score')) < 60])
    eachscore.sort(reverse=True)
    score_order = ','.join(map(lambda x: str(x), eachscore))
    export = """
班级平均成绩：\t%s
男生平均成绩：\t%s
女生平均成绩：\t%s
分数段分布：
%s
最高分：\t%s
最低分：\t%s
不及格名单：\t%s
分数排序：\t%s    
    """ % (classaverage, boyaverage, girlaverage, fenbuword, maxscore, minscore, badscore_name, score_order)
    print(export)


def main():
    username = input("请输入用户名:")
    psw = input("请输入密码：")
    if account.get(username) != psw:
        return "用户名或密码错误"
    first = True
    while True:
        if not first:
            input("\n按回车键继续")
        input("请输入要执行的操作编号:")
        menu()
        choice = input("请输入要执行的操作编号:")
        if not (choice >= '0' and choice <= '8'):
            print('请输入0-8的整数数字')
        else:
            if choice == '0':
                print("退出系统")
                break
            elif choice == '1':
                addinfo()
            elif choice == '2':
                modifyinfo()
            elif choice == '3':
                showinfo()
            elif choice == '4':
                delinfo()
            elif choice == '5':
                anainfo()
            # elif choice == 6:
            #     outputinfo()
            elif choice == '7':
                seekinfo()
            elif choice == '8':
                saveinfo()
            else:
                print('无效操作')
                pass
        first = False


if __name__ == '__main__':
    main()  # 调用主函数
