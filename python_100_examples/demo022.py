# 题目：两个乒乓球队进行比赛，各出三人。
# 甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。
# a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

""" solution 1 """
# 一次找一个
print(f"solution 1: ")

team_A = ['a', 'b', 'c']
team_B = ['x', 'y', 'z']

matches = {}
for player_index in team_A:
    for player_A in team_A:
        # 一轮找一个，但是第一轮找到的可能是c，就需要嵌套两层
        # flag = 1确保是唯一解
        flag = 0
        for player_B in team_B:
            # 删除找好的 player_B
            if player_B not in matches.values():
                if player_A == 'a' and player_B != 'x':
                    flag += 1
                    y = player_B
                if player_A == 'b':
                    flag += 1
                    y = player_B
                if player_A == 'c' and (player_B != 'x' and player_B != 'z'):
                    flag += 1
                    y = player_B
        if player_A not in matches and flag == 1:
                matches[player_A] = y

for player_A, player_B in matches.items():
    print(f'{player_A} - {player_B}')

""" solution 2 """
# 一次找全
print(f"solution 2: ")

team_A = ['a', 'b', 'c']
team_B = ['x', 'y', 'z']

matches = {}
# 默认了 a, b, c 的先后循序，后续只需要在对应位置 != 
# 3 个 for 循环对应了 {z, x, y} 顺序解，因此有两个 if 来避免重复
for player_1 in team_B:
    for player_2 in team_B:
        if player_1 != player_2:
            for player_3 in team_B:
                if player_1 != player_3 and player_2 != player_3:
                    if player_1 != 'x' and player_3 != 'x' and player_3 != 'z':
                        print(f"a - {player_1}")
                        print(f"b - {player_2}")
                        print(f"c - {player_3}")

for player_A, player_B in matches.items():
    print(f'{player_A} - {player_B}')
