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

    rooms['4엘레베이터2'] = {
        'adjacent': [],
        'is_corner': False  # 코너 여부를 나타내는 변수
    }
    rooms['4엘레베이터3'] = {
        'adjacent': [],
        'is_corner': False  # 코너 여부를 나타내는 변수
    }
    rooms['4아르테크네'] = {
        'adjacent': [],
        'is_corner': False  # 코너 여부를 나타내는 변수
    }
    rooms['4야외 테라스'] = {
        'adjacent': [],
        'is_corner': False  # 코너 여부를 나타내는 변수
    }
    # 방 연결 관계 설정
    rooms['401']['adjacent'].append(('402', 5))  # 401호와 402호를 5m 거리로 연결
    rooms['401']['adjacent'].append(('435', 7.5))  # 401호와 435호를 8m 거리로 연결
    rooms['402']['adjacent'].append(('401', 5))  # 402호와 401호를 5m 거리로 연결
    rooms['402']['adjacent'].append(('403', 7.5))  # 402호와 403호를 5m 거리로 연결
    rooms['403']['adjacent'].append(('402', 7.5))  # 403호와 402호를 5m 거리로 연결
    rooms['403']['adjacent'].append(('404', 9.9))  # 403호와 404호를 9.9m 거리로 연결
    rooms['404']['adjacent'].append(('403', 9.9))  # 404호와 403호를 9.9m 거리로 연결
    rooms['404']['adjacent'].append(('405', 9.9))  # 404호와 405호를 9.9m 거리로 연결
    rooms['405']['adjacent'].append(('404', 9.9))  # 405호와 404호를 9.9m 거리로 연결
    rooms['405']['adjacent'].append(('406', 9.9))  # 405호와 406호를 9.9m 거리로 연결
    rooms['406']['adjacent'].append(('405', 9.9))  # 406호와 405호를 9.9m 거리로 연결
    rooms['406']['adjacent'].append(('407', 3.3))  # 406호와 407호를 9.9m 거리로 연결
    rooms['407']['adjacent'].append(('406', 3.3))  # 407호와 406호를 9.9m 거리로 연결
    rooms['407']['adjacent'].append(('408', 6.6))  # 407호와 408호를 6.6m 거리로 연결
    rooms['408']['adjacent'].append(('407', 6.6))  # 408호와 407호를 6.6m 거리로 연결
    rooms['408']['adjacent'].append(('409', 6.6))  # 408호와 409호를 6.6m 거리로 연결
    rooms['409']['adjacent'].append(('408', 6.6))  # 409호와 408호를 6.6m 거리로 연결
    rooms['409']['adjacent'].append(('410', 6.6))  # 409호와 410호를 6.6m 거리로 연결
    rooms['410']['adjacent'].append(('409', 6.6))  # 410호와 409호를 6.6m 거리로 연결
    rooms['410']['adjacent'].append(('411', 3.3))  # 410호와 411호를 2.5m 거리로 연결
    rooms['411']['adjacent'].append(('410', 3.3))  # 411호와 410호를 2.5m 거리로 연결
    rooms['411']['adjacent'].append(('412', 4.5))  # 411호와 412호를 9.9m 거리로 연결
    rooms['412']['adjacent'].append(('411', 4.5))  # 412호와 411호를 9.9m 거리로 연결
    rooms['412']['adjacent'].append(('413', 9.9))  # 412호와 413호를 9.9m 거리로 연결
    rooms['413']['adjacent'].append(('412', 9.9))  # 413호와 412호를 9.9m 거리로 연결
    rooms['413']['adjacent'].append(('414', 9.9))  # 413호와 414호를 9.9m 거리로 연결
    rooms['414']['adjacent'].append(('413', 9.9))  # 414호와 413호를 9.9m 거리로 연결
    rooms['414']['adjacent'].append(('415', 9.9))  # 414호와 415호를 9.9m 거리로 연결
    rooms['415']['adjacent'].append(('414', 9.9))  # 415호와 414호를 9.9m 거리로 연결
    rooms['415']['adjacent'].append(('416', 5))  # 415호와 416호를 2m 거리로 연결
    rooms['416']['adjacent'].append(('415', 5))  # 416호와 415호를 2m 거리로 연결
    rooms['416']['adjacent'].append(('417', 3.3))  # 416호와 417호를 3.3m 거리로 연결
    rooms['417']['adjacent'].append(('416', 3.3))  # 417호와 416호를 3.3m 거리로 연결
    rooms['417']['adjacent'].append(('418', 3.3))  # 417호와 418호를 3.3m 거리로 연결
    rooms['418']['adjacent'].append(('417', 3.3))  # 418호와 417호를 3.3m 거리로 연결
    rooms['418']['adjacent'].append(('419', 3.3))  # 418호와 419호를 3.3m 거리로 연결
    rooms['419']['adjacent'].append(('418', 3.3))  # 419호와 418호를 3.3m 거리로 연결
    rooms['419']['adjacent'].append(('420', 3.3))  # 419호와 420호를 6.6m 거리로 연결
    rooms['420']['adjacent'].append(('419', 3.3))  # 420호와 419호를 6.6m 거리로 연결
    rooms['420']['adjacent'].append(('421', 3.3))  # 420호와 421호를 6.6m 거리로 연결
    rooms['421']['adjacent'].append(('420', 3.3))  # 421호와 420호를 6.6m 거리로 연결
    rooms['421']['adjacent'].append(('422', 3.3))  # 421호와 422호를 3.3m 거리로 연결
    rooms['422']['adjacent'].append(('421', 3.3))  # 422호와 421호를 3.3m 거리로 연결
    rooms['422']['adjacent'].append(('423', 3.3))  # 422호와 423호를 3.3m 거리로 연결
    rooms['423']['adjacent'].append(('422', 3.3))  # 423호와 422호를 3.3m 거리로 연결
    rooms['423']['adjacent'].append(('424', 3.3))  # 423호와 424호를 3.3m 거리로 연결
    rooms['424']['adjacent'].append(('423', 3.3))  # 424호와 423호를 3.3m 거리로 연결
    rooms['424']['adjacent'].append(('425', 3.3))  # 424호와 425호를 3.3m 거리로 연결
    rooms['425']['adjacent'].append(('424', 3.3))  # 425호와 424호를 3.3m 거리로 연결
    rooms['425']['adjacent'].append(('4아르테크네', 3.3))  # 425호와 426호를 3.3m 거리로 연결
    rooms['4아르테크네']['adjacent'].append(('425', 3.3))  # 426호와 425호를 3.3m 거리로 연결
    rooms['4아르테크네']['adjacent'].append(('426', 3.3))  # 425호와 426호를 3.3m 거리로 연결
    rooms['426']['adjacent'].append(('4아르테크네', 3.3))  # 426호와 425호를 3.3m 거리로 연결
    rooms['426']['adjacent'].append(('427', 3.3))  # 426호와 427호를 3.3m 거리로 연결
    rooms['427']['adjacent'].append(('426', 3.3))  # 427호와 426호를 3.3m 거리로 연결
    rooms['427']['adjacent'].append(('428', 3.3))  # 427호와 428호를 3.3m 거리로 연결
    rooms['428']['adjacent'].append(('427', 3.3))  # 428호와 427호를 3.3m 거리로 연결
    rooms['428']['adjacent'].append(('429', 3.3))  # 428호와 429호를 3.3m 거리로 연결
    rooms['429']['adjacent'].append(('428', 3.3))  # 429호와 428호를 3.3m 거리로 연결
    rooms['429']['adjacent'].append(('430', 3.3))  # 429호와 430호를 3.3m 거리로 연결
    rooms['430']['adjacent'].append(('429', 3.3))  # 430호와 429호를 3.3m 거리로 연결
    rooms['430']['adjacent'].append(('431', 3.3))  # 430호와 431호를 3.3m 거리로 연결
    rooms['431']['adjacent'].append(('430', 3.3))  # 431호와 430호를 3.3m 거리로 연결
    rooms['431']['adjacent'].append(('432', 3.3))  # 431호와 432호를 3.3m 거리로 연결
    rooms['432']['adjacent'].append(('431', 3.3))  # 432호와 431호를 3.3m 거리로 연결
    rooms['432']['adjacent'].append(('433', 3.3))  # 432호와 433호를 3.3m 거리로 연결
    rooms['433']['adjacent'].append(('432', 3.3))  # 433호와 432호를 3.3m 거리로 연결
    rooms['433']['adjacent'].append(('434', 3.3))  # 433호와 434호를 3.3m 거리로 연결
    rooms['434']['adjacent'].append(('433', 3.3))  # 434호와 433호를 3.3m 거리로 연결
    rooms['434']['adjacent'].append(('435', 3.3))  # 434호와 435호를 3.3m 거리로 연결
    rooms['435']['adjacent'].append(('434', 3.3))  # 435호와 434호를 3.3m 거리로 연결
    rooms['435']['adjacent'].append(('401', 7.5))  # 435호와 401호를 8m 거리로 연결
    rooms['418']['adjacent'].append(('4엘레베이터2', 6.2))  # 엘레베이터2와 418연결
    rooms['4엘레베이터2']['adjacent'].append(('418', 6.2))
    rooms['433']['adjacent'].append(('4엘레베이터2', 6.2))  # 엘레베이터2와 433연결
    rooms['4엘레베이터2']['adjacent'].append(('433', 6.2))
    rooms['4야외 테라스']['adjacent'].append(('4엘레베이터2', 6.2))  # 엘레베이터2와 야외 테라스 연결
    rooms['4엘레베이터2']['adjacent'].append(('4야외 테라스', 6.2))

    # 엘베3
    rooms['405']['adjacent'].append(('4엘레베이터3', 17))
    rooms['4엘레베이터3']['adjacent'].append(('405', 17))
    rooms['412']['adjacent'].append(('4엘레베이터3', 8))
    rooms['4엘레베이터3']['adjacent'].append(('412', 8))
    rooms['410']['adjacent'].append(('4엘레베이터3', 8))
    rooms['4엘레베이터3']['adjacent'].append(('410', 8))

    # 코너 설정
    rooms['405']['is_corner'] = True
    rooms['407']['is_corner'] = True
    rooms['410']['is_corner'] = True
    rooms['411']['is_corner'] = True
    rooms['412']['is_corner'] = True
    rooms['418']['is_corner'] = True
    rooms['426']['is_corner'] = True
    rooms['433']['is_corner'] = True
    rooms['4아르테크네']['is_corner'] = True
    rooms['4엘레베이터2']['is_corner'] = True
    rooms['4엘레베이터3']['is_corner'] = True
    return rooms


