'''
列表的元素可以改动，但是元组的数据不可改变。
如果元组里面只有一个元素，则元素后面一定有都逗号，
break :终止循环，直接结束循环代码的执行
# continue： 循环到continue后的代码不在执行，将直接重新执行新的代码
字典：可以用来储存多个数据，其中储存的每个数据都包括key和value，可以通过key取到对应的值，
字典

# 列表：python中用来储存一组数据的类型，其中储存的每一个数据都成为‘元素’
# 定义：列表变量名 = [数据1，数据2，数据3，...]
# 访问：列表变量名[位置标号]列表中的元素的位置编号从左边0开始，右边是从-1开始位置编号也称为索引或者下标
#for循环中的else和while中的else一样,当循环中没有遇到break时，循环结束时会执行else中的代码

'''

# name_list = [1,2,3,4,5,6,7,8]
# name_list1 = (1,2,3,4,5,6,7,8)
# print(type(name_list1))
# print(type(name_list), name_list)
# print(name_list[1])
# print(name_list[-1])

# while的循环语句
# 计算1到100 的累加和
# i =2
# sum =0

# while i <= 100:
#     print(i)
#     sum = sum + i
#     # print(sum)
#     i += 1
# print(sum)

# while i <= 100:
#     print(i)
#     sum = sum + i
#     i += 2
# print(sum)
# print(sum * 2)


# 循环跑步
# i = 1
# while i <= 5:
#     print('跑步%d圈'% i)
#     a = 1
#     while a <= 10:
#         print('做%d个俯卧撑' % a)
#         a += 1
#     i = i + 1

#     # print('做十个俯卧撑')
#     # i += 1


# import signal

# def signal_handler(signal, frame):
#     print('程序终止')
#     sys.exit(0)

# signal.signal(signal.SIGINT, signal_handler)

# while True:
#     print('跑步一圈')


# 输出一个字符串
# print("Hello, world!")

# # 输出两个数值，并使用分隔符分隔它们
# x = 3
# y = 4
# print(x, y, sep=' - ')

# # 输出多个值，以空格作为分隔符，不使用换行符
# print("apple", "banana", "cherry", end=' ')
# print("date", "elderberry")

# print 打印内容到文件里面
# with open('output.txt', 'w') as f:
#     print("This is a test.", file=f)
# name_list = [1,2,3,4,5,6,7,8,9,0]
# name_list.append(22)
# name_list.remove(2)

# name_list[2] = 222

# print(len(name_list))

# print(6 in name_list)



# print(name_list)


# my_dict = {'age':'12','name':'song','city':'sh'}
# # my_dict['qq'] = 'aa'
# # city = my_dict.pop('city')
# # print(city)
# # my_dict['city'] = 'sh'

# user_list = ['1','2']
# print(type(user_list),user_list)

# # print(my_dict)
# for key in my_dict:
#     user_list.append(key)   
# print(type(user_list),user_list)
# user_list.append('edc')
# print(user_list)
# for value in my_dict.values():
    # print(value)

# for key,value in my_dict.items():
    # print(key,value)
 
def main(dividend:int,divisor:int):
    tag1 = dividend
    tag2 =divisor 
    if dividend<0:
        dividend = -dividend
    if divisor<0:
        divisor = -divisor
    num = 0
    while dividend>=divisor:
        num+=1
        dividend = dividend - divisor
    if (tag1>0 and tag2<0) or (tag1<0 and tag2>0):
        num = -num
    return num
print(main(-10,-5))
        
class Solution(object):

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # 考虑被除数为最小值的情况
        if dividend == INT_MIN:
            if divisor == 1:
                return INT_MIN
            if divisor == -1:
                return INT_MAX
        
        # 考虑除数为最小值的情况
        if divisor == INT_MIN:
            return 1 if dividend == INT_MIN else 0
        # 考虑被除数为 0 的情况
        if dividend == 0:
            return 0
        
        # 一般情况，使用二分查找
        # 将所有的正数取相反数，这样就只需要考虑一种情况
        rev = False
        if dividend > 0:
            dividend = -dividend
            rev = not rev
        if divisor > 0:
            divisor = -divisor
            rev = not rev

        def quickAdd(y: int, z: int, x: int):
            # x 和 y 是负数，z 是正数
            # 需要判断 z * y >= x 是否成立
            result, add = 0, y
            while z > 0:
                if (z & 1) == 1:
                    # 需要保证 result + add >= x
                    if result < x - add:
                        return False
                    result += add
                if z != 1:
                    # 需要保证 add + add >= x
                    if add < x - add:
                        return False
                    add += add
                # 不能使用除法
                z >>= 1
            return True
        

        left, right, ans = 1, INT_MAX, 0
        while left <= right:
            # 注意溢出，并且不能使用除法
            mid = left + ((right - left) >> 1)
            check = quickAdd(divisor, mid, dividend)
            if check:
                ans = mid
                # 注意溢出
                if mid == INT_MAX:
                    break
                left = mid + 1
            else:
                right = mid - 1

        return -ans if rev else ans

