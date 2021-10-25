#define PinoSen 7
#define PinoBuzzer 8


void setup() {
  pinMode(PinoSen, INPUT);
  pinMode(PinoBuzzer, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  bool sensorReflexivo = digitalRead(PinoSen);

  if(!sensorReflexivo){
    Serial.println("Não Achou");
    digitalWrite(PinoBuzzer, LOW);
  }
  else{
    Serial.println("Achou");
    digitalWrite(PinoBuzzer, HIGH);
    delay(500);
    while(sensorReflexivo == true){
      digitalWrite(PinoBuzzer, LOW);
      sensorReflexivo = digitalRead(PinoSen);
    }
  }

}
