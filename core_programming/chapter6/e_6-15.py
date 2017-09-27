def datedif(date1, date2):
    '''利用datetime模块计算两个日期之间的天数，格式为YYYY-MM-DD'''
    if date1 == date2:
        return 0
    from datetime import date
    d1 = map(int, date1.split('-'))
    d2 = map(int, date2.split('-'))
    d1 = date(d1[0], d1[1], d1[2])
    d2 = date(d2[0], d2[1], d2[2])
    return (d1-d2).days

def dttoday(date1):
    '''计算date1到今天的天数， 格式为YYYY-MM-DD'''
    from datetime import date
    date2 = date.today().isoformat()
    return datedif(date1, date2)

def dtb(date1):
    '''计算生日为date1的人的下次生日还有多长时间'''
    from datetime import date
    today = date.today()
    d1 = map(int, date1.split('-'))
    d1 = date(today.year, d1[1], d1[2])
    if today > d1:
        d1 = d1.replace(year=d1.year + 1)
    return (d1-today).days