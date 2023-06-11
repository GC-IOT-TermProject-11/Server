from collections import deque

import mapTest
import map


def main(prediction):
    file_path = 'shortest_path.txt'

    with open(file_path, 'r') as file:
        shortest_path = file.read()

    # 문자열로 저장된 경로를 리스트에 저장
    path = shortest_path.split(' -> ')

    room_graph = map.create_room_graph_4th_floor()

    total_distance = 0
    for i in range(0, len(path)):
        if room_graph[path[i]]['is_corner']:
            # 현재위치가 코너 노드인 경우 현재 노드에서 부터 다음 노드까지의 거리를 total distance로 갱신
            # 방향은 코너노드의 전노드, 다음노드를 통해 판단
            if i == 0:
                for adjacent, weight in room_graph[path[i]]['adjacent']:
                    if adjacent == path[i + 1]:
                        total_distance += weight
                break
            for j in range(0, i):
                for adjacent, weight in room_graph[path[j]]['adjacent']:
                    if adjacent == path[j + 1]:
                        total_distance += weight
            break

    print(total_distance)

    return total_distance


def direction(prediction):
    file_path = 'shortest_path.txt'

    with open(file_path, 'r') as file:
        shortest_path = file.read()

    # 문자열로 저장된 경로를 리스트에 저장
    path = shortest_path.split(' -> ')

    room_graph = map.create_room_graph_4th_floor()

    result = '직진'

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

    # # 경로가 2개 이하일 경우 (세 노드를 비교하여 방향 판단 불가)  --> 회전이 없음
    # else:
    #     dir = '직진'

    return result