def create_room_graph_5th_floor():
    rooms = {}

    # 방 노드 생성
    for i in range(501, 533):
        rooms[str(i)] = {
            'adjacent': [],
            'is_corner': False  # 코너 여부를 나타내는 변수
        }
    rooms['5엘레베이터1'] = {
        'adjacent': [],
        'is_corner': False  # 코너 여부를 나타내는 변수
    }
    rooms['5엘레베이터2'] = {
        'adjacent': [],
        'is_corner': False  # 코너 여부를 나타내는 변수
    }
    rooms['5엘레베이터3'] = {
        'adjacent': [],
        'is_corner': False  # 코너 여부를 나타내는 변수
    }
    rooms['502쪽 큐브'] = {
        'adjacent': [],
        'is_corner': False  # 코너 여부를 나타내는 변수
    }
    rooms['515쪽 큐브'] = {
        'adjacent': [],
        'is_corner': False  # 코너 여부를 나타내는 변수
    }

    # 방 연결 관계 설정
    rooms['501']['adjacent'].append(('502', 5))
    rooms['501']['adjacent'].append(('532', 7.5))
    rooms['502']['adjacent'].append(('501', 5))
    rooms['502']['adjacent'].append(('503', 7.5))
    rooms['503']['adjacent'].append(('502', 7.5))
    rooms['503']['adjacent'].append(('504', 9.9))
    rooms['504']['adjacent'].append(('503', 9.9))
    rooms['504']['adjacent'].append(('505', 9.9))
    rooms['505']['adjacent'].append(('504', 9.9))
    rooms['505']['adjacent'].append(('506', 9.9))
    rooms['506']['adjacent'].append(('505', 9.9))
    rooms['506']['adjacent'].append(('507', 3.3))
    rooms['507']['adjacent'].append(('506', 3.3))
    rooms['507']['adjacent'].append(('508', 6.6))
    rooms['508']['adjacent'].append(('507', 6.6))
    rooms['508']['adjacent'].append(('509', 6.6))
    rooms['509']['adjacent'].append(('508', 6.6))
    rooms['509']['adjacent'].append(('510', 6.6))
    rooms['510']['adjacent'].append(('509', 6.6))
    rooms['510']['adjacent'].append(('511', 3.3))
    rooms['511']['adjacent'].append(('510', 3.3))
    rooms['511']['adjacent'].append(('512', 4.5))
    rooms['512']['adjacent'].append(('511', 4.5))
    rooms['512']['adjacent'].append(('513', 6.6))
    rooms['513']['adjacent'].append(('512', 6.6))
    rooms['513']['adjacent'].append(('514', 5))
    rooms['514']['adjacent'].append(('513', 5))
    rooms['514']['adjacent'].append(('515', 5))
    rooms['515']['adjacent'].append(('514', 5))
    rooms['515']['adjacent'].append(('516', 5))
    rooms['516']['adjacent'].append(('515', 5))
    rooms['516']['adjacent'].append(('517', 3.3))
    rooms['517']['adjacent'].append(('516', 3.3))
    rooms['517']['adjacent'].append(('518', 5))
    rooms['518']['adjacent'].append(('517', 5))
    rooms['518']['adjacent'].append(('519', 6.6))
    rooms['519']['adjacent'].append(('518', 6.6))
    rooms['519']['adjacent'].append(('520', 5))
    rooms['520']['adjacent'].append(('519', 5))
    rooms['520']['adjacent'].append(('521', 5))
    rooms['521']['adjacent'].append(('520', 5))
    rooms['520']['adjacent'].append(('5층엘레베이터2', 5))
    rooms['5엘레베이터2']['adjacent'].append(('520', 5))
    rooms['5엘레베이터2']['adjacent'].append(('531', 6.2))
    rooms['531']['adjacent'].append(('5엘레베이터2', 6.2))
    rooms['521']['adjacent'].append(('522', 5))
    rooms['522']['adjacent'].append(('521', 5))
    rooms['522']['adjacent'].append(('523', 5))
    rooms['523']['adjacent'].append(('522', 5))
    rooms['523']['adjacent'].append(('524', 5))
    rooms['524']['adjacent'].append(('523', 5))
    rooms['524']['adjacent'].append(('525', 5))
    rooms['525']['adjacent'].append(('524', 5))
    rooms['525']['adjacent'].append(('5엘레베이터1', 3.3))
    rooms['5엘레베이터1']['adjacent'].append(('525', 3.3))
    rooms['526']['adjacent'].append(('5엘레베이터1', 3.3))
    rooms['5엘레베이터1']['adjacent'].append(('526', 3.3))
    rooms['526']['adjacent'].append(('527', 5))
    rooms['527']['adjacent'].append(('526', 5))
    rooms['527']['adjacent'].append(('528', 5))
    rooms['528']['adjacent'].append(('527', 5))
    rooms['528']['adjacent'].append(('529', 5))
    rooms['529']['adjacent'].append(('528', 5))
    rooms['529']['adjacent'].append(('530', 5))
    rooms['530']['adjacent'].append(('529', 5))
    rooms['530']['adjacent'].append(('531', 5))
    rooms['531']['adjacent'].append(('530', 5))
    rooms['531']['adjacent'].append(('532', 5))
    rooms['532']['adjacent'].append(('531', 5))
    rooms['503']['adjacent'].append(('502쪽 큐브', 5))
    rooms['502쪽 큐브']['adjacent'].append(('503', 5))
    rooms['502쪽 큐브']['adjacent'].append(('515쪽 큐브', 10))
    rooms['515쪽 큐브']['adjacent'].append(('502쪽 큐브', 10))
    rooms['502쪽 큐브']['adjacent'].append(('515', 5))
    rooms['515']['adjacent'].append(('502쪽 큐브', 5))

    # 엘베3
    rooms['505']['adjacent'].append(('5엘레베이터3', 17))
    rooms['5엘레베이터3']['adjacent'].append(('505', 17))
    rooms['512']['adjacent'].append(('5엘레베이터3', 8))
    rooms['5엘레베이터3']['adjacent'].append(('512', 8))
    rooms['510']['adjacent'].append(('5엘레베이터3', 8))
    rooms['5엘레베이터3']['adjacent'].append(('510', 8))

    # 코너 설정
    rooms['503']['is_corner'] = True
    rooms['515']['is_corner'] = True
    rooms['505']['is_corner'] = True
    rooms['507']['is_corner'] = True
    rooms['511']['is_corner'] = True
    rooms['512']['is_corner'] = True
    rooms['520']['is_corner'] = True
    rooms['525']['is_corner'] = True
    rooms['526']['is_corner'] = True
    rooms['531']['is_corner'] = True
    rooms['5엘레베이터1']['is_corner'] = True
    rooms['5엘레베이터3']['is_corner'] = True

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


