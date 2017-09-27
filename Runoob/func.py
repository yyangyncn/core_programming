def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)

print_welcome("ABC")
w = 4
h = 5
print(area(w, h))


def change_int(b):
    b = 10

b = 0
change_int(b)
print(b)
# 结果是 2


# 可写函数说明
def changeme( list ):
    "修改传入的列表"
    list.append([1,2,3,4]);
    print("函数内取值: ", list)
    return

# 调用changeme函数
mylist = [10,20,30];
changeme( mylist );
print ("函数外取值: ", mylist)


#可写函数说明
def printme( str , b):
    "打印任何传入的字符串"
    print (str, b)
    return

#调用printme函数
printme( str = "菜鸟教程", b = 1)