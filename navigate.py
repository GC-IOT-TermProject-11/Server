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
