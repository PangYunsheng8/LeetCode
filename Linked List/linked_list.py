class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class SingleLinkList(object):
    def __init__(self, node=None):
         self.__head = node

    # 判断链表是否为空
    def is_empty(self):
        return self.__head == None
    
    # 返回链表长度
    def length(self):
        count = 0
        cur = self.__head
        while cur != None:
            count += 1
            cur = cur.next
        return count

    # 遍历链表
    def travel(self):
        cur = self.__head
        str_list = ""
        while cur != None:
            str_list += str(cur.val) + " "
            cur = cur.next
        print(str_list)

    # 在链表头部添加元素
    def add(self, item):
        node = ListNode(item)
        node.next = self.__head
        self.__head = node

    # 在链表尾部添加元素
    def append(self, item):
        node = ListNode(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    # 在指定位置添加元素
    def insert(self, item, pos):
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            cur = self.__head
            cur_pos = 0
            node = ListNode(item)
            while cur_pos < pos:
                cur = cur.next
                cur_pos += 1
            temp = cur.next
            cur.next = node
            node.next = temp

    # 按值删除结点
    def remove(self, item):
        cur = self.__head
        pre = None
        while cur != None:
            if cur.val == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    # 从链表尾部删除第n个结点
    def remove_nth_from_end(self, n):
        reveser_n = self.length() - n
        cur = self.__head
        cur_pos = 0
        pre = None
        while cur_pos < reveser_n:
            pre = cur
            cur = cur.next
            cur_pos += 1
        pre.next = cur.next


if __name__ == "__main__":
    link_list = SingleLinkList()
    print(link_list.is_empty())
    print(link_list.length())
    print("-----------------------------------")

    link_list.append(1)
    link_list.append(2)
    link_list.append(5)
    link_list.append(3)
    link_list.travel()
    print(link_list.is_empty())
    print(link_list.length())
    print("-----------------------------------")

    link_list.add(4)
    link_list.travel()
    print("-----------------------------------")

    link_list.insert(10, -3)
    link_list.travel()
    link_list.insert(11, 8)
    link_list.travel()
    link_list.insert(12, 5)
    link_list.travel()
    link_list.insert(0, 2)
    link_list.travel()
    print("-----------------------------------")

    link_list.remove(5)
    link_list.travel()  
    print("-----------------------------------")

    link_list.remove_nth_from_end(5)
    link_list.travel()  
