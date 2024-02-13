# file: ds07_simpleLinkedList.py
# desc: 단순연결리스트 일반 구현

memory = [] # 컴퓨터에 메모리를 모방
head, curr, prev = None, None, None

class Node():
    # data, link 두개의 멤버변수 존재
    # 생성자 추가
    def __init__(self, name) -> None:
        self.data = name
        self.link = None



def printNodes(start):
    curr = start
    print(curr.data, end=' -> ')
    while curr.link != None:
        curr = curr.link # 내 노드 다음의 노드가 current가 됨
        print(curr.data, end=' -> ')