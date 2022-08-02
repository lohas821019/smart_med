
#%%
from flask import Flask
from flask import Flask, render_template, request

import serial
import time
import numpy as np

COM_PORT = 'COM4'
baudRate = 115200
try:
    ser = serial.Serial(COM_PORT, baudRate, timeout=0.5)
except serial.SerialException as e:
    print(e)
    
#%%
app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            signal = '1'
            data = np.array(signal).tobytes()
            ser.write(data)            # 訊息必須是位元組類型
            print(1)

        elif  request.form.get('action2') == 'VALUE2':
            signal = '2'
            data = np.array(signal).tobytes()
            ser.write(data)            # 訊息必須是位元組類型
            print(2)

        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template("index.html")

@app.route('/get_toggled_status') 
def toggled_status():
  current_status = request.args.get('status')
  return 'clicked' if current_status == 'Unclicked' else 'Unclicked'

if __name__ == '__main__':
    app = Flask(__name__)                 # 例項化flask
    app.config.from_object(Config())      # 為例項化的 flask 引入配置 
    app.debug = True
    app.run()                                  # 啟動 flask