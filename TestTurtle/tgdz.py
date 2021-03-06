#####################################################################
#
# author:  sheisc@163.com
#
#####################################################################

tg = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
dz = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']


############################## 方法1: 输出一个甲子的60个年份  #################################################
# k = 0
# i = 0
# j = 0
# len_tg = len(tg)
# len_dz = len(dz)
# while not (i == len_tg and j == len_dz):
#     if i == len_tg:
#         i = 0
#     if j == len_dz:
#         j = 0
#     # print(tg[i] + dz[j])
#     print("{0:02d}: {1}".format(k, tg[i] + dz[j]))
#     k += 1
#     i += 1
#     j += 1

############################## 方法2: 输出一个甲子的60个年份  #################################################
# i = 0
# j = 0
# k = 0
# while k < 60:
#     i = k % len(tg)
#     j = k % len(dz)
#     #print(tg[i] + dz[j])
#     print("{0:02d}: {1}".format(k, tg[i] + dz[j]))
#     k += 1


############################## 输入公历年份, 查询对应的干支纪年 #################################################

# 已知公历1984为甲子年
JIA_ZI = 1984
# (1) 严格说来:公历年与农历年不是完全一一对应,
# (2) 不存在公元0年, 公元1年称为公元元年,
#     公元前n年, 记为输入时按-n输入, 处理时当作 -n + 1
#
year = -841


while True:
    year = int(input('Please input a year:\n'))
    if year == 0:
        break
    elif year < 0:
        year += 1

    k = 0
    if year >= JIA_ZI:
        k = year - JIA_ZI
        k %= 60
    else:
        k = JIA_ZI - year
        k %= 60
        k = (60 - k) % 60

    i = k % len(tg)
    j = k % len(dz)
    print(tg[i] + dz[j])


