# 翻译
# 整体思路：
#       1. 使用zip()将 srcstr和desstr合并组合，且zip()只组合到两个字符的相同长度；
#       2. 如果len(srcstr) > len(desstr), 则要进行截断操作——还是使用短的desstr来代替长的srcstr， 不够的使用None值代替；
#       3. 遍历string，若字符串的字符在字典的key之中，则将value值加入到列表当中；
#       4. 遍历列表，将None值剔除，输出。
def tr(srcstr, desstr, string, casemap=True):
    assert len(srcstr) >= len(desstr)

    table = dict(zip(srcstr, desstr)) # zip() 只组合到相同的长度
    if len(srcstr) > len(desstr):  # src = abcdef, des = mno, string = abcdefghi, print = mnoghi
        temp = {}.fromkeys(srcstr[len(desstr):]) # srcstr的全部字符长度
        table.update(temp)
        print(table) # {'e': None, 'd': None, 'B': 'n', 'c': 'o', 'f': None, 'a': 'm'}

    ls = []
    for ch in string:
        if not casemap:
            if ch.lower() in table:
                ls.append(table[ch.lower()])
            elif ch.upper() in table:
                ls.append(table[ch.upper()])
            else:
                ls.append(ch)
            continue

        if ch in table:
            ls.append(table[ch])
        else:
            ls.append(ch)


    ls = [ch for ch in ls if ch] # 剔除截断时使用的字典中的None值
    return ''.join(ls)

print(tr('abc', 'mno', 'abcdef'))
print(tr('aBcdef', 'mno', 'abcdefghi', False))

# li = list('abcd')
# print(li[3:])