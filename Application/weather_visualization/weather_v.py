from turtle import *
from random import randint
from time import sleep
import pandas as pd


def get_precip(strs):
    if '大暴雨' in strs:
        return randint(100, 250)
    elif '暴雨' in strs:
        return randint(50, 99)
    elif '大雨' in strs:
        return randint(25, 50)
    elif '中雨' in strs:
        return randint(10, 25)
    elif '小雨' in strs:
        return randint(1, 10)
    else:
        return 0.1


def get_weather(strs):
    if '晴' == strs:
        return 0
    elif '雷阵雨' in strs:
        return 1
    elif '雨' in strs:
        return 2
    elif '风' in strs:
        return 3
    elif '阴' in strs:
        return 4
    elif '多云' in strs:
        return 5
    else:
        return None


def getwindclass(strs):
    if '微风' in strs:
        return 0
    elif '1级' in strs:
        return 1
    elif '小于3级' in strs or '2' in strs:
        return 2
    elif '3-4' in strs:
        return 3
    elif '4-5' in strs:
        return 4
    elif '5-6' in strs:
        return 5
    elif '6-7' in strs:
        return 6
    else:
        return 0


weathers = pd.read_csv('weathers.csv', header=0)
# weathers = weathers.sample(frac=0.3)
# 碰撞声 = 'sound.wav'
w, h = 750, 557
screen = Screen()
screen.delay(0)  # 屏幕延时为1豪秒
screen.bgcolor("black")
screen.setup(w, h)
screen.title("上海天气展示")
screen.addshape('sun.gif')
screen.addshape('rain.gif')
screen.addshape('grandrain.gif')
screen.addshape('sunetclound.gif')
screen.addshape('wind.gif')
screen.addshape('cloud.gif')
screen.addshape('feng.gif')
screen.addshape('temper.gif')
# --------------------------------------------------------------
# 封面设计
封面图 = "地图.gif"
背景图 = "地图.gif"

screen.bgpic(封面图)
screen.update()
sleep(1)
screen.bgpic(背景图)


# --------------------------------------------------------------


class grandrain:
    def __init__(self, num, shape):
        self.order = num
        self.sun = Turtle(shape=shape)
        self.sun.speed(0)  # 速度为最快.
        self.sun.penup()

    def add(self):
        self.sun.goto(-w / 2 + 85 + 130 * self.order, h / 2 - 85)

    def changeto(self, shape):
        self.sun.shape(shape)


class wind:
    def __init__(self, shape):
        self.sun = Turtle(shape=shape)
        self.sun.speed(0)  # 速度为最快.
        self.sun.penup()

    def add(self, num):
        self.sun.goto(w / 2 - 60, h / 2 - 60 - 85 * num)

    def hide(self):
        self.sun.hideturtle()

    def show(self):
        self.sun.showturtle()


weat_obj_dic = {0: 'sun.gif', 1: 'grandrain.gif', 2: 'rain.gif', 3: 'wind.gif', 4: 'cloud.gif', 5: 'sunetclound.gif'}
wea_image = grandrain(0, 'sun.gif')
wea_image.add()
weather_txt = Turtle(visible=False)
weather_txt.penup()
lanban_tx = Turtle(visible=False)
lanban_tx.penup()
wind_dic = {}
for i in range(7):
    wind_dic[i] = wind('feng.gif')
    wind_dic[i].add(i)
wind_txt = Turtle(visible=False)
wind_txt.penup()
temper = Turtle(shape='temper.gif')
temper.penup()
temper.goto(-60, 0 - h / 12)

temp = Turtle(visible=False, shape='square')
temp.penup()
temp.pensize(6)
for i, j in weathers.iterrows():
    exec(','.join(list(j.index)) + "=list(j)")
    wea_code = get_weather(weather)
    wea_image.changeto(weat_obj_dic.get(wea_code))
    weather_txt.goto(-w / 2 + 20, h / 2 - 85 - 200)
    weather_txt.write('日期：%s\n天气：%s\n风向：%s\n风力：%s\n最高气温：%s\n最低气温：%s' % (
        weather_time, weather, wind_direction, wind_power, maximum_temperature, minimum_temperature), align="left",
                      font=("楷体", 16, "bold"))
    wind_info = getwindclass(wind_power)
    temp.goto(-60, 0 - h / 12 - 100)
    temp.color('yellow')
    temp.down()
    temp.goto(-60, 0 - h / 12 - 16 + minimum_temperature * 2)
    temp.color('red')
    temp.goto(-60, 0 - h / 12 - 16 + maximum_temperature * 2)
    temp.penup()
    for i in range(6, wind_info - 1, -1):
        wind_dic[i].hide()
    for i in range(wind_info):
        wind_dic[i].show()
    lanban = Turtle(shape='square', visible=False)
    lanban.penup()
    precip = get_precip(weather)
    if precip > 16:
        lanban.shapesize(15, 2)
        lanban_tx.goto(120, 0 - h / 12 - 15 * 20 / 2 - 25)
    else:
        lanban.shapesize(precip, 2)
        lanban_tx.goto(120, 0 - h / 12 - precip * 20 / 2 - 25)

    lanban.speed(0)
    lanban.color("black", "blue")
    lanban.setx(120)
    lanban.sety(0 - h / 12)
    lanban.showturtle()
    # lanban_tx.goto(120, 0 - h / 12 - precip * 20 / 2 - 25)
    precip_txt = "降雨量为%dmm" % precip if precip > 1 else "无降雨"
    lanban_tx.write(precip_txt, align="center", font=("楷体", 16, "bold"))
    sleep(0.2)
    lanban.shapesize(0.1, 2)
    lanban_tx.clear()
    weather_txt.clear()
    temp.clear()

screen.bgpic("地图.gif")
screen.mainloop()
