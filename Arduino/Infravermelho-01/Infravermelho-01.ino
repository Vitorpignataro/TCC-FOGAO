#define pinoSensor 12

void setup() {
  pinMode(pinoSensor, INPUT);
  Serial.begin(9600);
}

void loop() {
  bool estadoSensor = digitalRead(pinoSensor);

  if(estadoSensor){
    Serial.println("Não captou"); 
  }
  else{
    Serial.println("CAPTOU");
  }
  
}
