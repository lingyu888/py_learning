# 题目：反向输出一个链表。


""" solution 1 """
print('solution 1: ')

if __name__ == '__main__':
    ptr = []  # 创建一个空的列表，用来模拟链表

    for i in range(5):
        num = int(input('Please input a number: '))  # 使用 input() 接收输入
        ptr.append(num)  # 将输入的数字添加到列表（模拟链表节点的添加）
    
    print(ptr)  # 打印链表（这里打印的是列表）

    ptr.reverse()
    print(ptr)


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

    # 反转链表
    def reverse(self):
        # 创建一个新的链表
        prev = None  # 初始化前一个节点为空
        # 逐渐从旧链表中把 Node 搬到新链表头部
        current = self.head  # 旧链表中当前节点为头节点

        while current:  # 遍历链表，直到最后一个节点
            # 旧链表的头部，逐渐向后移动
            next_node = current.next  # 保存当前节点的下一个节点
            # current 从旧链表的头变成新链表的头，同时把 旧链表的数据链接在了新链表的前面
            current.next = prev  # 反转当前节点的 next 指针
            # 新链表真正的头往前移，替代 current 的位置
            prev = current  # 移动 prev 到当前节点
            # current 重新回到旧链表的头上，同时往后移动一下
            current = next_node  # 移动 current 到下一个节点
        
        # 舍弃旧链表，直接定义为新链表的头
        self.head = prev  # 最后，prev 会指向新的头节点
        
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

    # 反转链表
    linked_list.reverse()
    print("Reversed list:")
    linked_list.print_list()  # 打印反转后的链表