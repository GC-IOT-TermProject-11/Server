from collections import deque

import mapTest


def main(prediction):
    file_path = 'shortest_path.txt'

    with open(file_path, 'r') as file:
        shortest_path = file.read()

    # 문자열로 저장된 경로를 큐에 저장
    queue = deque(shortest_path.split(" -> "))

    room_graph = map.create_room_graph_4th_floor()

    first_node = queue[0]
    prev_node = None
    next_node = None
    next_node2 = None

    current_node = prediction
    passed_node = None
    direction = None

    if first_node == current_node:
        if len(queue) > 1:  # 남은 경로가 한 개 이상일 때
            next_node = queue[1]
            # 다음 노드를 확인해서 코너인지 아닌지 먼저 확인
            if room_graph[next_node]['is_corner'] == True:
                # print("코너입니다")
                next_node2 = queue[2]
                # print("다다음노드" + next_node2)
                if next_node == '418':
                    if current_node == '417' and next_node2 == '433':
                        direction = '우회전'
                        print('우회전')
                    elif current_node == '419' and next_node2 == '433':
                        direction = '좌회전'
                        print('좌회전')
                    elif current_node == '433' and next_node2 == '419':
                        direction = '우회전'
                        print('우회전')
                    elif current_node == '433' and next_node2 == '417':
                        direction = '좌회전'
                        print('좌회전')
                elif next_node == '425' and next_node2 == '426':
                    direction = '우회전'
                    print('우회전')
                elif next_node == '426' and next_node2 == '425':
                    direction = '좌회전'
                    print('좌회전')
                elif next_node == '433':
                    if current_node == '432' and next_node2 == '418':
                        direction = '우회전'
                        print('우회전')
                    elif current_node == '418' and next_node2 == '432':
                        direction = '좌회전'
                        print('좌회전')
                    elif current_node == '418' and next_node2 == '434':
                        direction = '우회전'
                        print('우회전')
                    elif current_node == '434' and next_node2 == '418':
                        direction = '좌회전'
                        print('좌회전')
                elif next_node == '405':
                    if current_node == '404' and next_node2 == '412':
                        direction = '우회전'
                        print('우회전')
                    elif current_node == '412' and next_node2 == '404':
                        direction = '좌회전'
                        print('좌회전')
                    elif current_node == '412' and next_node2 == '406':
                        direction = '우회전'
                        print('우회전')
                    elif current_node == '406' and next_node2 == '412':
                        direction = '좌회전'
                        print('좌회전')
                elif next_node == '407':
                    if next_node2 == '408':
                        direction = '우회전'
                        print('우회전')
                    elif next_node2 == '406':
                        direction = '좌회전'
                        print('좌회전')
                elif next_node == '411':
                    if next_node2 == '412':
                        direction = '우회전'
                        print('우회전')
                    elif next_node2 == '410':
                        direction = '좌회전'
                        print('좌회전')
                elif next_node == '412':
                    if current_node == '411' and next_node2 == '405':
                        direction = '우회전'
                        print('우회전')
                    elif current_node == '405' and next_node2 == '411':
                        direction = '좌회전'
                        print('좌회전')
                    elif current_node == '405' and next_node2 == '413':
                        direction = '우회전'
                        print('우회전')
                    elif current_node == '413' and next_node2 == '405':
                        direction = '좌회전'
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
