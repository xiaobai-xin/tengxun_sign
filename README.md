# 腾讯课堂自动签到程序
本人水平一般，写的比较垃圾，但是确实能用<br>
本代码的主要目的是学习openCV，本人不对使用本程序造成的任何后果负责！<br>
请务必使用管理员运行，因为点击操作pyautogui.click需要管理员权限，否则无法签到！<br>
我顺便打包了exe,需要的可以到我的博客下载https://xiaobai1103.cn/2022/04/22/tengxun_sign/<br>
说明：<br>
main.py是最开始做的代码，仅具有签到功能<br>
tengxun_auto.py加入了定时启动腾讯课堂并自动进入相应课程<br>
效果如下图所示：<br>
![image](https://user-images.githubusercontent.com/103569755/164979182-0f7fea13-788f-49ee-b145-843b2a559320.png)

注释应该写的挺全的，可以根据需要修改<br>
修改记录：<br>
  Apr 22,2022:增加了签到确认功能，如果签到失败会发出提醒<br>
  Apr 24,2022:增加了定时启动，并自动进入相应课程的功能<br>
  May 11,2022:增加了高校邦自动刷课程序，gaoxiaobang.py