def main(start_room, target_room):
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
        return shortest_path

        # 경로를 따라 방문하면서 해당 노드를 제거
        queue = deque(shortest_path.split(" -> "))
        first_node = queue[0]
        prev_node = None
        next_node = None
        passed_node = None
        while queue:
            current_node = queue[0]
            user_input = input(f"{current_node} 방을 방문하셨습니까? (방 번호 입력): ")

            # 방문해야 하는 강의실과 내 위치가 일치 할 경우
            if user_input == current_node:
                if len(queue) > 1:  # 남은 경로가 한 개 이상일 때
                    if user_input == first_node:  # 현재 위치가 최단 경로의 가장 첫번째 강의실일 때
                        next_node = queue[1]
                        print("현재위치~목적지", " -> ".join(queue), "다음 노드: ", next_node)
                    else:
                        next_node = queue[1]
                        prev_node = passed_node
                        print("현재위치~목적지", " -> ".join(queue), "이전 노드: ", prev_node, " 다음 노드: ", next_node)
                else:  # 남은 경로가 마지막 경로 즉, 목적지 하나만 남았을 때
                    prev_node = passed_node
                    print("현재위치~목적지:", " -> ".join(queue), "이전 노드: ", prev_node)
                passed_node = current_node
                if current_node == queue[-1]:
                    print("도착했습니다!")
            # 방문해야하는 강의실과 내 위치가 일치하지 않을 경우
            else:
                print("방문하지 않았습니다.")
                break
            queue.popleft()
    else:
        print("시작 노드에서 도착 노드까지 경로가 존재하지 않습니다.")
        return None


