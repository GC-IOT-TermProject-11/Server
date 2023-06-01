import heapq
from collections import deque


def create_room_graph_4th_floor():
    rooms = {}

    # 방 노드 생성
    for i in range(401, 436):
        rooms[str(i)] = {
            'adjacent': [],
            'is_corner': False  # 코너 여부를 나타내는 변수
        }

    # 방 연결 관계 설정
    for i in range(401, 435):
        rooms[str(i)]['adjacent'].append((str(i + 1), 1))  # 바로 다음 호수와 거리 1로 연결
        rooms[str(i + 1)]['adjacent'].append((str(i), 1))  # 다음 호수에서도 거꾸로 연결

    rooms['435']['adjacent'].append(('401', 1))  # 435호와 401호 연결
    rooms['401']['adjacent'].append(('435', 1))  # 401호에서도 거꾸로 연결
    rooms['433']['adjacent'].append(('418', 2))  # 433호와 418호 연결 (거리 2)
    rooms['418']['adjacent'].append(('433', 2))  # 418호에서도 거꾸로 연결
    rooms['405']['adjacent'].append(('412', 3))  # 405호와 412호 연결 (거리 3)
    rooms['412']['adjacent'].append(('405', 3))  # 412호에서도 거꾸로 연결

    # 코너 설정
    rooms['405']['is_corner'] = True
    rooms['407']['is_corner'] = True
    rooms['411']['is_corner'] = True
    rooms['412']['is_corner'] = True
    rooms['418']['is_corner'] = True
    rooms['425']['is_corner'] = True
    rooms['426']['is_corner'] = True
    rooms['433']['is_corner'] = True

    return rooms


def create_room_graph_5th_floor():
    rooms = {}

    # 방 노드 생성
    for i in range(501, 533):
        rooms[str(i)] = {
            'adjacent': [],
            'is_corner': False  # 코너 여부를 나타내는 변수
        }

    # 방 연결 관계 설정
    for i in range(501, 532):
        rooms[str(i)]['adjacent'].append((str(i + 1), 1))  # 바로 다음 호수와 거리 1로 연결
        rooms[str(i + 1)]['adjacent'].append((str(i), 1))  # 다음 호수에서도 거꾸로 연결

    rooms['532']['adjacent'].append(('501', 1))
    rooms['501']['adjacent'].append(('532', 1))
    rooms['531']['adjacent'].append(('518', 2))
    rooms['518']['adjacent'].append(('531', 2))
    rooms['505']['adjacent'].append(('512', 3))
    rooms['512']['adjacent'].append(('505', 3))

    # 코너 설정
    rooms['505']['is_corner'] = True
    rooms['512']['is_corner'] = True

    return rooms


def dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph}  # 모든 노드의 거리를 무한대로 초기화
    distances[start_node] = 0  # 시작 노드의 거리는 0
    previous = {node: None for node in graph}  # 이전 노드를 저장하기 위한 딕셔너리

    queue = []
    heapq.heappush(queue, (distances[start_node], start_node))  # 우선순위 큐에 시작 노드를 추가

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # 이미 처리된 노드는 무시
        if current_distance > distances[current_node]:
            continue

        # 인접한 노드들의 거리 갱신
        for adjacent, weight in graph[current_node]['adjacent']:
            distance = current_distance + weight

            # 더 짧은 거리라면 갱신하고 큐에 추가
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                previous[adjacent] = current_node
                heapq.heappush(queue, (distance, adjacent))

    return distances, previous


def get_shortest_path(previous, start_node, target_node):
    path = deque()  # 경로를 저장하는 큐

    current_node = target_node
    while current_node is not None:
        path.appendleft(current_node)
        current_node = previous[current_node]

    if path[0] != start_node:
        return ""  # 시작 노드에서 도착 노드까지의 경로가 없는 경우

    return " -> ".join(path)  # 경로를 문자열로 변환하여 반환


