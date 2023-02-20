'''
%s：表示给任意类型数据占位(表示是一个空，可以被任意类型数据填上)
%d：表示给整数占位(表示是一个空，可以被整数填上)
%f：表示给小数占位(表示是一个空，可以被小数填上)
input函数接受的是由键盘出入的内容，并且input接收的数据，都是str字符串类型。
'''
# name = 'son                                                                                        g'
# age = 22
# weight = 178.3
# print('我的体重为%08f,年龄为%d，名字叫%s' % (weight, age, name))
# hub = (input("请输入你的电话号码："))
# print(type(hub))
# 买苹果
# 先输入苹果的斤数和价格
# price = int(input('请输入苹果的单价：'))
# weight = float(input('请输入苹果的斤数:'))
# # print(price)
# # print(weight)
# allprice = float(price * weight)
# print('你好一共%.2f元' % (allprice))

# num1 = 10
# num2 = 20
# print(num1 == num2)

# age = int(input('请输入你的年龄：'))
# if age >= 18:
#     print('可以上网吧喽')
# else:
#     print('回家写作业去')

# 车票安检
# ticker1 = bool(input('chepiao:'))
# print(ticker1)

# a = 1
# # a1 = 11
# b = 0
# print(bool(a))
# print(bool(b))
# # print(bool(a1))
# print(a)

# # knf_length = int(input('你的knf_length是多长的:'))
# # knf_length = int(input('nidedaochangdu:'))
# ticker2 = False
# if ticker:
#     # print('过安检')
#     knf_length = int(input('nidedaochangdu:'))

#     if knf_length > 12:
#         print('不能带上车')
#     else:
#         print('安检通过')
# else:
#     print('请先买票')

# 猜拳
# user = int(input('石头1,剪刀2,布3:'))
# # computer = 1
# import random
# computer = random.randint(1,3)
# print('电脑出%d' % computer)
# if (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
#     print('yonghuying')
# else:
#     print('diannao ying')

# 三目运算符
# a = 10
# b = 20
# max = a if a > b else b
# print(max)


# while 循环
# while True:
#     print('跑步一圈')



# import random
# a = random.randint(3,9)
# print(a)

# x = random.random()
# print(x)
# numbers = [1, 2, 3, 4, 5]
# random.shuffle(numbers)
# print(numbers)

# 设置随机数种子
# random.seed(1234)

# 生成一个 [0, 1) 范围内的随机浮点数
# x = random.random()
# print(x)


# 循环
# i = 1
# while i < 10:
#     print('跑步%d' % i)
#     i += 1
