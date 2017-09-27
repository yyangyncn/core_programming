# 5-4 Is a Leap Year?
# def IsLeapYear(year):
#     if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:  # 先算 and, 再算or
#         print('{year:.1f} year is a Leap Year!'.format(year = year))
#     else:
#         print('not a Leap year!')
#
# IsLeapYear(int(input('Input year: ')))

# 5.5 doller change to coins, doller less than $1
# doller = int(float(input('please input doller (less than 1):')) * 100)
# if(doller > 100):
#     print('the doller must less than $1.')
#     exit()
# coin_25, left = divmod(doller, 25)
# coin_10, left = divmod(left, 10)
# coin_5, coin_1 = divmod(left, 5)
# print('共能换取：', coin_25, '个25美分 + ', coin_10, '个10美分 + ', coin_5, '个5美分 + ', coin_1, '个1美分硬币')

# list.sort()  # 默认升

aString = 'Hello world'
anotherString = "Hello world"
print(aString)
print(anotherString)