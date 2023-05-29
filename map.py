import heapq
from collections import deque


def create_room_graph_4th_floor():
    rooms = {}

    # 방 노드 생성
    for i in range(401, 436):
        rooms[str(i)] = []

    # 방 연결 관계 설정
    for i in range(401, 435):
        rooms[str(i)].append((str(i + 1), 1))  # 바로 다음 호수와 거리 1로 연결
        rooms[str(i + 1)].append((str(i), 1))  # 다음 호수에서도 거꾸로 연결

    rooms['435'].append(('401', 1))  # 435호와 401호 연결
    rooms['401'].append(('435', 1))  # 401호에서도 거꾸로 연결
    rooms['433'].append(('418', 2))  # 433호와 418호 연결 (거리 2)
    rooms['418'].append(('433', 2))  # 418호에서도 거꾸로 연결
    rooms['405'].append(('412', 3))  # 405호와 412호 연결 (거리 3)
    rooms['412'].append(('405', 3))  # 412호에서도 거꾸로 연결

    return rooms


def create_room_graph_5th_floor():
    rooms = {}

    # 방 노드 생성
    for i in range(501, 533):
        rooms[str(i)] = []

    # 방 연결 관계 설정
    for i in range(501, 532):
        rooms[str(i)].append((str(i + 1), 1))  # 바로 다음 호수와 거리 1로 연결
        rooms[str(i + 1)].append((str(i), 1))  # 다음 호수에서도 거꾸로 연결

    rooms['532'].append(('501', 1))
    rooms['501'].append(('532', 1))
    rooms['531'].append(('518', 2))
    rooms['518'].append(('531', 2))
    rooms['505'].append(('512', 3))
    rooms['512'].append(('505', 3))

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
        for adjacent, weight in graph[current_node]:
            distance = current_distance + weight

            # 더 짧은 거리라면 갱신하고 큐에 추가
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                previous[adjacent] = current_node
                heapq.heappush(queue, (distance, adjacent))

    return distances, previous


# def get_shortest_path(previous, start_node, target_node):
#     path = []
#     current_node = target_node
#
#     # 도착 노드에서 시작 노드까지 역순으로 이전 노드를 따라가며 경로 구성
#     while current_node is not None:
#         path.insert(0, current_node)
#         current_node = previous[current_node]
#
#     if path[0] != start_node:
#         return []  # 시작 노드에서 도착 노드까지의 경로가 없는 경우
#
#     return path

def get_shortest_path(previous, start_node, target_node):
    path = deque()  # 경로를 저장하는 큐

    current_node = target_node
    while current_node is not None:
        path.appendleft(current_node)
        current_node = previous[current_node]

    if path[0] != start_node:
        return deque()  # 시작 노드에서 도착 노드까지의 경로가 없는 경우

    return path


# def main():
#     start_room = input("시작 노드(방)를 입력하세요: ")
#     target_room = input("도착 노드(방)를 입력하세요: ")
#
#     if start_room.startswith('4') and target_room.startswith('4'):
#         floor = '4층'
#         room_graph = create_room_graph_4th_floor()
#     elif start_room.startswith('5') and target_room.startswith('5'):
#         floor = '5층'
#         room_graph = create_room_graph_5th_floor()
#     else:
#         print("입력한 방이 4층 또는 5층에 속하지 않습니다.")
#         return
#
#     distances, previous = dijkstra(room_graph, start_room)
#     shortest_path = get_shortest_path(previous, start_room, target_room)
#
#     if shortest_path:
#         print(f"{floor} - {start_room}호에서 {target_room}호까지 최단 거리: {distances[target_room]}")
#         print("최단 경로:", " -> ".join(shortest_path))
#     else:
#         print("시작 노드에서 도착 노드까지 경로가 존재하지 않습니다.")




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
        print("최단 경로:", " -> ".join(shortest_path))

        # 경로를 따라 방문하면서 해당 노드를 제거
        queue = deque(shortest_path)
        while queue:
            current_node = queue.popleft()
            user_input = input(f"{current_node} 방을 방문하셨습니까? (방 번호 입력): ")

            if user_input == current_node:
                print("방문한 노드:", current_node)
                if queue:
                    print("남은 경로:", " -> ".join(queue))
            else:
                print("방문하지 않았습니다.")
                break
    else:
        print("시작 노드에서 도착 노드까지 경로가 존재하지 않습니다.")





if __name__ == "__main__":
    main()
