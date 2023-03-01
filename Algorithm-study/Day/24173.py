# 알고리즘 수업 - 힙 정렬1
unsorted = 5
index = 2
heap_size = [2,5,1,4,3]

def check_swap_up(self, idx):
	# 삽입한 모드의 부모 노드가 없을 경우
    if idx <= 1:
    	return False

	parent_idx = idx // 2

	if self.heap[idx] > self.heap[parent_idx]:
		return True
	else:
    return False

# 데이터 삽입
def insert(self, data):
	self.heap.append(data)
    idx = len(self.heap) - 1

    # check_swap_up() 의 값이 참이라면 부모와 위치 바꾸기
    while self.check_swap_up(idx):
    	parent_idx = idx // 2

        self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
        idx = parent_idx

	return True