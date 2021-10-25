#include <NewPing.h>

#define TRIGGER_PING 12
#define ECHO_PIN 11
#define MAX_DISTANCE 200
int buzzer2 = 9;


NewPing sonar(TRIGGER_PING, ECHO_PIN, MAX_DISTANCE);

void setup() {
  Serial.begin(9600);
  pinMode(buzzer2, OUTPUT);
}

void loop() {
  Serial.print("ping: ");
  Serial.print(sonar.ping_cm());
  Serial.println("cm");

    if(sonar.ping_cm() <= 30){
      digitalWrite(buzzer2, HIGH);
      //delay(500);
      //while(sonar.ping_cm() <= 55){
        //sonar.ping_cm();
        //digitalWrite(buzzer2, LOW);
     // }
    }
    else {
      digitalWrite(buzzer2, LOW);
    }
  }
