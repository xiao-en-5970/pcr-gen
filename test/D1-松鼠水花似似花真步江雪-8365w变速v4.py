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
minitouch.setPos("似似花", int(max_x * 0.5), int(max_y * 0.8))
print("真步 定位中")
minitouch.setPos("真步", int(max_x * 0.38), int(max_y * 0.8))
print("江雪 定位中")
minitouch.setPos("江雪", int(max_x * 0.26), int(max_y * 0.8))
print("解除暂停，塔塔开!")

autopcr.setOffset(2, 0); # offset calibration
autopcr.waitFrame(autopcr.getFrame() + 50); minitouch.press("SPEED") #加速
autopcr.waitFrame(1098 - 60); minitouch.press("SPEED") #减速 lframe 1098
autopcr.waitFrame(1098); minitouch.press("松鼠") # lframe 1098
autopcr.waitFrame(1098 + 30); minitouch.press("SPEED") #加速 lframe 1098
autopcr.waitFrame(1480 - 45); minitouch.press("松鼠") #连点 lframe 1192
autopcr.waitFrame(1783 - 45); minitouch.press("真步") #连点 lframe 1207
autopcr.waitFrame(2295 - 45); minitouch.press("水花") #连点 lframe 1329
autopcr.waitFrame(2627 - 60); minitouch.press("SPEED") #减速 lframe 1402
autopcr.waitFrame(2627); minitouch.press("江雪") # lframe 1402
autopcr.waitFrame(2627 + 30); minitouch.press("SPEED") #加速 lframe 1402
autopcr.waitFrame(2942 - 45); minitouch.press("松鼠") #连点 lframe 1441
autopcr.waitFrame(3259 - 60); minitouch.press("SPEED") #减速 lframe 1470
autopcr.waitFrame(3259); minitouch.press("似似花") # lframe 1470
autopcr.waitFrame(3259 + 30); minitouch.press("SPEED") #加速 lframe 1470
autopcr.waitFrame(3505 - 45); minitouch.press("松鼠") #连点 lframe 1505
#BOSS  UB
autopcr.waitFrame(4341 - 45); minitouch.press("真步") #连点 lframe 1573
autopcr.waitFrame(4774 - 45); minitouch.press("水花") #连点 lframe 1616
autopcr.waitFrame(5190 - 60); minitouch.press("SPEED") #减速 lframe 1773
autopcr.waitFrame(5190 ); minitouch.press("江雪") # lframe 1773
autopcr.waitFrame(5190 + 30); minitouch.press("SPEED") #加速 lframe 1773
autopcr.waitFrame(5466 - 45); minitouch.press("松鼠") #连点 lframe 1773
autopcr.waitFrame(5847 - 60); minitouch.press("SPEED") #减速 lframe 1866
autopcr.waitFrame(5847); minitouch.press("似似花") # lframe 1866
autopcr.waitFrame(5847 + 30); minitouch.press("SPEED") #加速 lframe 1866
autopcr.waitFrame(6058 - 45); minitouch.press("真步") #连点 lframe 1866
autopcr.waitFrame(6448 - 45); minitouch.press("水花") #连点 lframe 1866
autopcr.waitFrame(6750 - 45); minitouch.press("松鼠") #连点 lframe 1909
autopcr.waitFrame(7112 - 45); minitouch.press("似似花") #连点 lframe 1983
autopcr.waitFrame(7362 - 45); minitouch.press("松鼠") #连点 lframe 2022
autopcr.waitFrame(7650 - 45); minitouch.press("江雪") #连点 lframe 2022
autopcr.waitFrame(8028 - 45); minitouch.press("真步") #连点 lframe 2124
autopcr.waitFrame(8418 - 45); minitouch.press("水花") #连点 lframe 2124
autopcr.waitFrame(8747 - 45); minitouch.press("似似花") #连点 lframe 2194
autopcr.waitFrame(8965 - 45); minitouch.press("江雪") #连点 lframe 2201
#BOSS  UB
autopcr.waitFrame(9762 - 45); minitouch.press("松鼠") #连点 lframe 2242
autopcr.waitFrame(10173 - 45); minitouch.press("水花") #连点 lframe 2365
autopcr.waitFrame(10432 - 45); minitouch.press("真步") #连点 lframe 2365
autopcr.waitFrame(10834 - 45); minitouch.press("松鼠") #连点 lframe 2377
autopcr.waitFrame(11122 - 45); minitouch.press("似似花") #连点 lframe 2377
autopcr.waitFrame(11333 - 45); minitouch.press("江雪") #连点 lframe 2377
autopcr.waitFrame(11676 - 45); minitouch.press("水花") #连点 lframe 2444
autopcr.waitFrame(11941 - 45); minitouch.press("松鼠") #连点 lframe 2450
autopcr.waitFrame(12265 - 45); minitouch.press("真步") #连点 lframe 2486
autopcr.waitFrame(12655 - 45); minitouch.press("似似花") #连点 lframe 2486
autopcr.waitFrame(12866 - 45); minitouch.press("江雪") #连点 lframe 2486
autopcr.waitFrame(13179 - 45); minitouch.press("水花") #连点 lframe 2523
autopcr.waitFrame(13495 - 45); minitouch.press("真步") #连点 lframe 2580
autopcr.waitFrame(13885 - 45); minitouch.press("松鼠") #连点 lframe 2580
autopcr.waitFrame(14234 - 45); minitouch.press("似似花") #连点 lframe 2641
autopcr.waitFrame(14445 - 45); minitouch.press("江雪") #连点 lframe 2641
autopcr.waitFrame(14802 - 45); minitouch.press("AUTO") #AUTO开 lframe 2722
#AUTO
autopcr.waitFrame(14802 + 10); minitouch.press("AUTO") #AUTO关 lframe 2722
autopcr.waitFrame(15068 - 45); minitouch.press("松鼠") #连点 lframe 2729
autopcr.waitFrame(15362 - 45); minitouch.press("真步") #连点 lframe 2735
autopcr.waitFrame(15752 - 45); minitouch.press("江雪") #连点 lframe 2735
autopcr.waitFrame(16057 - 45); minitouch.press("水花") #连点 lframe 2764
autopcr.waitFrame(16316 - 45); minitouch.press("似似花") #连点 lframe 2764
autopcr.waitFrame(16559 - 45); minitouch.press("真步") #连点 lframe 2796
autopcr.waitFrame(16949 - 45); minitouch.press("松鼠") #连点 lframe 2796
autopcr.waitFrame(17252 - 45); minitouch.press("江雪") #连点 lframe 2811
autopcr.waitFrame(17557 - 45); minitouch.press("似似花") #连点 lframe 2840
autopcr.waitFrame(17771 - 45); minitouch.press("水花") #连点 lframe 2843
autopcr.waitFrame(18072 - 45); minitouch.press("真步") #连点 lframe 2885
autopcr.waitFrame(18468 - 45); minitouch.press("似似花") #连点 lframe 2891
autopcr.waitFrame(18679 - 45); minitouch.press("江雪") #连点 lframe 2891
autopcr.waitFrame(18977 - 45); minitouch.press("松鼠") #连点 lframe 2913
autopcr.waitFrame(19274 - 45); minitouch.press("水花") #连点 lframe 2922
autopcr.waitFrame(19579 - 45); minitouch.press("真步") #连点 lframe 2968
autopcr.waitFrame(19969 - 45); minitouch.press("水花") #连点 lframe 2968
autopcr.waitFrame(20264 - 60); minitouch.press("SPEED") #减速 lframe 3004
autopcr.waitFrame(20264); minitouch.press("似似花") # lframe 3004
autopcr.waitFrame(20264 + 30); minitouch.press("SPEED") #加速 lframe 3004
autopcr.waitFrame(20511 - 45); minitouch.press("松鼠") #连点 lframe 3040
autopcr.waitFrame(20799 - 45); minitouch.press("江雪") #连点 lframe 3040
autopcr.waitFrame(21092 - 45); minitouch.press("真步") #连点 lframe 3057
autopcr.waitFrame(21482 - 45); minitouch.press("水花") #连点 lframe 3057
autopcr.waitFrame(21764 - 45); minitouch.press("似似花") #连点 lframe 3080
autopcr.waitFrame(22023 - 45); minitouch.press("水花") #连点 lframe 3128
autopcr.waitFrame(22282 - 45); minitouch.press("江雪") #连点 lframe 3128
autopcr.waitFrame(22576 - 45); minitouch.press("真步") #连点 lframe 3146
autopcr.waitFrame(22966 - 45); minitouch.press("松鼠") #连点 lframe 3146
autopcr.waitFrame(23254 - 45); minitouch.press("水花") #连点 lframe 3146
autopcr.waitFrame(23529 - 45); minitouch.press("似似花") #连点 lframe 3162
autopcr.waitFrame(23785 - 45); minitouch.press("江雪") #连点 lframe 3207
#BOSS  UB
autopcr.waitFrame(24563 - 45); minitouch.press("真步") #连点 lframe 3229
autopcr.waitFrame(24953 - 45); minitouch.press("水花") #连点 lframe 3229
autopcr.waitFrame(25267 - 45); minitouch.press("似似花") #连点 lframe 3284
autopcr.waitFrame(25512 - 45); minitouch.press("真步") #连点 lframe 3318
autopcr.waitFrame(25902 - 45); minitouch.press("松鼠") #连点 lframe 3318
autopcr.waitFrame(26190 - 45); minitouch.press("江雪") #连点 lframe 3318
autopcr.waitFrame(26527 - 45); minitouch.press("似似花") #连点 lframe 3379
autopcr.waitFrame(26740 - 60); minitouch.press("SPEED") #减速 lframe 3381
autopcr.waitFrame(26740); minitouch.press("水花") # lframe 3381
autopcr.waitFrame(26740 + 30); minitouch.press("SPEED") #加速 lframe 3381
autopcr.waitFrame(27025 - 45); minitouch.press("真步") #连点 lframe 3407
autopcr.waitFrame(27431 - 45); minitouch.press("水花") #连点 lframe 3423
autopcr.waitFrame(27735 - 45); minitouch.press("似似花") #连点 lframe 3468
autopcr.waitFrame(27957 - 45); minitouch.press("AUTO") #AUTO开 lframe 3479
#AUTO
autopcr.waitFrame(27957 + 10); minitouch.press("AUTO") #AUTO关 lframe 3479
autopcr.waitFrame(28233 - 45); minitouch.press("真步") #连点 lframe 3479
autopcr.waitFrame(28646 - 45); minitouch.press("水花") #连点 lframe 3502
autopcr.waitFrame(28970 - 45); minitouch.press("水花") #连点 lframe 3567
autopcr.waitFrame(29229 - 45); minitouch.press("松鼠") #连点 lframe 3567
autopcr.waitFrame(29517 - 45); minitouch.press("江雪") #连点 lframe 3567
autopcr.waitFrame(29794 - 45); minitouch.press("真步") #连点 lframe 3568
autopcr.waitFrame(30199 - 45); minitouch.press("水花") #连点 lframe 3583
autopcr.waitFrame(30458 - 45); minitouch.press("似似花") #连点 lframe 3583
autopcr.waitFrame(30737 - 45); minitouch.press("真步") #连点 lframe 3651
autopcr.waitFrame(31127 - 45); minitouch.press("松鼠") #连点 lframe 3651
autopcr.waitFrame(31415 - 45); minitouch.press("水花") #连点 lframe 3651
autopcr.waitFrame(31708 - 45); minitouch.press("似似花") #连点 lframe 3685
autopcr.waitFrame(31962 - 45); minitouch.press("AUTO") #AUTO开 lframe 3728
#AUTO
autopcr.waitFrame(31962 + 10); minitouch.press("AUTO") #AUTO关 lframe 3728
autopcr.waitFrame(32250 - 45); minitouch.press("真步") #连点 lframe 3740
autopcr.waitFrame(32640 - 45); minitouch.press("水花") #连点 lframe 3740
autopcr.waitFrame(32960 - 45); minitouch.press("似似花") #连点 lframe 3801
autopcr.waitFrame(33186 - 45); minitouch.press("水花") #连点 lframe 3816
autopcr.waitFrame(33445 - 45); minitouch.press("江雪") #连点 lframe 3816
autopcr.waitFrame(33734 - 45); minitouch.press("真步") #连点 lframe 3829
autopcr.waitFrame(34124 - 45); minitouch.press("松鼠") #连点 lframe 3829
autopcr.waitFrame(34412 - 45); minitouch.press("水花") #连点 lframe 3829
autopcr.waitFrame(34732 - 45); minitouch.press("似似花") #连点 lframe 3890
autopcr.waitFrame(34945 - 45); minitouch.press("江雪") #连点 lframe 3892
autopcr.waitFrame(35241 - 45); minitouch.press("真步") #连点 lframe 3912
autopcr.waitFrame(35631 - 45); minitouch.press("水花") #连点 lframe 3912
autopcr.waitFrame(35968 - 45); minitouch.press("似似花") #连点 lframe 3990
autopcr.waitFrame(36183 - 45); minitouch.press("松鼠") #连点 lframe 3994
autopcr.waitFrame(36478 - 45); minitouch.press("真步") #连点 lframe 4001
autopcr.waitFrame(36868 - 45); minitouch.press("江雪") #连点 lframe 4001
autopcr.waitFrame(37207 - 60); minitouch.press("SPEED") #减速 lframe 4064
autopcr.waitFrame(37207); minitouch.press("水花") # lframe 4064
autopcr.waitFrame(37207 + 30); minitouch.press("SPEED") #加速 lframe 4064
autopcr.waitFrame(37492 - 45); minitouch.press("真步") #连点 lframe 4090
autopcr.waitFrame(37882 - 45); minitouch.press("松鼠") #连点 lframe 4090
autopcr.waitFrame(38186 - 45); minitouch.press("水花") #连点 lframe 4106
autopcr.waitFrame(38445 - 45); minitouch.press("似似花") #连点 lframe 4106
autopcr.waitFrame(38712 - 45); minitouch.press("AUTO") #AUTO开 lframe 4162
#AUTO
autopcr.waitFrame(38712 + 10); minitouch.press("AUTO") #AUTO关 lframe 4162
autopcr.waitFrame(38988 - 45); minitouch.press("真步") #连点 lframe 4162
autopcr.waitFrame(39401 - 45); minitouch.press("水花") #连点 lframe 4185
autopcr.waitFrame(39725 - 45); minitouch.press("水花") #连点 lframe 4250
autopcr.waitFrame(39984 - 45); minitouch.press("似似花") #连点 lframe 4250
autopcr.waitFrame(40195 - 45); minitouch.press("江雪") #连点 lframe 4250
autopcr.waitFrame(40472 - 45); minitouch.press("真步") #连点 lframe 4251
autopcr.waitFrame(40862 - 45); minitouch.press("松鼠") #连点 lframe 4251
autopcr.waitFrame(41165 - 45); minitouch.press("水花") #连点 lframe 4266
autopcr.waitFrame(41484 - 45); minitouch.press("江雪") #连点 lframe 4326
autopcr.waitFrame(41768 - 45); minitouch.press("真步") #连点 lframe 4334
autopcr.waitFrame(42158 - 45); minitouch.press("似似花") #连点 lframe 4334
autopcr.waitFrame(42369 - 45); minitouch.press("水花") #连点 lframe 4334
autopcr.waitFrame(42689 - 45); minitouch.press("江雪") #连点 lframe 4395
autopcr.waitFrame(42993 - 45); minitouch.press("真步") #连点 lframe 4423
autopcr.waitFrame(43383 - 45); minitouch.press("松鼠") #连点 lframe 4423
autopcr.waitFrame(43671 - 45); minitouch.press("水花") #连点 lframe 4423
autopcr.waitFrame(43954 - 60); minitouch.press("SPEED") #减速 lframe 4447
autopcr.waitFrame(43954); minitouch.press("似似花") # lframe 4447
autopcr.waitFrame(44208); minitouch.press("江雪") # lframe 4490
autopcr.waitFrame(44208 + 30); minitouch.press("SPEED") #加速 lframe 4490
autopcr.waitFrame(44506 - 45); minitouch.press("真步") #连点 lframe 4512
autopcr.waitFrame(44896 - 45); minitouch.press("水花") #连点 lframe 4512
autopcr.waitFrame(45194 - 45); minitouch.press("似似花") #连点 lframe 4551
autopcr.waitFrame(45432 - 45); minitouch.press("水花") #连点 lframe 4578
autopcr.waitFrame(45691 - 45); minitouch.press("江雪") #连点 lframe 4578
autopcr.waitFrame(45984 - 45); minitouch.press("真步") #连点 lframe 4595
autopcr.waitFrame(46374 - 45); minitouch.press("松鼠") #连点 lframe 4595
autopcr.waitFrame(46662 - 45); minitouch.press("水花") #连点 lframe 4595
autopcr.waitFrame(46982 - 45); minitouch.press("似似花") #连点 lframe 4656
autopcr.waitFrame(47221 - 45); minitouch.press("真步") #连点 lframe 4684
#BOSS  UB
autopcr.waitFrame(48169 - 45); minitouch.press("水花") #连点 lframe 4762
autopcr.waitFrame(48439 - 45); minitouch.press("真步") #连点 lframe 4773
autopcr.waitFrame(48829 - 45); minitouch.press("松鼠") #连点 lframe 4773
autopcr.waitFrame(49117 - 45); minitouch.press("似似花") #连点 lframe 4773
autopcr.waitFrame(49359 - 45); minitouch.press("水花") #连点 lframe 4804
autopcr.waitFrame(49641 - 45); minitouch.press("水花") #连点 lframe 4827
autopcr.waitFrame(49900 - 45); minitouch.press("江雪") #连点 lframe 4827
autopcr.waitFrame(50183 - 45); minitouch.press("真步") #连点 lframe 4834
autopcr.waitFrame(50588 - 45); minitouch.press("似似花") #连点 lframe 4849
autopcr.waitFrame(50835 - 45); minitouch.press("水花") #连点 lframe 4885
autopcr.waitFrame(51112 - 45); minitouch.press("江雪") #连点 lframe 4903
autopcr.waitFrame(51408 - 45); minitouch.press("真步") #连点 lframe 4923
autopcr.waitFrame(51798 - 45); minitouch.press("松鼠") #连点 lframe 4923
autopcr.waitFrame(52127 - 45); minitouch.press("水花") #连点 lframe 4964
autopcr.waitFrame(52386 - 45); minitouch.press("似似花") #连点 lframe 4964
autopcr.waitFrame(52639 - 45); minitouch.press("真步") #连点 lframe 5006
autopcr.waitFrame(53029 - 45); minitouch.press("江雪") #连点 lframe 5006
autopcr.waitFrame(53305 - 45); minitouch.press("水花") #连点 lframe 5006
autopcr.waitFrame(53609 - 45); minitouch.press("似似花") #连点 lframe 5051
autopcr.waitFrame(53864 - 45); minitouch.press("真步") #连点 lframe 5095
autopcr.waitFrame(54254 - 45); minitouch.press("松鼠") #连点 lframe 5095
autopcr.waitFrame(54542 - 45); minitouch.press("水花") #连点 lframe 5095
autopcr.waitFrame(54873 - 45); minitouch.press("AUTO") #AUTO开 lframe 5167
#AUTO
autopcr.waitFrame(54873 + 10); minitouch.press("AUTO") #AUTO关 lframe 5167
autopcr.waitFrame(55166 - 45); minitouch.press("真步") #连点 lframe 5184
autopcr.waitFrame(55556 - 45); minitouch.press("水花") #连点 lframe 5184
autopcr.waitFrame(55886 - 45); minitouch.press("水花") #连点 lframe 5255
autopcr.waitFrame(56145 - 45); minitouch.press("似似花") #连点 lframe 5255
autopcr.waitFrame(56356 - 45); minitouch.press("江雪") #连点 lframe 5255
autopcr.waitFrame(56643 - 45); minitouch.press("松鼠") #连点 lframe 5266
autopcr.waitFrame(56932 - 45); minitouch.press("真步") #连点 lframe 5267
autopcr.waitFrame(57405 - 45); minitouch.press("AUTO") #AUTO开 lframe 5350
#AUTO
autopcr.waitFrame(57405 + 10); minitouch.press("AUTO") #AUTO关 lframe 5350
autopcr.waitFrame(57670 - 45); minitouch.press("真步") #连点 lframe 5356
autopcr.waitFrame(58096 - 45); minitouch.press("水花") #连点 lframe 5392
autopcr.waitFrame(58355 - 45); minitouch.press("似似花") #连点 lframe 5392
autopcr.waitFrame(58573 - 60); minitouch.press("暂停") #暂停

#日志：
#v3:添加了最后暂停
#v4:引入auto，修改set提前量S
