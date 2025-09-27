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
print("松鼠 定位中")
minitouch.setPos("松鼠", int(max_x * 0.74), int(max_y * 0.8))
print("水花 定位中")
minitouch.setPos("水花", int(max_x * 0.62), int(max_y * 0.8))
print("似似花 定位中")
minitouch.setPos("似似花", int(max_x * 0.50), int(max_y * 0.8))
print("真步 定位中")
minitouch.setPos("真步", int(max_x * 0.38), int(max_y * 0.8))
print("江雪 定位中")
minitouch.setPos("江雪", int(max_x * 0.26), int(max_y * 0.8))
print("解除暂停，塔塔开!")

autopcr.setOffset(2, 0); # offset calibration
autopcr.waitFrame(autopcr.getFrame() + 50); minitouch.press("SPEED") #加速
autopcr.waitFrame(1098 - 120); minitouch.press("SPEED") #减速
autopcr.waitFrame(1098); minitouch.press("松鼠") #lframe 1098//time 1:12
autopcr.waitFrame(1098 + 30); minitouch.press("SPEED") #加速 
autopcr.waitFrame(1480 - 60); minitouch.press("松鼠") #连点 lframe 1192//time 1:11
autopcr.waitFrame(1783 - 60); minitouch.press("真步") #连点 lframe 1207//time 1:10
autopcr.waitFrame(2295 - 60); minitouch.press("水花") #连点 lframe 1329//time 1:08
autopcr.waitFrame(2627 - 120); minitouch.press("SPEED") #减速
autopcr.waitFrame(2627); minitouch.press("江雪") #lframe 1402//time 1:07
autopcr.waitFrame(2627 + 30); minitouch.press("SPEED") #加速 
autopcr.waitFrame(2942 - 60); minitouch.press("松鼠") #连点 lframe 1441//time 1:06
autopcr.waitFrame(3259 - 120); minitouch.press("SPEED") #减速
autopcr.waitFrame(3259); minitouch.press("似似花") #lframe 1470//time 1:06
autopcr.waitFrame(3259 + 30); minitouch.press("SPEED") #加速 
autopcr.waitFrame(3505 - 60); minitouch.press("松鼠") #连点 lframe 1505//time 1:05
#BOSS  UB//time 1:05
autopcr.waitFrame(4341 - 60); minitouch.press("真步") #连点 lframe 1573//time 1:04
autopcr.waitFrame(4774 - 60); minitouch.press("水花") #连点 lframe 1616//time 1:04
autopcr.waitFrame(5190 - 120); minitouch.press("SPEED") #减速
autopcr.waitFrame(5190); minitouch.press("江雪") #lframe 1773//time 1:01
autopcr.waitFrame(5190 + 30); minitouch.press("SPEED") #加速 
autopcr.waitFrame(5466 - 60); minitouch.press("松鼠") #连点 lframe 1773//time 1:01
autopcr.waitFrame(5847 - 120); minitouch.press("SPEED") #减速
autopcr.waitFrame(5847); minitouch.press("似似花") #lframe 1866//time 59
autopcr.waitFrame(5847 + 30); minitouch.press("SPEED") #加速 
autopcr.waitFrame(6058 - 60); minitouch.press("真步") #连点 lframe 1866//time 59
autopcr.waitFrame(6448 - 60); minitouch.press("水花") #连点 lframe 1866//time 59
autopcr.waitFrame(6750 - 60); minitouch.press("松鼠") #连点 lframe 1909//time 59
autopcr.waitFrame(7112 - 60); minitouch.press("似似花") #连点 lframe 1983//time 57
autopcr.waitFrame(7362 - 60); minitouch.press("松鼠") #连点 lframe 2022//time 57
autopcr.waitFrame(7650 - 60); minitouch.press("江雪") #连点 lframe 2022//time 57
autopcr.waitFrame(8028 - 60); minitouch.press("真步") #连点 lframe 2124//time 55
autopcr.waitFrame(8418 - 60); minitouch.press("水花") #连点 lframe 2124//time 55
autopcr.waitFrame(8747 - 60); minitouch.press("似似花") #连点 lframe 2194//time 54
autopcr.waitFrame(8965 - 60); minitouch.press("江雪") #连点 lframe 2201//time 54
#BOSS  UB//time 54
autopcr.waitFrame(9762 - 60); minitouch.press("松鼠") #连点 lframe 2242//time 53
autopcr.waitFrame(10173 - 60); minitouch.press("水花") #连点 lframe 2365//time 51
autopcr.waitFrame(10432 - 60); minitouch.press("真步") #连点 lframe 2365//time 51
autopcr.waitFrame(10834 - 60); minitouch.press("松鼠") #连点 lframe 2377//time 51
autopcr.waitFrame(11122 - 60); minitouch.press("似似花") #连点 lframe 2377//time 51
autopcr.waitFrame(11333 - 60); minitouch.press("江雪") #连点 lframe 2377//time 51
autopcr.waitFrame(11676 - 60); minitouch.press("水花") #连点 lframe 2444//time 50
autopcr.waitFrame(11941 - 60); minitouch.press("松鼠") #连点 lframe 2450//time 50
autopcr.waitFrame(12265 - 60); minitouch.press("真步") #连点 lframe 2486//time 49
autopcr.waitFrame(12655 - 60); minitouch.press("似似花") #连点 lframe 2486//time 49
autopcr.waitFrame(12866 - 60); minitouch.press("江雪") #连点 lframe 2486//time 49
autopcr.waitFrame(13179 - 60); minitouch.press("水花") #连点 lframe 2523//time 48
autopcr.waitFrame(13495 - 60); minitouch.press("真步") #连点 lframe 2580//time 47
autopcr.waitFrame(13495 - 60 + 60); minitouch.press("松鼠") #连点 lframe 2580//time 47
autopcr.waitFrame(13495 - 60 + 120); minitouch.press("似似花") #连点 lframe 2580//time 46
autopcr.waitFrame(14445 - 60); minitouch.press("江雪") #连点 lframe 2641//time 46
autopcr.waitFrame(14802 - 60); minitouch.press("AUTO") #AUTO开
# 水花 AUTO lframe 2722//time 45
autopcr.waitFrame(14802 + 10); minitouch.press("AUTO") #AUTO关
autopcr.waitFrame(15068 - 60); minitouch.press("松鼠") #连点 lframe 2729//time 45
autopcr.waitFrame(15362 - 60); minitouch.press("真步") #连点 lframe 2735//time 45
autopcr.waitFrame(15752 - 60); minitouch.press("江雪") #连点 lframe 2735//time 45
autopcr.waitFrame(16057 - 60); minitouch.press("水花") #连点 lframe 2764//time 44
autopcr.waitFrame(16316 - 60); minitouch.press("似似花") #连点 lframe 2764//time 44
autopcr.waitFrame(16559 - 60); minitouch.press("真步") #连点 lframe 2796//time 44
autopcr.waitFrame(16949 - 60); minitouch.press("松鼠") #连点 lframe 2796//time 44
autopcr.waitFrame(17252 - 60); minitouch.press("江雪") #连点 lframe 2811//time 44
autopcr.waitFrame(17557 - 60); minitouch.press("似似花") #连点 lframe 2840//time 43
autopcr.waitFrame(17771 - 60); minitouch.press("水花") #连点 lframe 2843//time 43
autopcr.waitFrame(18072 - 60); minitouch.press("真步") #连点 lframe 2885//time 42
autopcr.waitFrame(18468 - 60); minitouch.press("似似花") #连点 lframe 2891//time 42
autopcr.waitFrame(18679 - 60); minitouch.press("江雪") #连点 lframe 2891//time 42
autopcr.waitFrame(18977 - 60); minitouch.press("松鼠") #连点 lframe 2913//time 42
autopcr.waitFrame(19274 - 60); minitouch.press("水花") #连点 lframe 2922//time 42
autopcr.waitFrame(19579 - 60); minitouch.press("真步") #连点 lframe 2968//time 41
autopcr.waitFrame(19969 - 60); minitouch.press("水花") #连点 lframe 2968//time 41
autopcr.waitFrame(20264 - 120); minitouch.press("SPEED") #减速
autopcr.waitFrame(20264); minitouch.press("似似花") #lframe 3004//time 40
autopcr.waitFrame(20264 + 30); minitouch.press("SPEED") #加速 
autopcr.waitFrame(20511 - 60); minitouch.press("松鼠") #连点 lframe 3040//time 40
autopcr.waitFrame(20799 - 60); minitouch.press("江雪") #连点 lframe 3040//time 40
autopcr.waitFrame(21092 - 60); minitouch.press("真步") #连点 lframe 3057//time 40
autopcr.waitFrame(21482 - 60); minitouch.press("水花") #连点 lframe 3057//time 40
autopcr.waitFrame(21764 - 60); minitouch.press("似似花") #连点 lframe 3080//time 39
autopcr.waitFrame(22023 - 60); minitouch.press("水花") #连点 lframe 3128//time 38
autopcr.waitFrame(22282 - 60); minitouch.press("江雪") #连点 lframe 3128//time 38
autopcr.waitFrame(22576 - 60); minitouch.press("真步") #连点 lframe 3146//time 38
autopcr.waitFrame(22966 - 60); minitouch.press("松鼠") #连点 lframe 3146//time 38
autopcr.waitFrame(23254 - 60); minitouch.press("水花") #连点 lframe 3146//time 38
autopcr.waitFrame(23529 - 60); minitouch.press("似似花") #连点 lframe 3162//time 38
autopcr.waitFrame(23785 - 60); minitouch.press("江雪") #连点 lframe 3207//time 37
#BOSS  UB//time 37
autopcr.waitFrame(24563 - 60); minitouch.press("真步") #连点 lframe 3229//time 37
autopcr.waitFrame(24953 - 60); minitouch.press("水花") #连点 lframe 3229//time 37
autopcr.waitFrame(25267 - 60); minitouch.press("似似花") #连点 lframe 3284//time 36
autopcr.waitFrame(25512 - 60); minitouch.press("真步") #连点 lframe 3318//time 35
autopcr.waitFrame(25902 - 60); minitouch.press("松鼠") #连点 lframe 3318//time 35
autopcr.waitFrame(26190 - 60); minitouch.press("江雪") #连点 lframe 3318//time 35
autopcr.waitFrame(26527 - 60); minitouch.press("似似花") #连点 lframe 3379//time 34
autopcr.waitFrame(26740 - 120); minitouch.press("SPEED") #减速
autopcr.waitFrame(26740); minitouch.press("水花") #lframe 3381//time 34
autopcr.waitFrame(26740 + 30); minitouch.press("SPEED") #加速 
autopcr.waitFrame(27025 - 60); minitouch.press("真步") #连点 lframe 3407//time 34
autopcr.waitFrame(27431 - 60); minitouch.press("水花") #连点 lframe 3423//time 33
autopcr.waitFrame(27735 - 60); minitouch.press("似似花") #连点 lframe 3468//time 33
autopcr.waitFrame(27957 - 60); minitouch.press("AUTO") #AUTO开
# 江雪 AUTO lframe 3479//time 33
autopcr.waitFrame(27957 + 10); minitouch.press("AUTO") #AUTO关
autopcr.waitFrame(28233 - 60); minitouch.press("真步") #连点 lframe 3479//time 33
autopcr.waitFrame(28646 - 60); minitouch.press("水花") #连点 lframe 3502//time 32
autopcr.waitFrame(28970 - 60); minitouch.press("水花") #连点 lframe 3567//time 31
autopcr.waitFrame(29229 - 60); minitouch.press("松鼠") #连点 lframe 3567//time 31
autopcr.waitFrame(29517 - 60); minitouch.press("江雪") #连点 lframe 3567//time 31
autopcr.waitFrame(29794 - 60); minitouch.press("真步") #连点 lframe 3568//time 31
autopcr.waitFrame(30199 - 60); minitouch.press("水花") #连点 lframe 3583//time 31
autopcr.waitFrame(30458 - 60); minitouch.press("似似花") #连点 lframe 3583//time 31
autopcr.waitFrame(30737 - 60); minitouch.press("真步") #连点 lframe 3651//time 30
autopcr.waitFrame(31127 - 60); minitouch.press("松鼠") #连点 lframe 3651//time 30
autopcr.waitFrame(31415 - 60); minitouch.press("水花") #连点 lframe 3651//time 30
autopcr.waitFrame(31708 - 60); minitouch.press("似似花") #连点 lframe 3685//time 29
autopcr.waitFrame(31962 - 60); minitouch.press("AUTO") #AUTO开
# 江雪 AUTO lframe 3728//time 28
autopcr.waitFrame(31962 + 10); minitouch.press("AUTO") #AUTO关
autopcr.waitFrame(32250 - 60); minitouch.press("真步") #连点 lframe 3740//time 28
autopcr.waitFrame(32640 - 60); minitouch.press("水花") #连点 lframe 3740//time 28
autopcr.waitFrame(32960 - 60); minitouch.press("似似花") #连点 lframe 3801//time 27
autopcr.waitFrame(33186 - 60); minitouch.press("水花") #连点 lframe 3816//time 27
autopcr.waitFrame(33445 - 60); minitouch.press("江雪") #连点 lframe 3816//time 27
autopcr.waitFrame(33734 - 60); minitouch.press("真步") #连点 lframe 3829//time 27
autopcr.waitFrame(34124 - 60); minitouch.press("松鼠") #连点 lframe 3829//time 27
autopcr.waitFrame(34412 - 60); minitouch.press("水花") #连点 lframe 3829//time 27
autopcr.waitFrame(34732 - 60); minitouch.press("似似花") #连点 lframe 3890//time 26
autopcr.waitFrame(34945 - 60); minitouch.press("江雪") #连点 lframe 3892//time 26
autopcr.waitFrame(35241 - 60); minitouch.press("真步") #连点 lframe 3912//time 25
autopcr.waitFrame(35631 - 60); minitouch.press("水花") #连点 lframe 3912//time 25
autopcr.waitFrame(35968 - 60); minitouch.press("似似花") #连点 lframe 3990//time 24
autopcr.waitFrame(36183 - 60); minitouch.press("松鼠") #连点 lframe 3994//time 24
autopcr.waitFrame(36478 - 60); minitouch.press("真步") #连点 lframe 4001//time 24
autopcr.waitFrame(36868 - 60); minitouch.press("江雪") #连点 lframe 4001//time 24
autopcr.waitFrame(37207 - 120); minitouch.press("SPEED") #减速
autopcr.waitFrame(37207); minitouch.press("水花") #lframe 4064//time 23
autopcr.waitFrame(37207 + 30); minitouch.press("SPEED") #加速 
autopcr.waitFrame(37492 - 60); minitouch.press("真步") #连点 lframe 4090//time 22
autopcr.waitFrame(37882 - 60); minitouch.press("松鼠") #连点 lframe 4090//time 22
autopcr.waitFrame(38186 - 60); minitouch.press("水花") #连点 lframe 4106//time 22
autopcr.waitFrame(38445 - 60); minitouch.press("似似花") #连点 lframe 4106//time 22
autopcr.waitFrame(38712 - 60); minitouch.press("AUTO") #AUTO开
# 江雪 AUTO lframe 4162//time 21
autopcr.waitFrame(38712 + 10); minitouch.press("AUTO") #AUTO关
autopcr.waitFrame(38988 - 60); minitouch.press("真步") #连点 lframe 4162//time 21
autopcr.waitFrame(39401 - 60); minitouch.press("水花") #连点 lframe 4185//time 21
autopcr.waitFrame(39725 - 60); minitouch.press("水花") #连点 lframe 4250//time 20
autopcr.waitFrame(39984 - 60); minitouch.press("似似花") #连点 lframe 4250//time 20
autopcr.waitFrame(40195 - 60); minitouch.press("江雪") #连点 lframe 4250//time 20
autopcr.waitFrame(40472 - 60); minitouch.press("真步") #连点 lframe 4251//time 20
autopcr.waitFrame(40862 - 60); minitouch.press("松鼠") #连点 lframe 4251//time 20
autopcr.waitFrame(41165 - 60); minitouch.press("水花") #连点 lframe 4266//time 19
autopcr.waitFrame(41484 - 60); minitouch.press("江雪") #连点 lframe 4326//time 18
autopcr.waitFrame(41768 - 60); minitouch.press("真步") #连点 lframe 4334//time 18
autopcr.waitFrame(42158 - 60); minitouch.press("似似花") #连点 lframe 4334//time 18
autopcr.waitFrame(42369 - 60); minitouch.press("水花") #连点 lframe 4334//time 18
autopcr.waitFrame(42689 - 60); minitouch.press("江雪") #连点 lframe 4395//time 17
autopcr.waitFrame(42993 - 60); minitouch.press("真步") #连点 lframe 4423//time 17
autopcr.waitFrame(43383 - 60); minitouch.press("松鼠") #连点 lframe 4423//time 17
autopcr.waitFrame(43671 - 60); minitouch.press("水花") #连点 lframe 4423//time 17
autopcr.waitFrame(43954 - 120); minitouch.press("SPEED") #减速
autopcr.waitFrame(43954); minitouch.press("似似花") #lframe 4447//time 16
autopcr.waitFrame(43954 + 30); minitouch.press("SPEED") #加速 
autopcr.waitFrame(44208 - 120); minitouch.press("SPEED") #减速
autopcr.waitFrame(44208); minitouch.press("江雪") #lframe 4490//time 16
autopcr.waitFrame(44208 + 30); minitouch.press("SPEED") #加速 
autopcr.waitFrame(44506 - 60); minitouch.press("真步") #连点 lframe 4512//time 15
autopcr.waitFrame(44896 - 60); minitouch.press("水花") #连点 lframe 4512//time 15
autopcr.waitFrame(45194 - 60); minitouch.press("似似花") #连点 lframe 4551//time 15
autopcr.waitFrame(45432 - 60); minitouch.press("水花") #连点 lframe 4578//time 14
autopcr.waitFrame(45691 - 60); minitouch.press("江雪") #连点 lframe 4578//time 14
autopcr.waitFrame(45984 - 60); minitouch.press("真步") #连点 lframe 4595//time 14
autopcr.waitFrame(46374 - 60); minitouch.press("松鼠") #连点 lframe 4595//time 14
autopcr.waitFrame(46662 - 60); minitouch.press("水花") #连点 lframe 4595//time 14
autopcr.waitFrame(46982 - 60); minitouch.press("似似花") #连点 lframe 4656//time 13
autopcr.waitFrame(47221 - 60); minitouch.press("真步") #连点 lframe 4684//time 12
#BOSS  UB//time 11
autopcr.waitFrame(48169 - 60); minitouch.press("水花") #连点 lframe 4762//time 11
autopcr.waitFrame(48439 - 60); minitouch.press("真步") #连点 lframe 4773//time 11
autopcr.waitFrame(48829 - 60); minitouch.press("松鼠") #连点 lframe 4773//time 11
autopcr.waitFrame(49117 - 60); minitouch.press("似似花") #连点 lframe 4773//time 11
autopcr.waitFrame(49359 - 60); minitouch.press("水花") #连点 lframe 4804//time 10
autopcr.waitFrame(49641 - 60); minitouch.press("水花") #连点 lframe 4827//time 10
autopcr.waitFrame(49900 - 60); minitouch.press("江雪") #连点 lframe 4827//time 10
autopcr.waitFrame(50183 - 60); minitouch.press("真步") #连点 lframe 4834//time 10
autopcr.waitFrame(50588 - 60); minitouch.press("似似花") #连点 lframe 4849//time 10
autopcr.waitFrame(50835 - 60); minitouch.press("水花") #连点 lframe 4885//time 9
autopcr.waitFrame(51112 - 60); minitouch.press("江雪") #连点 lframe 4903//time 9
autopcr.waitFrame(51408 - 60); minitouch.press("真步") #连点 lframe 4923//time 8
autopcr.waitFrame(51798 - 60); minitouch.press("松鼠") #连点 lframe 4923//time 8
autopcr.waitFrame(52127 - 60); minitouch.press("水花") #连点 lframe 4964//time 8
autopcr.waitFrame(52386 - 60); minitouch.press("似似花") #连点 lframe 4964//time 8
autopcr.waitFrame(52639 - 60); minitouch.press("真步") #连点 lframe 5006//time 7
autopcr.waitFrame(53029 - 60); minitouch.press("江雪") #连点 lframe 5006//time 7
autopcr.waitFrame(53305 - 60); minitouch.press("水花") #连点 lframe 5006//time 7
autopcr.waitFrame(53609 - 60); minitouch.press("似似花") #连点 lframe 5051//time 6
autopcr.waitFrame(53864 - 60); minitouch.press("真步") #连点 lframe 5095//time 6
autopcr.waitFrame(54254 - 60); minitouch.press("松鼠") #连点 lframe 5095//time 6
autopcr.waitFrame(54542 - 60); minitouch.press("水花") #连点 lframe 5095//time 6
autopcr.waitFrame(54873 - 60); minitouch.press("AUTO") #AUTO开
# 江雪 AUTO lframe 5167//time 4
autopcr.waitFrame(54873 + 10); minitouch.press("AUTO") #AUTO关
autopcr.waitFrame(55166 - 60); minitouch.press("真步") #连点 lframe 5184//time 4
autopcr.waitFrame(55556 - 60); minitouch.press("水花") #连点 lframe 5184//time 4
autopcr.waitFrame(55886 - 60); minitouch.press("水花") #连点 lframe 5255//time 3
autopcr.waitFrame(56145 - 60); minitouch.press("似似花") #连点 lframe 5255//time 3
autopcr.waitFrame(56356 - 60); minitouch.press("江雪") #连点 lframe 5255//time 3
autopcr.waitFrame(56643 - 60); minitouch.press("松鼠") #连点 lframe 5266//time 3
autopcr.waitFrame(56932 - 60); minitouch.press("真步") #连点 lframe 5267//time 3
autopcr.waitFrame(57405 - 60); minitouch.press("AUTO") #AUTO开
# 水花 AUTO lframe 5350//time 1
autopcr.waitFrame(57405 + 10); minitouch.press("AUTO") #AUTO关
autopcr.waitFrame(57670 - 60); minitouch.press("真步") #连点 lframe 5356//time 1
autopcr.waitFrame(58096 - 60); minitouch.press("水花") #连点 lframe 5392//time 1
autopcr.waitFrame(58355 - 60); minitouch.press("似似花") #连点 lframe 5392//time 1
autopcr.waitFrame(58573 - 60); minitouch.press("暂停") #暂停

#日志：
#v3:添加了最后暂停
#v4:引入auto，修改set提前量S
