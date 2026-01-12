# 강을 가로지르는 하나의 차선으로 된 다리가 하나 있다. 이 다리를 n 개의 트럭이 건너가려고 한다. 트럭의 순서는 바꿀 수 없으며, 트럭의 무게는 서로 같지 않을 수 있다. 다리 위에는 단지 w 대의 트럭만 동시에 올라갈 수 있다. 다리의 길이는 w 단위길이(unit distance)이며, 각 트럭들은 하나의 단위시간(unit time)에 하나의 단위길이만큼만 이동할 수 있다고 가정한다. 동시에 다리 위에 올라가 있는 트럭들의 무게의 합은 다리의 최대하중인 L보다 작거나 같아야 한다. 참고로, 다리 위에 완전히 올라가지 못한 트럭의 무게는 다리 위의 트럭들의 무게의 합을 계산할 때 포함하지 않는다고 가정한다.

# 예를 들어, 다리의 길이 w는 2, 다리의 최대하중 L은 10, 다리를 건너려는 트럭이 트럭의 무게가 [7, 4, 5, 6]인 순서대로 다리를 오른쪽에서 왼쪽으로 건넌다고 하자. 이 경우 모든 트럭이 다리를 건너는 최단시간은 아래의 그림에서 보는 것과 같이 8 이다.

# 다리의 길이와 다리의 최대하중, 그리고 다리를 건너려는 트럭들의 무게가 순서대로 주어졌을 때, 모든 트럭이 다리를 건너는 최단시간을 구하는 프로그램을 작성하라.



from collections import deque

# w: 다리 길이, L: 최대 하중, trucks: 트럭들 무게 리스트
def solution(w, L, trucks):
    trucks = deque(trucks) # 대기 트럭
    bridge = deque([0] * w) # 다리 상태 (처음엔 0으로 가득 참)
    time = 0
    current_weight = 0 # 현재 다리 위 무게 (계속 더하면 느리니까 따로 관리해요)

    while trucks:
        time += 1
        # 1. 다리에서 나가는 차 빼기
        current_weight -= bridge.popleft()

        # 2. 새 트럭이 들어올 수 있나?
        if current_weight + trucks[0] <= L:
            new_truck = trucks.popleft()
            bridge.append(new_truck)
            current_weight += new_truck
        else:
            # 못 들어오면 0을 넣어서 전진시키기
            bridge.append(0)

    # 마지막 트럭이 올라가고 반복문이 끝나므로, 다리 길이만큼 더해주면 끝!
    return time + w