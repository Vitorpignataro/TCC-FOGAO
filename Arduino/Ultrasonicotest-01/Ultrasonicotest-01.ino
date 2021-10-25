#include <NewPing.h>

#define TRIGGER_PING 12
#define ECHO_PIN 11
#define MAX_DISTANCE 200

NewPing sonar(TRIGGER_PING, ECHO_PIN, MAX_DISTANCE);

void setup() {
  Serial.begin(9600);
  Serial.print(sonar.ping_cm());
}

void loop() {
  delay(50);
  Serial.print("ping: ");
  Serial.print(sonar.ping_cm());
  Serial.println("cm");
  }
