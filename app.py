from flask import Flask, request, jsonify
import joblib, csv, os
import pandas as pd
import map

app = Flask(__name__)
model = joblib.load('model.joblib')
base_csv_file = 'base.csv'


@app.route('/')
def hello():
    return 'It is only calculating Server'


@app.route('/predict', methods=['POST'])
def predict():
    # 클라이언트로부터 전달된 와이파이 리스트 가져오기
    data = request.get_json()
    wifi_list = data.get('wifiList', [])

    # 예측을 위해 입력 데이터 형식 변환
    input_data = []
    for wifi in wifi_list:
        bssid = wifi.get('BSSID')
        rssi = wifi.get('RSSI')
        app.logger.info('BSSID: %s, RSSI: %s', bssid, rssi)  # 클라이언트에서 받은 값을 로그로 출력
        input_data.append([bssid, rssi])

    with open('test.csv', 'w') as file:
        write = csv.writer(file)
        write.writerow(input_data)

    # base.csv 파일을 데이터프레임으로 읽어오기
    df = pd.read_csv(base_csv_file)

    # BSSID와 받아온 값 매핑
    for received_value in input_data:
        bssid, rssi = received_value
        # BSSID 값이 일치하는 열의 인덱스를 찾기
        matching_columns = df.columns[df.columns == bssid]

        # 일치하는 BSSID 값이 존재하는 경우에만 RSSI 값을 변경
        if len(matching_columns) > 0:
            column_index = matching_columns[0]
            df[column_index] = rssi

    # 모델에 예측 입력 데이터 전달
    X = df.drop(columns=['room'])

    # 모델 예측
    predictions = model.predict(X)
    predictions = [str(pred) for pred in predictions]  # 모든 원소를 문자열로 변환

    response = {'predictions': predictions}

    # 예측 결과를 클라이언트에 반환
    return jsonify(response)


@app.route('/pathfind', methods=['POST'])
def pathfind():
    data = request.get_json()
    current_location = data.get('currentLocation')
    destination = data.get('destination')

    # 최단 경로를 계산하기 위해 map.py의 main 함수 호출
    shortest_path = map.main(current_location, destination)

    # shortest_path가 존재하는 경우
    if shortest_path:
        response = {'shortestPath': shortest_path}

        # shortest_path를 텍스트 파일로 저장
        file_path = 'shortest_path.txt'

        # 파일이 이미 존재하는 경우 삭제
        if os.path.exists(file_path):
            os.remove(file_path)

        with open(file_path, 'w') as file:
            file.write(shortest_path)

    else:
        response = {'error': '시작 노드에서 도착 노드까지 경로가 존재하지 않습니다.', 'shortestPath': None}

    return jsonify(response)


@app.route('/navigate', methods=['POST'])
def navigate():
    # 클라이언트로부터 전달된 와이파이 리스트 가져오기
    data = request.get_json()
    wifi_list = data.get('wifiList', [])

    # 예측을 위해 입력 데이터 형식 변환
    input_data = []
    for wifi in wifi_list:
        bssid = wifi.get('BSSID')
        rssi = wifi.get('RSSI')
        app.logger.info('BSSID: %s, RSSI: %s', bssid, rssi)  # 클라이언트에서 받은 값을 로그로 출력
        input_data.append([bssid, rssi])

    with open('test.csv', 'w') as file:
        write = csv.writer(file)
        write.writerow(input_data)

    # base.csv 파일을 데이터프레임으로 읽어오기
    df = pd.read_csv(base_csv_file)

    # BSSID와 받아온 값 매핑
    for received_value in input_data:
        bssid, rssi = received_value
        # BSSID 값이 일치하는 열의 인덱스를 찾기
        matching_columns = df.columns[df.columns == bssid]

        # 일치하는 BSSID 값이 존재하는 경우에만 RSSI 값을 변경
        if len(matching_columns) > 0:
            column_index = matching_columns[0]
            df[column_index] = rssi

    # 모델에 예측 입력 데이터 전달
    X = df.drop(columns=['room'])

    # 모델 예측
    predictions = model.predict(X)
    predictions = [str(pred) for pred in predictions]  # 모든 원소를 문자열로 변환

    # 새롭게 현재위치가 갱신이 되면 다시 shortest path를 받아 파일에 다시 쓰기
    # 현재 위치는 예측값 목적지는 shortest path의 맨 마지막 값
    file_path = 'shortest_path.txt'
    with open(file_path, 'r') as file:
        shortest_path = file.read()

    path_list = shortest_path.split(' -> ')

    current_location = predictions
    destination = path_list[-1]

    # 최단 거리 갱신된 위치를 기반으로 다시 받아오기
    new_shortest_path = map.main(current_location, destination)

    # 파일이 이미 존재하는 경우 삭제
    if os.path.exists(file_path):
        os.remove(file_path)
    # shortest_path.txt에 새로운 최단 경로 쓰기
    with open(file_path, 'w') as file:
        file.write(new_shortest_path)

    distance = navigate.main(predictions)
    direction = navigate.direction(predictions)

    return distance


if __name__ == '__main__':
    app.run(debug=True)