def main():
    start_room = input("시작 노드(방)를 입력하세요: ")
    target_room = input("도착 노드(방)를 입력하세요: ")

    if start_room.startswith('4') and target_room.startswith('4'):
        floor = '4층'
        room_graph = create_room_graph_4th_floor()
    elif start_room.startswith('5') and target_room.startswith('5'):
        floor = '5층'
        room_graph = create_room_graph_5th_floor()
    else:
        print("입력한 방이 4층 또는 5층에 속하지 않습니다.")
        return

    distances, previous = dijkstra(room_graph, start_room)
    shortest_path = get_shortest_path(previous, start_room, target_room)

    if shortest_path:
        print(f"{floor} - {start_room}호에서 {target_room}호까지 최단 거리: {distances[target_room]}")
        print("최단 경로:", shortest_path)

        # 경로를 따라 방문하면서 해당 노드를 제거
        queue = deque(shortest_path.split(" -> "))
        first_node = queue[0]
        prev_node = None
        next_node = None
        next_node2 = None
        passed_node = None
        while queue:
            current_node = queue[0]
            user_input = input(f"{current_node} 방을 방문하셨습니까? (방 번호 입력): ")
            # 방문해야하는 강의실과 내 위치가 일치 할 경우
            if user_input == current_node:
                if len(queue) > 1:  # 남은 경로가 한 개 이상일 때
                    next_node = queue[1]
                    # 다음 노드를 확인해서 코너인지 아닌지 먼저 확인
                    if room_graph[next_node]['is_corner'] == True:
                        # print("코너입니다")
                        next_node2 = queue[2]
                        # print("다다음노드" + next_node2)
                        if next_node == '418':
                            if current_node == '417' and next_node2 == '433':
                                print('우회전')
                            elif current_node == '419' and next_node2 == '433':
                                print('좌회전')
                            elif current_node == '433' and next_node2 == '419':
                                print('우회전')
                            elif current_node == '433' and next_node2 == '417':
                                print('좌회전')
                        elif next_node == '425' and next_node2 == '426':
                            print('우회전')
                        elif next_node == '426' and next_node2 == '425':
                            print('좌회전')
                        elif next_node == '433':
                            if current_node == '432' and next_node2 == '418':
                                print('우회전')
                            elif current_node == '418' and next_node2 == '432':
                                print('좌회전')
                            elif current_node == '418' and next_node2 == '434':
                                print('우회전')
                            elif current_node == '434' and next_node2 == '418':
                                print('좌회전')
                        elif next_node == '405':
                            if current_node == '404' and next_node2 == '412':
                                print('우회전')
                            elif current_node == '412' and next_node2 == '404':
                                print('좌회전')
                            elif current_node == '412' and next_node2 == '406':
                                print('우회전')
                            elif current_node == '406' and next_node2 == '412':
                                print('좌회전')
                        elif next_node == '407':
                            if next_node2 == '408':
                                print('우회전')
                            elif next_node2 == '406':
                                print('좌회전')
                        elif next_node == '411':
                            if next_node2 == '412':
                                print('우회전')
                            elif next_node2 == '410':
                                print('좌회전')
                        elif next_node == '412':
                            if current_node == '411' and next_node2 == '405':
                                print('우회전')
                            elif current_node == '405' and next_node2 == '411':
                                print('좌회전')
                            elif current_node == '405' and next_node2 == '413':
                                print('우회전')
                            elif current_node == '413' and next_node2 == '405':
                                print('좌회전')
                    print("현재위치~목적지", " -> ".join(queue), "다음 노드:", next_node)
                    # print("현재위치~목적지", " -> ".join(queue), "이전 노드: ", prev_node, " 다음 노드: ", next_node)
                else:  # 남은 경로가 마지막 경로 즉, 목적지 하나만 남았을 때
                    prev_node = passed_node
                    print("현재위치~목적지:", " -> ".join(queue), "이전 노드: ", prev_node)
                passed_node = current_node
                queue.popleft()
                if current_node == target_room:
                    print("도착했습니다!")
            # 방문해야하는 강의실과 내 위치가 일치하지 않을 경우
            else:
                print("방문하지 않았습니다.")
                continue

    else:
        print("시작 노드에서 도착 노드까지 경로가 존재하지 않습니다.")


if __name__ == "__main__":
    main()
