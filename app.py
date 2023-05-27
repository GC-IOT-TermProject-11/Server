from flask import Flask, request, jsonify
import joblib
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
    wifi_list = data.get('wifi_list', [])

    # 예측을 위해 입력 데이터 형식 변환
    input_data = []
    for wifi in wifi_list:
        bssid = wifi.get('bssid')
        rssi = wifi.get('rssi')
        input_data.append([bssid, rssi])

    # base.csv 파일을 데이터프레임으로 읽어오기
    df = pd.read_csv(base_csv_file)

     # BSSID와 받아온 값 매핑
    for received_value in input_data:
        bssid, rssi = received_value
        if bssid in df.columns:
            df.loc[df['BSSID'] == bssid, 'RSSI'] = rssi  # 값 교체

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
