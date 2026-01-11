# 题目：找到年龄最大的人，并输出。请找出程序中有什么问题。

if __name__ == '__main__':
    person = {"li":18,"wang":50,"zhang":20,"sun":22}
    
    # 在循环开始时，m 被初始化为 'li'。这意味着在第一次迭代时，m 已经是 'li'，所以它不会被正确地更新为最大年龄的人的名字。
    # 换句话说，m 的初始值不应该是 'li'，应该根据字典的第一个元素进行初始化。
    # m = 'li'

    # 初始化 m 为字典中的第一个元素
    m = next(iter(person))  # 获取字典中的第一个键

    for key in person.keys():
        if person[m] < person[key]:
            m = key
 
    print('%s,%d' % (m,person[m]))