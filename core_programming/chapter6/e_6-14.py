import random

guess_list = ['剪刀', '石头', '布']
guize = [['布', '石头'], ['石头', '剪刀'], ['剪刀', '布',]]

while True:
    computer = random.choice(guess_list)
    people = input('请输入：剪刀、石头、布：')

    if people not in guess_list:
        people = input('请重新输入：剪刀、石头、布：')
        continue

    print('电脑出：', computer)
    if computer == people:
        print('平')
    elif [computer, people] in guize:
        print('电脑胜')
    else:
        print('人胜')
