# 题目：创建一个链表。

""" solution 1 """
print('solution 1: ')

if __name__ == '__main__':
    ptr = []  # 创建一个空的列表，用来模拟链表
    for i in range(5):
        num = int(input('Please input a number: '))  # 使用 input() 接收输入
        ptr.append(num)  # 将输入的数字添加到列表（模拟链表节点的添加）
    
    print(ptr)  # 打印链表（这里打印的是列表）



""" solution 2 """
print('solution 2: ')

class Node:
    def __init__(self, data):
        self.data = data  # 存储数据
        self.next = None  # 指向下一个节点

class LinkedList:
    def __init__(self):
        self.head = None  # 初始化时链表为空

    # 插入新节点到链表末尾
    def append(self, data):
        new_node = Node(data)  # 创建新节点
        if not self.head:  # 如果链表为空
            self.head = new_node  # 将新节点设置为头节点
            return
        last = self.head
        while last.next:  # 遍历链表，找到最后一个节点
            last = last.next
        last.next = new_node  # 将新节点添加到链表末尾

    # 打印链表内容
    def print_list(self):
        current = self.head
        while current:  # 遍历链表
            print(current.data, end=" -> ")  # 打印当前节点的数据
            current = current.next
        print("None")  # 最后输出 None，表示链表的结束

if __name__ == '__main__':
    linked_list = LinkedList()  # 创建一个链表实例

    # 输入 5 个数字并将其插入链表
    for i in range(5):
        num = int(input('Please input a number: '))
        linked_list.append(num)  # 将输入的数字添加到链表中

    # 打印链表
    linked_list.print_list()  # 输出链表内容
