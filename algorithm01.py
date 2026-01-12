
# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 

# 이제 순서대로 K번째 사람을 제거한다. 
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
# 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 
# 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 
# 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.




from collections import deque :
N , K = 7, 3
# N=7, K=3 이라고 가정
people = deque(range(1, n + 1))# [1, 2, 3, 4, 5, 6, 7]
result = []                    # 제거된 사람을 담을 접시

# K번째 사람을 찾아서 제거하기 (핵심 로직)
while people:
    for _ in range(K - 1) # 1. (K-1)명은 뒤로 보내기 (넘기기)
        front_person = people.popleft()  # 맨 앞사람 나와!
        people.append(front_person)      # 뒤로 가서 서!
    # 이제 맨 앞에 온 K번째 사람을 제거 (빼기)
    removed = people.popleft()    # 넌 탈락!
    result.append(removed)        # 접시에 담기
    # 마지막 : 결과 출력하기 (마무리)
    # 숫자를 문자로 바꿔서 쉼표로 연결하기
    print("<" + "," .join(map(str, result))+ ">")



# 1~N번까지 줄 세우기	q = deque(range(1, N+1))	숫자를 순서대로 바구니에 담음
# 사람이 있으면 반복	while q:	줄이 텅 빌 때까지 계속하라는 뜻
# K-1번 동안 넘기기	for _ in range(K-1): q.append(q.popleft())	"하나, 둘" 할 때 뒤로 보내는 동작
# K번째 사람 제거	result.append(q.popleft())	"셋!" 할 때 바구니에 쏙 담는 동작