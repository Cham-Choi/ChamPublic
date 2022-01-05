class Empty(Exception):   ### 왜 선언하는지?
    pass

class ArrayQueue: ### 클래스로 잡아주는 이유는?
    DEFAULT_CAPACITY = 10    # 기본 큐 크기
    def __init__(self): # 빈 큐 생성
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY    # 데이터 관리 리스트
        self._size = 0    # 큐에 저장된 데이터의 개수
        self._front = 0    #  첫 번째 값의 인덱스 
        
    
    def __len__(self): # 큐의 길이를 반환. 
        return self._size
        
    def size(self):
        return self._size
    
    def _resize(self, n):   # 큐가 가득 찼을 때 큐를 확장.
        old = self._data   # 기존 큐는 old 로 보냄.
        self._data = [None] *n   # 새 큐를 빈 것으로 생성.
        walk = self._front   # walk는 기존 큐의 첫 번째 인덱스
        for i in range(self._size):
            self._data[i] = old[walk] 
            # 새 큐의 첫 번째 인덱스를 기존 큐의 첫 인덱스와 매칭.
            walk = (walk +1 ) % len(old)  
            # 기존 큐의 인덱스를 증가시키되, 길이를 초과하면 처음으로 돌아옴.
        self._front = 0 # 새 큐의 첫 번째 인덱스는 0으로 초기화.
        
    def empty(self):   # 큐가 비어있으면 True를 반환.
        if self._size == 0:
            return 1
        else:
            return 0    
    
    def first(self):   # front의 요소를 제거하지 않고 반환.
        if empty():
            raise Empty("Queue is empty")
        return self._data[self._front]
        
    def push(self, e):   # back에 요소를 추가.
        if self._size == len(self._data):   # 큐가 가득찼다면 큐의 크기를 두배로 늘려줌.
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)   
        # 새로운 값이 들어갈 인덱스에 마지막 값의 다음 인덱스를 큐의 크기로 나눈 나머지를 할당.
        self._data[avail]=e   # 새 인덱스에 데이터를 삽입
        self._size+=1  # 큐에 저장된 데이터 수를 증가.
        
    def pop(self):
        if self._size == 0:
            return -1
        answer = self._data[self._front]   #맨 앞에 있는 값을 할당
        self._data[self._front] = None   # 맨 앞에 있는 값을 제거.
        self._front = (self._front+1)%len(self._data) # 다음 값을 맨 앞으로 가져옴. 
        # 이 때 큐의 길이로 나눈 나머지를 할당. 마지막 인덱스인 경우에도 큐를 확장하지 않고 0으로 돌아옴. 원형 리스트.
        self._size-=1
        return answer
    
    def front(self): 
        if empty() == 1:
            return -1
        
        return self._data[self._front]   #맨 앞에 있는 값을 출력
    
    def back(self): 
        if empty() == 1:
            return -1
        
        return self._data[self._front + self._size - 1]   #맨 뒤에 있는 값을 출력


LinearQueue = ArrayQueue()
LinearQueue.push(1)
LinearQueue.push(2)
print(LinearQueue.front())
print(LinearQueue.back())
print(LinearQueue.size())
print(LinearQueue.empty())
print(LinearQueue.pop())
print(LinearQueue.pop())
print(LinearQueue.pop())
print(LinearQueue.size())
print(LinearQueue.empty())
print(LinearQueue.pop())
LinearQueue.push(3)
print(LinearQueue.empty())
print(LinearQueue.front())
