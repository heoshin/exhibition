#include <DHT.h>
DHT dht(0, DHT11);

void setup()
{
  Serial.begin(115200);
  dht.begin();
}
 
void loop() 
{
  delay(10);

  float h = dht.readHumidity(); // 습도값을 h에 저장
  float t = dht.readTemperature(); // 온도값을 t에 저장
  Serial.print("Humidity: "); // 문자열 출력
  Serial.print(h); // 습도값 출력
  Serial.print("% ");
  Serial.print("Temperature: ");
  Serial.print(t); // 온도값 출력
  Serial.println("C");
}