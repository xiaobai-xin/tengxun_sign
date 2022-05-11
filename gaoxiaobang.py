
'''
    特别说明：本人不对使用该程序造成的任何后果负责，建议合理使用本程序
    该程序签到功能仅在我的电脑实验成功
    请务必用管理员身份运行！
    我的博客:https://xiaobai1103.cn/2022/04/22/tengxun_sign/
    XiaoBai May 11,2022 
'''
import cv2
import pyautogui   #自动GUI操作
import pyscreeze   #屏幕截图
from time import sleep 
count=0 #签到次数 
checkbox_path='C:/pic/checkbox.png'
submit_button_path='C:/pic/submit.png'
continue_button_path='C:/pic/continue.png'
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
 
###选择框####  
target_button=cv2.imread(checkbox_path, cv2.IMREAD_GRAYSCALE)
sp=target_button.shape
checkbox_height=sp[0]
checkbox_width=sp[1]
###提交按钮####  
target_button=cv2.imread(submit_button_path, cv2.IMREAD_GRAYSCALE)
sp=target_button.shape
submit_button_height=sp[0]
submit_button_width=sp[1]
###继续观看按钮####  
target_button=cv2.imread(continue_button_path, cv2.IMREAD_GRAYSCALE)
sp=target_button.shape
continue_button_height=sp[0]
continue_button_width=sp[1]
 
 
while 1:       
    res=check(checkbox_path)#选择框
    if res:
        click(res,checkbox_width,checkbox_height)
        sleep(2)
    
    res=check(submit_button_path)#提交按钮
    if res:
        click(res,submit_button_width,submit_button_height)
        sleep(2)
 
    res=check(continue_button_path)#继续按钮
    if res:
        click(res,continue_button_width,continue_button_height)
        sleep(2)
        res=check(continue_button_path)#再次查找继续按钮
        if res:
            print("出现异常")
        else:
            print("完成课堂测试")
    sleep(3)


