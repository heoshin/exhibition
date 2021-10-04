#include <SoftwareSerial.h>
#include <PMS.h>

SoftwareSerial pms7003(D7, D8);

PMS pms(pms7003);
PMS::DATA data;

struct Pm
{
  int pm1_0 = 0;
  int pm2_5 = 0;
  int pm10_0 = 0;
};

Pm getPm() {
  Pm pm;
  pms.requestRead();
  if (pms.readUntil(data))
  {
    pm.pm1_0 = data.PM_AE_UG_1_0;
    pm.pm2_5 = data.PM_AE_UG_2_5;
    pm.pm10_0 = data.PM_AE_UG_10_0;
  }
  else
  {
    Serial.println("No data.");
  }
  return pm;
}

void setup()
{
  Serial.begin(9600);   // GPIO1, GPIO3 (TX/RX pin on ESP-12E Development Board)
  pms7003.begin(9600);  // GPIO2 (D4 pin on ESP-12E Development Board)
  pms.passiveMode();    // Switch to passive mode
  pms.wakeUp();
}

void loop()
{
  int pm1_0 = 0, pm2_5 = 0, pm10_0 = 0;

  delay(1000);

  Pm pm = getPm();

  Serial.printf("PM 1.0: %d  PM 2.5: %d  PM 10.0: %d\n", pm.pm1_0, pm.pm2_5, pm.pm10_0);

  // pms.sleep();
  delay(2000);
}