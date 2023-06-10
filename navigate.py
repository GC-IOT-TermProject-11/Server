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
            print(path[i])
            for j in range(0, i):
                for adjacent, weight in room_graph[path[j]]['adjacent']:
                    if adjacent == path[j + 1]:
                        total_distance += weight
            break

    return total_distance
