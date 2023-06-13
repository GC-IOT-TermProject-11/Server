import map


def distance(prediction):
    file_path = 'shortest_path.txt'

    with open(file_path, 'r') as file:
        shortest_path = file.read()

    # 문자열로 저장된 경로를 리스트에 저장
    path = shortest_path.split(' -> ')

    if str(path[0]).startswith('4'):
        room_graph = map.create_room_graph_4th_floor()
    elif str(path[0]).startswith('5'):
        room_graph = map.create_room_graph_5th_floor()

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

    print(total_distance)

    return total_distance


def direction(prediction):
    file_path = 'shortest_path.txt'

    with open(file_path, 'r') as file:
        shortest_path = file.read()

    result = '직진'

    # 문자열로 저장된 경로를 리스트에 저장
    path = shortest_path.split(' -> ')
    if str(path[0]).startswith('4'):
        room_graph = map.create_room_graph_4th_floor()

        # path[0]이 현 위치
        # path[1]이 다음 노드
        # path[2]가 다다음 노드

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

    elif str(path[0]).startswith('5'):
        room_graph = map.create_room_graph_5th_floor()

        # path[0]이 현 위치
        # path[1]이 다음 노드
        # path[2]가 다다음 노드

        # 경로가 2개보다 많을 때 (세 노드를 비교하여 방향 판단 가능)
        if room_graph[path[1]]['is_corner']:
            if len(path) > 2:
                if path[1] == '520':
                    if path[0] == '531' and path[2] == '521':
                        result = '우회전'
                    elif path[0] == '531' and path[2] == '519':
                        result = '좌회전'
                    elif path[0] == '519' and path[2] == '531':
                        result = '우회전'
                    elif path[0] == '521' and path[2] == '531':
                        result = '좌회전'
                elif path[1] == '525' and path[2] == '526':
                    result = '우회전'
                elif path[1] == '526' and path[2] == '525':
                    result = '좌회전'
                elif path[1] == '531':
                    if path[0] == '520' and path[2] == '532':
                        result = '우회전'
                    elif path[0] == '520' and path[2] == '530':
                        result = '좌회전'
                    elif path[0] == '530' and path[2] == '520':
                        result = '우회전'
                    elif path[0] == '532' and path[2] == '520':
                        result = '좌회전'
                elif path[1] == '505':
                    if path[0] == '504' and path[2] == '512':
                        result = '우회전'
                    elif path[0] == '512' and path[2] == '504':
                        result = '좌회전'
                    elif path[0] == '512' and path[2] == '506':
                        result = '우회전'
                    elif path[0] == '506' and path[2] == '512':
                        result = '좌회전'
                elif path[1] == '507':
                    if path[2] == '508':
                        result = '우회전'
                    elif path[2] == '506':
                        result = '좌회전'
                elif path[1] == '511':
                    if path[2] == '512':
                        result = '우회전'
                    elif path[2] == '510':
                        result = '좌회전'
                elif path[1] == '512':
                    if path[0] == '511' and path[2] == '505':
                        result = '우회전'
                    elif path[0] == '505' and path[2] == '511':
                        result = '좌회전'
                    elif path[0] == '505' and path[2] == '513':
                        result = '우회전'
                    elif path[0] == '513' and path[2] == '505':
                        result = '좌회전'

    return result
