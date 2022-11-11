class Node: # 노드 안에는 데이터(data)와 다음 칸을 나타내는 포인터(next)가 있어야 함.
    def __init__(self, data): # 매개변수 data에 입력받아
        self.data = data # self.data에 저장
        self.next = None


node = Node(3)
first_node = Node(4)
node.next = first_node

class LinkedList: # 링크드리스트에는 head node만 가지고 있으면 된다.
    def __init__(self, data):
        self.head = Node(data) # 해당 데이터를 들고 있는 노드를 생성해서 넣어 준다.

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    def print_all(self):
        print('hihihi')
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
# [3] -> [4] -> [5] -> [6] -> None

linked_list = LinkedList(3)

linked_list.append(4)
linked_list.append(5)
linked_list.print_all()