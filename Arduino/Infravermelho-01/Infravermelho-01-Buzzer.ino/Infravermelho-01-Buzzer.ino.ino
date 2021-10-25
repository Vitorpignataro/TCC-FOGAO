#define pinoSensor 12
int buzzer2 = 9;

void setup() {
  pinMode(pinoSensor, INPUT);
  Serial.begin(9600);
  pinMode(buzzer2, OUTPUT);
}

void loop() {
  bool estadoSensor = digitalRead(pinoSensor);

  if(estadoSensor){
    Serial.println("Não captou");
    digitalWrite(buzzer2, LOW);
  }
  else{
    Serial.println("CAPTOU");
  digitalWrite(buzzer2, HIGH);
  }
  
}
