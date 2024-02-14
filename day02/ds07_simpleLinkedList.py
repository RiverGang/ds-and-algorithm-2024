# file: ds07_simpleLinkedList.py
# desc: 단순연결리스트 일반 구현

memory = [] # 컴퓨터에 메모리를 모방
# head, curr, prev 일반 변수
head, curr, prev = None, None, None

class Node():
    # data, link 두개의 멤버변수 존재
    # 생성자 추가
    def __init__(self, name) -> None:
        self.data = name
        self.link = None
# 클래스 끝


def printNodes(start):
    curr = start
    if curr == None: return # 함수를 빠져나감
    
    print(curr.data, end=' -> ')
    while curr.link != None:
        curr = curr.link # 내 노드 다음의 노드가 current가 됨
        print(curr.data, end=' -> ')
    print()

dataArray = ['다현', '정연', '쯔위', '사나', '지효']

# 메인시작

if __name__ == '__main__':
    node = Node(dataArray[0]) # '다현' 데이터 담은 노드 생성
    head = node # 첫번째 값을 head가 가리킴
    memory.append(node) #가짜 메모리에 집어넣음

    for data in dataArray[1:]: # 두번째 노드부터 끝까지
        prev = node
        node = Node(data) # 정연
        prev.link = node       
        memory.append(node)

    printNodes(head)
