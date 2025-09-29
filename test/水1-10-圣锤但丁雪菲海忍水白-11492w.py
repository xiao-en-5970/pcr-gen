from autotimeline import *
import sys
sys.path.append('.')

print("minitouch 连接中")
minitouch.connect("127.0.0.1", 1111)
max_x = minitouch.getMaxX()
max_y = minitouch.getMaxY()
minitouch.setPos("暂停", int(max_x * 0.94), int(max_y * 0.05))
minitouch.setPos("SET", int(max_x * 0.95), int(max_y * 0.64))
minitouch.setPos("AUTO", int(max_x * 0.95), int(max_y * 0.76))
minitouch.setPos("SPEED", int(max_x * 0.95), int(max_y * 0.9))
print("正在运行: /Users/dp/Documents/go-proj/private/pcrv3/test/水1-10-圣锤但丁雪菲海忍水白-11492w.xlsx")
print("圣锤 定位中")
minitouch.setPos("圣锤", int(max_x * 0.74), int(max_y * 0.8))
print("但丁 定位中")
minitouch.setPos("但丁", int(max_x * 0.62), int(max_y * 0.8))
print("雪菲 定位中")
minitouch.setPos("雪菲", int(max_x * 0.50), int(max_y * 0.8))
print("海忍 定位中")
minitouch.setPos("海忍", int(max_x * 0.38), int(max_y * 0.8))
print("水白 定位中")
minitouch.setPos("水白", int(max_x * 0.26), int(max_y * 0.8))
print("解除暂停，塔塔开!")

autopcr.setOffset(2, 0); # offset calibration
autopcr.waitFrame(autopcr.getFrame() + 50); minitouch.press("SPEED") #加速
autopcr.waitFrame(844 - 60); minitouch.press("圣锤") #连点 lframe 844//time 1:16
autopcr.waitFrame(1406 - 60); minitouch.press("海忍") #连点 lframe 1188//time 1:11
autopcr.waitFrame(1692 - 60); minitouch.press("圣锤") #连点 lframe 1201//time 1:10
autopcr.waitFrame(2539 - 60); minitouch.press("雪菲") #连点 lframe 1830//time 1:00
autopcr.waitFrame(2929 - 60); minitouch.press("圣锤") #连点 lframe 1830//time 1:00
# ランドスロース//time 59
autopcr.waitFrame(3590 - 60); minitouch.press("但丁") #连点 lframe 2086//time 56
autopcr.waitFrame(3878 - 60); minitouch.press("水白") #连点 lframe 2086//time 56
autopcr.waitFrame(4207 - 60); minitouch.press("海忍") #连点 lframe 2118//time 55
autopcr.waitFrame(4594 - 60); minitouch.press("圣锤") #连点 lframe 2232//time 53
autopcr.waitFrame(5216 - 60); minitouch.press("圣锤") #连点 lframe 2636//time 47
autopcr.waitFrame(5746 - 60); minitouch.press("海忍") #连点 lframe 2948//time 41
autopcr.waitFrame(6139 - 60); minitouch.press("圣锤") #连点 lframe 3068//time 39
autopcr.waitFrame(6431 - 60); minitouch.press("AUTO") #AUTO开
# 雪菲 AUTO lframe 3142//time 38
autopcr.waitFrame(6431 + 10); minitouch.press("AUTO") #AUTO关
autopcr.waitFrame(6835 - 60); minitouch.press("但丁") #连点 lframe 3156//time 38
autopcr.waitFrame(7467 - 60); minitouch.press("圣锤") #连点 lframe 3500//time 32
# ランドスロース//time 31
autopcr.waitFrame(8156 - 60); minitouch.press("海忍") #连点 lframe 3784//time 27
autopcr.waitFrame(8429 - 60); minitouch.press("水白") #连点 lframe 3784//time 27
autopcr.waitFrame(9000 - 60); minitouch.press("圣锤") #连点 lframe 4058//time 23
autopcr.waitFrame(9585 - 60); minitouch.press("AUTO") #AUTO开
# 雪菲 AUTO lframe 4425//time 17
autopcr.waitFrame(9585 + 10); minitouch.press("AUTO") #AUTO关
autopcr.waitFrame(10019 - 60); minitouch.press("但丁") #连点 lframe 4469//time 16
autopcr.waitFrame(10328 - 60); minitouch.press("圣锤") #连点 lframe 4490//time 16
autopcr.waitFrame(10601 - 60); minitouch.press("海忍") #连点 lframe 4545//time 15
autopcr.waitFrame(11251 - 60); minitouch.press("圣锤") #连点 lframe 4922//time 8
autopcr.waitFrame(11687 - 60); minitouch.press("水白") #连点 lframe 5140//time 5
autopcr.waitFrame(12303 - 60); minitouch.press("暂停") #暂停

#py脚本生成工具:  PCR-Gen
#作者:  小奀Í
#Github:  https://github.com/xiao-en-5970/pcr-gen
