# 家庭理财

import pickle
# 1.用户管理
user = input('please input a username:')
user_file = pickle.load(open('user.txt', 'rb'))
user_info = {}
if user not in user_file:
    print('username is wrong, please input again.')
else:
    user_info[user] = user_file[user]

# 2. 操作界面
def ui():
    print('Welcome ', user, '; Total Money:', user_file[user])
    print('####### user interface  #######')
    print('1. 存款')
    print('2. 取款')
    print('3. 借款')
    print('4. 贷款')
    print('e. 退出')

def save():
    print('welcome to save money, "q" for back')
    money = float(input('please input the money than you will save:'))
    print('you save ', money, 'money, and you will have ', user_info[user] + money)
    user_info[user] += money
    user_file.update(user_info)
    pickle.dump(user_file, open('user.txt', 'wb'))


def take():
    print('welcome to take money, "q" for back')

def borror():
    print('welcome to borror money, "q" for back')

def loan():
    print('welcome to loan money, "q" for back')

while True:
    ui()
    option = input('please input an option number:')
    if option == 'e':
        exit(0)
    elif option == '1':
        save()
    elif option == '2':
        take()
    elif option == '3':
        borror()
    elif option == '4':
        loan()
    else:
        continue



# s1 = {'yyang':1000.00, 'yyang2':2000.00}
# pickle.dump(s1, open('user.txt', 'wb'))
#
# s2 = pickle.load(open('user.txt', 'rb'))
# print(type(s2))
# i = 'yyang'
# if i in s2:
#     print(i, s2[i])