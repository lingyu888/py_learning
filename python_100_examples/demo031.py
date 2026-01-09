# 题目：请输入星期几的第一个字母来判断一下是星期几，
# 如果第一个字母一样，则继续判断第二个字母。

maps = {
    'm' : 'Monday',
    'tu' : 'Tuesday',
    'w' : 'Wednesday',
    'th' : 'Thursday',
    'f' : 'Friday',
    'sa' : 'Saturday',
    'su' : 'Sunday'
}

def day(initial_letter):
    # 转小写
    letters = initial_letter.lower()
    length = len(letters)

    # 单字母判断
    if length >= 1:
        letter = letters[0]
        if letter == 'm' or letter == 'w' or letter == 'f':
            return maps[letter]
        elif length == 1:
            return 0
    # 双字母判断
    if length > 1:
        letter = letters[0] + letters[1]
        if letter == 'tu':  return maps[letter]
        elif letter == 'th':  return maps[letter]
        elif letter == 'sa':  return maps[letter]
        elif letter == 'su':  return maps[letter]
        else: return 0
    


initial_letter = input(f'请输入星期几的首字母：')
if day(initial_letter) == 0:
    print(f'输入的 {initial_letter} 无法判断是星期几')
else:   
    print(f'字母 {initial_letter} 开头的是 {day(initial_letter)}')