#include <CapacitiveSensor.h>

CapacitiveSensor ligaFogao = CapacitiveSensor(3, 2);
CapacitiveSensor aumentaTemp = CapacitiveSensor(6, 5);
CapacitiveSensor diminuiTemp = CapacitiveSensor(9, 8);

const int trigPin = 10;
const int echoPing = 11;

long duration;
int distance;

int count = 0;

int valorMIN = 2400;



void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPing, INPUT);
  Serial.begin(9600);
}

void loop() {
 
  long valorLiga = ligaFogao.capacitiveSensor(30);
  long valorAume = aumentaTemp.capacitiveSensor(30);
  long valorDimi = diminuiTemp.capacitiveSensor(30);
  
  
  if (valorLiga > valorMIN) {
    Serial.println("FogaoLigado");
  }
  else{
    Serial.println("BotaoOFF");
  }
  
  if (valorAume > valorMIN) {
    Serial.println("Aumenta");
  }
  else{
    Serial.println("BotaoOFF");
  }
  
  if (valorDimi > valorMIN) {
    Serial.println("Diminui");
  }
  else{
    Serial.println("BotaoOFF");
  }
  if(count  == 0){
    digitalWrite(trigPin, LOW);
    delayMicroseconds(10);
    
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(trigPin, LOW);
  
    duration = pulseIn(echoPing, HIGH);
    distance = duration*0.034/2;

    if(distance == 10 || distance == 11){
        delay(600);
        count +=1;
        Serial.println(distance);
    }
    
  }
  

  delay(200);
}
