from flask import Flask, request, jsonify
import joblib, csv
import pandas as pd

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


if __name__ == '__main__':
    app.run(debug=True)
