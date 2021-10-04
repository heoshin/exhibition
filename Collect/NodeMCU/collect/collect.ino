#include <Adafruit_SSD1306.h>
#include <splash.h>

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>
#include <DHT.h>
#include <MHZ19PWM.h>
<<<<<<< HEAD

const char* ssid     = "CollecterServer";
=======
#include <SoftwareSerial.h>
#include <PMS.h>

SoftwareSerial pms7003(D7, D8);

PMS pms(pms7003);
PMS::DATA data;

const char* ssid     = "CollecterServer";
// const char* ssid     = "Heoshin-Thinkpad";
>>>>>>> f54a677 (first)
const char* password = "12345678";
String host = "http://192.168.137.1";

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
<<<<<<< HEAD
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);
=======
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, 2);
>>>>>>> f54a677 (first)

WiFiClient client;
HTTPClient http;

<<<<<<< HEAD
DHT dht(2, DHT11);
MHZ19PWM mhz(14, MHZ_CONTINUOUS_MODE);

=======
DHT dht(2, DHT22);
MHZ19PWM mhz(14, MHZ_CONTINUOUS_MODE);

struct Pm
{
  int pm1 = 0;
  int pm2 = 0;
  int pm10 = 0;
};

Pm getPm();

>>>>>>> f54a677 (first)
void DisplayInit();
void DisplayInit();
void DisplayPrint(String str, bool isEnter = true);
void WifiInit(String _ssid, String _pass);
String RequestGet(String _url);
String RequestPost(String _url, String _post);

<<<<<<< HEAD
void setup()
{
  Serial.begin(115200);
  DisplayInit();
  WifiInit(ssid, password);

  dht.begin();
=======

void setup()
{
  Serial.begin(9600);
  DisplayInit();
  WifiInit(ssid, password);

  DisplayPrint("Start");
  dht.begin();
  Serial.flush();

  pms7003.begin(9600);  // GPIO2 (D4 pin on ESP-12E Development Board)
  pms.passiveMode();    // Switch to passive mode
  pms.wakeUp();
>>>>>>> f54a677 (first)
}

void loop()
{
  DisplayClear();
  int hum = dht.readHumidity();
  float tmp = dht.readTemperature();
  float co2 = mhz.getCO2();
<<<<<<< HEAD

  String request_url = host + String("/sendGET?mac=") + WiFi.macAddress() + String("&tmp=") + String(tmp) + String("&hum=") + String(hum)
    + String("&co2=") + String(co2);
=======
  int voc = analogRead(A0);
  // float pm = 0.0;

  // char float1[20] = {0,}; // atof()함수를 위해 char 자료형 배열을 10바이트 선언
  // int pos = 0;
  // while (Serial.available() > 0) {
  //   uint8_t temp = Serial.read();
  //   float1[pos] = temp;
  //   pos++;
  // }
  // Serial.println(float1);
  // pm = atof(float1); // 문자 배열을 실수로 변환하는 함수, 배열 자료형은 char 
  // Serial.write(0);

  Pm pm = getPm();

  String request_url = host + String("/sendGET?mac=") + WiFi.macAddress()
    + String("&tmp=") + String(tmp) 
    + String("&hum=") + String(hum)
    + String("&co2=") + String(co2)
    + String("&pm1=") + String(pm.pm1)
    + String("&pm2=") + String(pm.pm2)
    + String("&pm10=") + String(pm.pm10)
    + String("&voc=") + String(voc);
    
>>>>>>> f54a677 (first)
  // String request_url = host + String("/sendPOST");
  String response = RequestGet(request_url);
  DisplayPrint(request_url);
  DisplayPrint(String("======Response======\n") + response);
  
	delay(2000);
}

void DisplayInit() {
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { // Address 0x3D for 128x64
    Serial.println(F("SSD1306 allocation failed"));
    for(;;);
  }
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0,0);
}

void DisplayClear() {
  Serial.println("\n=========clearDisplay=========");
  display.clearDisplay();
  display.setCursor(0,0);
}

void DisplayPrint(String str, bool isEnter) { //DisplayPrint([출력할 문자열], [개행 여부])
  Serial.print(str);
  display.print(str);
  if (isEnter) {
    Serial.println();
    display.println();
  }
  display.display();
}

void WifiInit(String _ssid, String _pass) {
  WiFi.begin(_ssid, _pass);
  DisplayPrint("MAC:" + String(WiFi.macAddress()));
  DisplayPrint("Connecting to\n" + String(ssid));
  while ( WiFi.status() != WL_CONNECTED ) {
    delay ( 500 );
    DisplayPrint(".", false);
  }
  DisplayClear();
  DisplayPrint("\nWiFi connected");
  DisplayPrint("IP address:");
  DisplayPrint(WiFi.localIP().toString());
  delay(2000);
  DisplayClear();
}

String RequestGet(String _url) {
  String response = "";
  http.begin(client, _url);
  http.setTimeout(1000);
  int httpCode = http.GET();
  if(httpCode == HTTP_CODE_OK) {
		response = http.getString();
	}
	else {
    response = String("err: ") + String(httpCode);
	}
	http.end();
  
  return response;
}

String RequestPost(String _url, String _post) {
  String response = "";
  http.begin(client, _url);
  http.setTimeout(1000);
  int httpCode = http.POST(_post);
  if(httpCode == HTTP_CODE_OK) {
		response = http.getString();
	}
	else {
    response = String("err: ") + String(httpCode);
	}
	http.end();
  
  return response;
<<<<<<< HEAD
=======
}

Pm getPm() {
  Pm pm;
  pms.requestRead();
  if (pms.readUntil(data))
  {
    pm.pm1 = data.PM_AE_UG_1_0;
    pm.pm2 = data.PM_AE_UG_2_5;
    pm.pm10 = data.PM_AE_UG_10_0;
  }
  else
  {
    Serial.println("No data.");
  }
  return pm;
>>>>>>> f54a677 (first)
}