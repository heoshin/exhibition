#include <MHZ19PWM.h>         //'MHZ19PWM.h' 포함

MHZ19PWM mhz(14, MHZ_CONTINUOUS_MODE);

void setup()
{
  Serial.begin(115200);
  Serial.println("Starting...");

  // mhz.useLimit(5000);
}

void loop()
{
  Serial.println(mhz.getCO2());
}