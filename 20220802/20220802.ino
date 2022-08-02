#include <Arduino.h>

int ledState = LOW;  
const int ledPin = 10;
char cmd[10];
int recv;

void setup()
{
    Serial.begin(115200); 
    pinMode(ledPin, OUTPUT);
}

void loop()
{
  if (Serial.available() > 0) {
  // 讀取收到的資料

    Serial.readBytes(cmd, 10);
    //Serial.readBytes()返回放置在緩衝區中的字符數。0 表示未找到有效數據。

    recv = atoi(cmd);
    //這邊沒有值的時候會一直收到0，所以上方recv == 0，要都設定成LOW，要不然會一直跑

    Serial.println(recv);
    //atoi將字符串轉換爲整型值。
    
    if (recv == 1) {
      ledState = HIGH;
      digitalWrite(ledPin, ledState);
      }
      
    if (recv == 2) {
      ledState = LOW;
      digitalWrite(ledPin, ledState);
      }      
  }
}
