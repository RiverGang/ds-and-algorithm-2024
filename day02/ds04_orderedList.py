# file: ds04_orderdList.py
# desc: 선형리스트 프로그램

kakaotalk = []


# 데이터 추가 함수
def add_date(friend):
    kakaotalk.append(None) # 배열에 빈자리 생성
    size = len(kakaotalk) # 배열 전체 크기 확인
    kakaotalk[size-1] = friend


# 데이터 삽입 함수
def insert_data(pos, friend):
    if pos < 0 or pos > len(kakaotalk):
        print('데이터 삽입범위 초과')
        return # 함수 빠져나감
    
    # 정상적인 처리시작
    kakaotalk.append(None) # 빈칸 추가
    size = len(kakaotalk) # 배열의 현재 크기
    
    # 삽입 위치까지 데이터를 하나씩 뒤로 밀기
    for i in range(size-1, pos, -1): # 역순으로 맨뒤에서 부터
        kakaotalk[i] = kakaotalk[i-1]
        kakaotalk[i-1] = None

    kakaotalk[pos] = friend


# 데이터 삭제 함수    
def delete_data(pos): # 데이터 삭제는 위치 값만
    if pos < 0 or pos >= len(kakaotalk):
        print('데이터 삭제범위 초과')
        return
    
    size = len(kakaotalk)
    kakaotalk[pos] = None # 데이터 삭제
    for i in range(pos+1, size):
        kakaotalk[i-1] = kakaotalk[i] # 뒤에 값을 앞으로
        kakaotalk[i] = None

    del(kakaotalk[size-1]) # 배열의 맨 마지막값 완전히 삭제

    # 전역 변수 선언

kakaotalk = []
select = -1 # 1/추가, 2/삽입, 3/삭제, 4/종료

if __name__ == '__main__':
    while (select != 4):
        select = int(input('선택(1: 추가, 2: 삽입, 3: 삭제, 4: 종료) > '))
        
        if select == 1:
            date = input('추가 데이터 --> ')
            add_date(date)
            print(kakaotalk)
        
        elif select == 2:
            pos = int(input('삽입위치 --> '))
            data = input('추가 데이터 --> ')
            insert_data(pos, data)
            print(kakaotalk)
        
        elif select == 3:
            pos = int(input('삭제위치 --> '))
            delete_data(pos)
            print(kakaotalk)

        elif select == 4:
            exit(0) # 프로그램 완전종료 함수
        
        else:
            print('1~4 중 하나를 입력하세요')
            continue