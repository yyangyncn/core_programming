# rot13 加密
# 注意chr()和ord()函数的运用
def rot13(srcstr):
    ls1 = [chr((num + 13) % 26 + ord('a')) for num in range(26)] # 后移13位的字母表
    ls2 = [chr((num) % 26 + ord('a')) for num in range(26)]      # 原字母表

    table = dict(zip(ls2, ls1))  # rot13后的key对应的原字母表的value
    ls1 = ''.join(ls1).upper()
    ls2 = ''.join(ls2).upper()
    table.update(dict(zip(ls2, ls1)))   # 加入大写

    ls = []
    for ch in srcstr:
        if ch in table:
            ls.append(table[ch])
        else:
            ls.append(ch)
    return ''.join(ls)

srcstr = input('please input a string:')
print(rot13(srcstr))