if __name__ == "__main__":
    start_room = input("시작 노드(방)를 입력하세요: ")
    target_room = input("도착 노드(방)를 입력하세요: ")
    path = main(start_room, target_room).split(' -> ')
    room_graph = create_room_graph_4th_floor()

    total_distance = 0
    # 현재 위치에서 제일 가까운 코너 찾아 그 코너까지 거리 구하기
    for i in range(0, len(path)):
        if room_graph[path[i]]['is_corner'] and i != 0:

            for j in range(0, i):
                for adjacent, weight in room_graph[path[j]]['adjacent']:
                    if adjacent == path[j + 1]:
                        total_distance += weight
            break

    # 경로상에 코너가 없으면 그냥 현재 위치부터 목적지까지 모두 더하기
    if total_distance == 0:
        for i in range(0, len(path) - 1):
            for adjacent, weight in room_graph[path[i]]['adjacent']:
                if adjacent == path[i + 1]:
                    total_distance += weight

    result = '직진'
    # 경로가 2개보다 많을 때 (세 노드를 비교하여 방향 판단 가능)
    if room_graph[path[1]]['is_corner']:
        if len(path) > 2:
            if path[1] == '418':
                if path[0] == '417' and path[2] == '433':
                    result = '우회전'
                elif path[0] == '419' and path[2] == '433':
                    result = '좌회전'
                elif path[0] == '433' and path[2] == '419':
                    result = '우회전'
                elif path[0] == '433' and path[2] == '417':
                    result = '좌회전'
            elif path[1] == '425' and path[2] == '426':
                result = '우회전'
            elif path[1] == '426' and path[2] == '425':
                result = '좌회전'
            elif path[1] == '433':
                if path[0] == '432' and path[2] == '418':
                    result = '우회전'
                elif path[0] == '418' and path[2] == '432':
                    result = '좌회전'
                elif path[0] == '418' and path[2] == '434':
                    result = '우회전'
                elif path[0] == '434' and path[2] == '418':
                    result = '좌회전'
            elif path[1] == '405':
                if path[0] == '404' and path[2] == '412':
                    result = '우회전'
                elif path[0] == '412' and path[2] == '404':
                    result = '좌회전'
                elif path[0] == '412' and path[2] == '406':
                    result = '우회전'
                elif path[0] == '406' and path[2] == '412':
                    result = '좌회전'
            elif path[1] == '407':
                if path[2] == '408':
                    result = '우회전'
                elif path[2] == '406':
                    result = '좌회전'
            elif path[1] == '411':
                if path[2] == '412':
                    result = '우회전'
                elif path[2] == '410':
                    result = '좌회전'
            elif path[1] == '412':
                if path[0] == '411' and path[2] == '405':
                    result = '우회전'
                elif path[0] == '405' and path[2] == '411':
                    result = '좌회전'
                elif path[0] == '405' and path[2] == '413':
                    result = '우회전'
                elif path[0] == '413' and path[2] == '405':
                    result = '좌회전'

    print(total_distance)
    print(result)
