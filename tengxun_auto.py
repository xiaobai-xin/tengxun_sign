import subprocess
import datetime 
import cv2
import pyautogui   #自动GUI操作
import pyscreeze   #屏幕截图
from time import sleep 

def check(path):
    target_button=cv2.imread(path, cv2.IMREAD_GRAYSCALE) 
    screenshot=pyscreeze.screenshot('C:/pic/screenshot.png')#截图
    target_screenshot=cv2.imread('C:/pic/screenshot.png', cv2.IMREAD_GRAYSCALE)#cv2读入截屏
    ####获取按钮的宽高####  
    sp=target_button.shape
    button_height=sp[0]
    button_width=sp[1]
    ####图片匹配#####
    result = cv2.matchTemplate(target_screenshot, target_button, cv2.TM_CCOEFF_NORMED)
    mn_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= 0.8:
        return max_loc
    else:
        return 0

def click(max_loc,X,Y):
    ####计算签到按钮位置####                                        
    taget_X=max_loc[0]+int(X/2)
    taget_Y=max_loc[1]+int(Y/2)          
    ###鼠标左键点击所计算的目标点####            
    pyautogui.click(taget_X, taget_Y, button='left') 

print("请选择要签到的课程：1=信息论与编码 2=数字信号处理 3=人工智能")
Lesson=input()
if Lesson=='1':
    target_button=cv2.imread('C:/pic/L1.png', cv2.IMREAD_GRAYSCALE) #信息论
    sp=target_button.shape
    L1_height=sp[0]
    L1_width=sp[1]
elif Lesson=='2':
    target_button=cv2.imread('C:/pic/L2.png', cv2.IMREAD_GRAYSCALE) #数字信号
    sp=target_button.shape
    L1_height=sp[0]
    L1_width=sp[1]
elif Lesson=='3':
    target_button=cv2.imread('C:/pic/L3.png', cv2.IMREAD_GRAYSCALE) #人工智能
    sp=target_button.shape
    sp=target_button.shape
    L1_height=sp[0]
    L1_width=sp[1]
else:
    print("没有找到课程！")

print("设置签到时间，输入hour,min空格隔开:")
hour_input,min_input =map(int,input().split())
count=0
target_button=cv2.imread('C:/pic/in_class.png', cv2.IMREAD_GRAYSCALE) #进入课堂按钮
sp=target_button.shape
in_height=sp[0]
in_width=sp[1]
target_button=cv2.imread('C:/pic/button.png', cv2.IMREAD_GRAYSCALE) #签到按钮
sp=target_button.shape
sign_height=sp[0]
sign_width=sp[1]
target_button=cv2.imread('C:/pic/log.png', cv2.IMREAD_GRAYSCALE) #登录
sp=target_button.shape
log_height=sp[0]
log_width=sp[1]
target_button=cv2.imread('C:/pic/right.png', cv2.IMREAD_GRAYSCALE) #右箭头
sp=target_button.shape
right_height=sp[0]
right_width=sp[1]

while 1:
    hour = datetime.datetime.now().hour
    min = datetime.datetime.now().minute
    if (min>=min_input)&(hour==hour_input):
        subprocess.Popen('C:\\Program Files (x86)\\Tencent\\TXEDU\\2.0.1.54\\bin\\TXEDU.exe')#启动腾讯课堂
        sleep(10)
        res=check('C:/pic/log.png')
        if res:
            click(res,log_width,log_height)#登录
            print("已经登录")
            sleep(10)
            while(1):
                res=check('C:/pic/L1.png')#查找课程L1
                if res:
                    click(res,L1_width,L1_height)#点击打开课程
                    res=check('C:/pic/in_class.png')
                    click(res,in_width,in_height)#点击进入直播
                    print("已经打开课程，接下来将为您自动签到")
                    while 1:
                        res=check('C:/pic/button.png')#查找签到按钮
                        if res:
                            click(res,sign_width,sign_height)#点击签到
                            sleep(3)
                            res=check('C:/pic/button.png')#再次检查签到按钮是否存在
                            if res:
                                print("警告：签到可能失败，请及时确认！")
                            else:
                                count+=1
                                print("已经完成",count,"次签到")
                        sleep(5)
                else :
                    res=check('C:/pic/right.png')
                    click(res,right_width,right_height)#下一页
                    sleep(5)



